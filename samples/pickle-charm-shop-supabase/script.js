// Pickle Charm Shop（Supabase 版）
// 第一部分：連線 Supabase
// 第二部分：註冊／登入（Supabase Auth）
// 第三部分：購物車（cart_items 資料表）
// 第四部分：訂單與「我的訂單」（orders 資料表）

/* ========== 連線 Supabase ========== */

// 請換成你的 Supabase 專案設定（Project Settings → API）
const SUPABASE_URL = "https://YOUR-PROJECT.supabase.co";
const SUPABASE_ANON_KEY = "YOUR-ANON-KEY";
const db = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

const CONNECTION_ERROR = '連線失敗，請稍後再試';

/* ========== 註冊／登入 ========== */

const loginBtn = document.getElementById('login-btn');
const logoutBtn = document.getElementById('logout-btn');
const welcomeText = document.getElementById('welcome-text');
const signupModal = document.getElementById('signup-modal');
const signupTitle = document.getElementById('signup-title');
const authForm = document.getElementById('auth-form');
const authNote = document.getElementById('auth-note');
const authNameLabel = document.getElementById('auth-name-label');
const authNameInput = document.getElementById('auth-name');
const authEmailInput = document.getElementById('auth-email');
const authPasswordInput = document.getElementById('auth-password');
const authSubmit = document.getElementById('auth-submit');
const authError = document.getElementById('auth-error');
const modeButtons = document.querySelectorAll('.mode-btn');
const orderNameInput = document.getElementById('order-name');

// 目前登入者：{ id, email, name } 或 null
let currentUser = null;
let authMode = 'login';

function setMode(mode) {
  authMode = mode;
  const isSignup = mode === 'signup';
  signupTitle.textContent = isSignup ? '註冊' : '登入';
  authNameLabel.hidden = !isSignup;
  authNameInput.required = isSignup;
  authPasswordInput.autocomplete = isSignup ? 'new-password' : 'current-password';
  modeButtons.forEach((btn) => {
    btn.setAttribute('aria-pressed', btn.dataset.mode === mode ? 'true' : 'false');
  });
  authError.hidden = true;
}

function showAuthError(message) {
  authError.textContent = message;
  authError.hidden = false;
}

function openModal(note) {
  signupModal.hidden = false;
  authError.hidden = true;
  if (note) {
    authNote.textContent = note;
    authNote.hidden = false;
  } else {
    authNote.textContent = '';
    authNote.hidden = true;
  }
  document.body.classList.add('no-scroll');
  const first = authMode === 'signup' ? authNameInput : authEmailInput;
  first.focus();
}

function closeModal() {
  signupModal.hidden = true;
  document.body.classList.remove('no-scroll');
}

async function fetchProfileName(userId) {
  const { data, error } = await db
    .from('profiles')
    .select('name')
    .eq('id', userId)
    .single();
  if (error || !data || !data.name) return '';
  return data.name;
}

function renderUser() {
  if (currentUser) {
    welcomeText.textContent = '歡迎回來，' + currentUser.name;
    welcomeText.hidden = false;
    loginBtn.hidden = true;
    logoutBtn.hidden = false;
    if (!orderNameInput.value) orderNameInput.value = currentUser.name;
  } else {
    welcomeText.textContent = '';
    welcomeText.hidden = true;
    loginBtn.hidden = false;
    logoutBtn.hidden = true;
  }
}

// 以 session 更新 currentUser，接著重新載入購物車與訂單。
// 登入時表單與 onAuthStateChange 都會呼叫這裡，用 loadSeq 確保只有最後一次更新畫面。
let loadSeq = 0;

async function applySession(session) {
  const seq = ++loadSeq;
  const user = session ? session.user : null;
  if (user) {
    const profileName = await fetchProfileName(user.id);
    currentUser = {
      id: user.id,
      email: user.email || '',
      name: profileName || user.email || '',
    };
  } else {
    currentUser = null;
  }
  if (seq !== loadSeq) return;
  renderUser();
  await Promise.all([loadCart(seq), loadOrders(seq)]);
}

// 回傳 true 表示這次載入已經過時（之後又有新的登入／登出），不要再更新畫面
function isStale(seq) {
  return seq !== undefined && seq !== loadSeq;
}

loginBtn.addEventListener('click', () => {
  setMode('login');
  openModal('');
});

modeButtons.forEach((btn) => {
  btn.addEventListener('click', () => setMode(btn.dataset.mode));
});

signupModal.querySelectorAll('[data-close-modal]').forEach((el) => {
  el.addEventListener('click', closeModal);
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    if (!signupModal.hidden) closeModal();
    if (cartPanel.classList.contains('open')) closeCart();
  }
});

authForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  authError.hidden = true;
  const email = authEmailInput.value.trim();
  const password = authPasswordInput.value;
  const name = authNameInput.value.trim();

  if (password.length < 6) {
    showAuthError('密碼至少 6 個字');
    return;
  }

  authSubmit.disabled = true;
  try {
    let result;
    if (authMode === 'signup') {
      result = await db.auth.signUp({
        email,
        password,
        options: { data: { name } },
      });
    } else {
      result = await db.auth.signInWithPassword({ email, password });
    }
    if (result.error) {
      showAuthError(result.error.message);
      return;
    }
    if (!result.data.session) {
      // Confirm email 未關閉時，註冊後不會直接登入
      showAuthError('註冊成功，請到信箱確認 Email 後再登入');
      return;
    }
    authForm.reset();
    closeModal();
    await applySession(result.data.session);
  } catch (error) {
    showAuthError(CONNECTION_ERROR);
  } finally {
    authSubmit.disabled = false;
  }
});

logoutBtn.addEventListener('click', async () => {
  logoutBtn.disabled = true;
  try {
    await db.auth.signOut();
  } catch (error) {
    // 即使登出失敗也把畫面清掉
  }
  orderNameInput.value = '';
  logoutBtn.disabled = false;
  await applySession(null);
});

/* ========== 購物車 ========== */

const cartBtn = document.getElementById('cart-btn');
const cartCountEl = document.getElementById('cart-count');
const cartPanel = document.getElementById('cart-panel');
const cartOverlay = document.getElementById('cart-overlay');
const cartClose = document.getElementById('cart-close');
const cartBody = document.getElementById('cart-body');
const cartItemsEl = document.getElementById('cart-items');
const cartEmptyEl = document.getElementById('cart-empty');
const cartTotalEl = document.getElementById('cart-total');
const cartError = document.getElementById('cart-error');
const orderForm = document.getElementById('order-form');
const orderPhoneInput = document.getElementById('order-phone');
const orderAddressInput = document.getElementById('order-address');
const orderNoteInput = document.getElementById('order-note');
const orderSubmit = document.getElementById('order-submit');
const orderError = document.getElementById('order-error');
const cartSuccess = document.getElementById('cart-success');
const successTitle = document.getElementById('success-title');
const successItems = document.getElementById('success-items');
const successTotal = document.getElementById('success-total');
const successClose = document.getElementById('success-close');

// cart 的結構：[{ name, price, qty }]（從 cart_items 讀出來的複本）
let cart = [];

function showCartError(message) {
  cartError.textContent = message;
  cartError.hidden = false;
}

function hideCartError() {
  cartError.hidden = true;
}

function cartTotal() {
  return cart.reduce((sum, item) => sum + item.price * item.qty, 0);
}

function cartQuantity() {
  return cart.reduce((sum, item) => sum + item.qty, 0);
}

// 從 cart_items 讀自己的購物車（RLS 只會回傳自己的列）
async function loadCart(seq) {
  if (!currentUser) {
    cart = [];
    hideCartError();
    renderCart();
    return;
  }
  const { data, error } = await db
    .from('cart_items')
    .select('product_name, unit_price, qty')
    .eq('user_id', currentUser.id)
    .order('id', { ascending: true });
  if (isStale(seq)) return;
  if (error) {
    showCartError(CONNECTION_ERROR);
    return;
  }
  hideCartError();
  cart = (data || []).map((row) => ({
    name: row.product_name,
    price: row.unit_price,
    qty: row.qty,
  }));
  renderCart();
}

async function addToCart(name, price) {
  if (!currentUser) {
    setMode('login');
    openModal('請先登入再加入購物車');
    return;
  }
  const found = cart.find((item) => item.name === name);
  const qty = found ? found.qty + 1 : 1;
  const { error } = await db.from('cart_items').upsert(
    {
      user_id: currentUser.id,
      product_name: name,
      unit_price: price,
      qty,
    },
    { onConflict: 'user_id,product_name' }
  );
  if (error) {
    showCartError(CONNECTION_ERROR);
    openCart();
    return;
  }
  await loadCart();
}

async function changeQty(name, delta) {
  if (!currentUser) return;
  const found = cart.find((item) => item.name === name);
  if (!found) return;
  const qty = found.qty + delta;
  let result;
  if (qty <= 0) {
    result = await db
      .from('cart_items')
      .delete()
      .eq('user_id', currentUser.id)
      .eq('product_name', name);
  } else {
    result = await db
      .from('cart_items')
      .update({ qty })
      .eq('user_id', currentUser.id)
      .eq('product_name', name);
  }
  if (result.error) {
    showCartError(CONNECTION_ERROR);
    return;
  }
  await loadCart();
}

function makeQtyButton(label, ariaLabel, onClick) {
  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'qty-btn';
  btn.textContent = label;
  btn.setAttribute('aria-label', ariaLabel);
  btn.addEventListener('click', onClick);
  return btn;
}

function renderCart() {
  cartItemsEl.textContent = '';
  cart.forEach((item) => {
    const li = document.createElement('li');
    li.className = 'cart-item';

    const info = document.createElement('div');
    info.className = 'cart-item-info';
    const name = document.createElement('strong');
    name.textContent = item.name;
    const price = document.createElement('span');
    price.textContent = '單價 NT$ ' + item.price;
    info.append(name, price);

    const controls = document.createElement('div');
    controls.className = 'cart-item-controls';
    const qty = document.createElement('span');
    qty.className = 'qty';
    qty.textContent = item.qty;
    controls.append(
      makeQtyButton('−', '減少 ' + item.name + ' 數量', () => changeQty(item.name, -1)),
      qty,
      makeQtyButton('+', '增加 ' + item.name + ' 數量', () => changeQty(item.name, 1))
    );

    const subtotal = document.createElement('div');
    subtotal.className = 'cart-item-subtotal';
    subtotal.textContent = 'NT$ ' + item.price * item.qty;

    li.append(info, controls, subtotal);
    cartItemsEl.appendChild(li);
  });

  const empty = cart.length === 0;
  cartEmptyEl.hidden = !empty;
  cartTotalEl.textContent = cartTotal();
  cartCountEl.textContent = cartQuantity();
  orderSubmit.disabled = empty;
  orderSubmit.textContent = empty ? '購物車是空的' : '送出訂單';
}

function openCart() {
  cartPanel.classList.add('open');
  cartPanel.setAttribute('aria-hidden', 'false');
  cartBtn.setAttribute('aria-expanded', 'true');
  cartOverlay.hidden = false;
  document.body.classList.add('no-scroll');
}

function closeCart() {
  cartPanel.classList.remove('open');
  cartPanel.setAttribute('aria-hidden', 'true');
  cartBtn.setAttribute('aria-expanded', 'false');
  cartOverlay.hidden = true;
  document.body.classList.remove('no-scroll');
}

cartBtn.addEventListener('click', () => {
  if (cartPanel.classList.contains('open')) {
    closeCart();
  } else {
    openCart();
  }
});
cartClose.addEventListener('click', closeCart);
cartOverlay.addEventListener('click', closeCart);

document.querySelectorAll('.buy-btn').forEach((button) => {
  button.addEventListener('click', async () => {
    const name = button.dataset.name;
    const price = Number(button.dataset.price);
    if (!name || Number.isNaN(price)) return;
    button.classList.add('added');
    setTimeout(() => button.classList.remove('added'), 400);
    await addToCart(name, price);
  });
});

/* ========== 下訂單 ========== */

orderForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  if (cart.length === 0) return;
  orderError.hidden = true;
  if (!currentUser) {
    orderError.textContent = '請先登入再送出訂單';
    orderError.hidden = false;
    return;
  }

  const items = cart.map((item) => ({ name: item.name, price: item.price, qty: item.qty }));
  const total = cartTotal();

  orderSubmit.disabled = true;
  try {
    const { data: order, error } = await db
      .from('orders')
      .insert({
        user_id: currentUser.id,
        email: currentUser.email,
        name: orderNameInput.value.trim(),
        phone: orderPhoneInput.value.trim(),
        address: orderAddressInput.value.trim(),
        note: orderNoteInput.value.trim(),
        items,
        total,
      })
      .select()
      .single();
    if (error) throw error;

    // 成功：清空自己的 cart_items，顯示摘要
    const { error: clearError } = await db
      .from('cart_items')
      .delete()
      .eq('user_id', currentUser.id);
    if (clearError) {
      showCartError(CONNECTION_ERROR);
    }
    cart = [];
    renderCart();
    orderForm.reset();
    orderNameInput.value = currentUser.name;

    successTitle.textContent = '訂單已送出，訂單編號 #' + order.id;
    successItems.textContent = '';
    items.forEach((item) => {
      const li = document.createElement('li');
      li.textContent = item.name + ' x' + item.qty;
      successItems.appendChild(li);
    });
    successTotal.textContent = total;
    cartBody.hidden = true;
    cartSuccess.hidden = false;
    await loadOrders();
  } catch (error) {
    orderError.textContent = (error && error.message) ? error.message : CONNECTION_ERROR;
    orderError.hidden = false;
    orderSubmit.disabled = false;
  }
});

successClose.addEventListener('click', () => {
  cartSuccess.hidden = true;
  cartBody.hidden = false;
  closeCart();
});

/* ========== 我的訂單 ========== */

const ordersNote = document.getElementById('orders-note');
const orderListEl = document.getElementById('order-list');

const STATUS_LABELS = {
  pending: '處理中',
  shipped: '已出貨',
};

function statusLabel(status) {
  return STATUS_LABELS[status] || status;
}

function formatDate(value) {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return '';
  return date.toLocaleString('zh-TW', { hour12: false });
}

function itemsSummary(items) {
  if (!Array.isArray(items)) return '';
  return items.map((item) => item.name + ' x' + item.qty).join('、');
}

function showOrdersNote(message) {
  ordersNote.textContent = message;
  ordersNote.hidden = false;
}

async function loadOrders(seq) {
  orderListEl.textContent = '';
  if (!currentUser) {
    showOrdersNote('登入後可查看訂單');
    return;
  }
  const { data, error } = await db
    .from('orders')
    .select('id, created_at, items, total, status')
    .eq('user_id', currentUser.id)
    .order('created_at', { ascending: false });
  if (isStale(seq)) return;
  orderListEl.textContent = '';
  if (error) {
    showOrdersNote(CONNECTION_ERROR);
    return;
  }
  if (!data || data.length === 0) {
    showOrdersNote('還沒有訂單');
    return;
  }
  ordersNote.hidden = true;
  data.forEach((order) => {
    const li = document.createElement('li');
    li.className = 'order-card';

    const head = document.createElement('div');
    head.className = 'order-head';
    const idEl = document.createElement('strong');
    idEl.textContent = '訂單編號 #' + order.id;
    const status = document.createElement('span');
    status.className = 'order-status order-status-' + order.status;
    status.textContent = statusLabel(order.status);
    head.append(idEl, status);

    const date = document.createElement('p');
    date.className = 'order-date';
    date.textContent = formatDate(order.created_at);

    const summary = document.createElement('p');
    summary.className = 'order-items';
    summary.textContent = itemsSummary(order.items);

    const total = document.createElement('p');
    total.className = 'order-total';
    total.textContent = '總金額 NT$ ' + order.total;

    li.append(head, date, summary, total);
    orderListEl.appendChild(li);
  });
}

/* ========== 初始化 ========== */

setMode('login');
renderCart();

db.auth.onAuthStateChange((event, session) => {
  if (event === 'INITIAL_SESSION') return;
  applySession(session);
});

db.auth
  .getSession()
  .then(({ data }) => applySession(data ? data.session : null))
  .catch(() => applySession(null));
