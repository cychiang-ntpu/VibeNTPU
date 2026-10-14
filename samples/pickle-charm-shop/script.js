// Pickle Charm Shop
// 第一部分：註冊／登入（localStorage "pickleUser"）
// 第二部分：購物車與下訂單（localStorage "pickleCart"）

const USER_KEY = 'pickleUser';
const CART_KEY = 'pickleCart';

/* ---------- 共用：localStorage 讀寫 ---------- */

function readJSON(key, fallback) {
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : fallback;
  } catch (error) {
    return fallback;
  }
}

function writeJSON(key, value) {
  localStorage.setItem(key, JSON.stringify(value));
}

/* ---------- 共用：以 fetch 送出 Netlify 表單 ---------- */

function postForm(form) {
  return fetch('/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams(new FormData(form)).toString(),
  });
}

/* ========== 註冊／登入 ========== */

const loginBtn = document.getElementById('login-btn');
const logoutBtn = document.getElementById('logout-btn');
const welcomeText = document.getElementById('welcome-text');
const signupModal = document.getElementById('signup-modal');
const signupForm = document.getElementById('signup-form');
const signupError = document.getElementById('signup-error');
const orderNameInput = document.getElementById('order-name');
const orderEmailInput = document.getElementById('order-email');

function getUser() {
  return readJSON(USER_KEY, null);
}

function renderUser() {
  const user = getUser();
  if (user && user.name) {
    welcomeText.textContent = '歡迎回來，' + user.name;
    welcomeText.hidden = false;
    loginBtn.hidden = true;
    logoutBtn.hidden = false;
    if (!orderNameInput.value) orderNameInput.value = user.name;
    orderEmailInput.value = user.email || '';
  } else {
    welcomeText.textContent = '';
    welcomeText.hidden = true;
    loginBtn.hidden = false;
    logoutBtn.hidden = true;
    orderEmailInput.value = '';
  }
}

function openModal() {
  signupModal.hidden = false;
  signupError.hidden = true;
  document.body.classList.add('no-scroll');
  const first = signupForm.querySelector('input[name="name"]');
  if (first) first.focus();
}

function closeModal() {
  signupModal.hidden = true;
  document.body.classList.remove('no-scroll');
}

loginBtn.addEventListener('click', openModal);

signupModal.querySelectorAll('[data-close-modal]').forEach((el) => {
  el.addEventListener('click', closeModal);
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    if (!signupModal.hidden) closeModal();
    if (cartPanel.classList.contains('open')) closeCart();
  }
});

signupForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  signupError.hidden = true;
  const submitBtn = signupForm.querySelector('button[type="submit"]');
  submitBtn.disabled = true;
  try {
    const response = await postForm(signupForm);
    if (!response.ok) throw new Error('bad response');
    const data = new FormData(signupForm);
    writeJSON(USER_KEY, {
      name: String(data.get('name') || '').trim(),
      email: String(data.get('email') || '').trim(),
    });
    signupForm.reset();
    closeModal();
    renderUser();
  } catch (error) {
    signupError.textContent = '送出失敗，請確認網路後再試一次';
    signupError.hidden = false;
  } finally {
    submitBtn.disabled = false;
  }
});

logoutBtn.addEventListener('click', () => {
  localStorage.removeItem(USER_KEY);
  orderNameInput.value = '';
  renderUser();
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
const orderForm = document.getElementById('order-form');
const orderItemsInput = document.getElementById('order-items');
const orderTotalInput = document.getElementById('order-total');
const orderSubmit = document.getElementById('order-submit');
const orderError = document.getElementById('order-error');
const cartSuccess = document.getElementById('cart-success');
const successItems = document.getElementById('success-items');
const successTotal = document.getElementById('success-total');
const successClose = document.getElementById('success-close');

// cart 的結構：[{ name, price, qty }]
let cart = readJSON(CART_KEY, []);
if (!Array.isArray(cart)) cart = [];

function saveCart() {
  writeJSON(CART_KEY, cart);
}

function cartTotal() {
  return cart.reduce((sum, item) => sum + item.price * item.qty, 0);
}

function cartQuantity() {
  return cart.reduce((sum, item) => sum + item.qty, 0);
}

function cartSummaryText() {
  return cart.map((item) => item.name + ' x' + item.qty).join(', ');
}

function addToCart(name, price) {
  const found = cart.find((item) => item.name === name);
  if (found) {
    found.qty += 1;
  } else {
    cart.push({ name, price, qty: 1 });
  }
  saveCart();
  renderCart();
}

function changeQty(name, delta) {
  const found = cart.find((item) => item.name === name);
  if (!found) return;
  found.qty += delta;
  if (found.qty <= 0) {
    cart = cart.filter((item) => item.name !== name);
  }
  saveCart();
  renderCart();
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
  button.addEventListener('click', () => {
    const name = button.dataset.name;
    const price = Number(button.dataset.price);
    if (!name || Number.isNaN(price)) return;
    addToCart(name, price);
    button.classList.add('added');
    setTimeout(() => button.classList.remove('added'), 400);
  });
});

/* ========== 下訂單 ========== */

orderForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  if (cart.length === 0) return;
  orderError.hidden = true;

  // 送出前先填好隱藏欄位
  const summary = cart.map((item) => ({ name: item.name, qty: item.qty }));
  const total = cartTotal();
  orderItemsInput.value = cartSummaryText();
  orderTotalInput.value = String(total);
  const user = getUser();
  orderEmailInput.value = user && user.email ? user.email : '';

  orderSubmit.disabled = true;
  try {
    const response = await postForm(orderForm);
    if (!response.ok) throw new Error('bad response');

    // 成功：清空購物車，顯示摘要
    cart = [];
    saveCart();
    renderCart();
    orderForm.reset();
    if (user && user.name) orderNameInput.value = user.name;

    successItems.textContent = '';
    summary.forEach((item) => {
      const li = document.createElement('li');
      li.textContent = item.name + ' x' + item.qty;
      successItems.appendChild(li);
    });
    successTotal.textContent = total;
    cartBody.hidden = true;
    cartSuccess.hidden = false;
  } catch (error) {
    orderError.textContent = '送出失敗，請確認網路後再試一次';
    orderError.hidden = false;
    orderSubmit.disabled = false;
  }
});

successClose.addEventListener('click', () => {
  cartSuccess.hidden = true;
  cartBody.hidden = false;
  closeCart();
});

/* ========== 初始化 ========== */

renderUser();
renderCart();
