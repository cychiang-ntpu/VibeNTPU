-- Pickle Charm Shop：Supabase 資料表與安全規則
-- 使用方式：全選複製 → Supabase 左側 SQL Editor → New query → 貼上 → Run
-- 這份 SQL 可以重複執行，不會重複建立。

-- ============================================================
-- 1. profiles：會員的顯示名稱（帳號本身由 Supabase Auth 管理）
-- ============================================================
create table if not exists public.profiles (
  id         uuid primary key references auth.users (id) on delete cascade,
  name       text not null default '',
  created_at timestamptz not null default now()
);

alter table public.profiles enable row level security;

drop policy if exists "profiles: 自己可讀" on public.profiles;
create policy "profiles: 自己可讀" on public.profiles
  for select using (auth.uid() = id);

drop policy if exists "profiles: 自己可新增" on public.profiles;
create policy "profiles: 自己可新增" on public.profiles
  for insert with check (auth.uid() = id);

drop policy if exists "profiles: 自己可修改" on public.profiles;
create policy "profiles: 自己可修改" on public.profiles
  for update using (auth.uid() = id);

-- 註冊時自動建立 profile（姓名來自註冊時附帶的 name）
create or replace function public.handle_new_user()
returns trigger
language plpgsql
security definer set search_path = public
as $$
begin
  insert into public.profiles (id, name)
  values (new.id, coalesce(new.raw_user_meta_data ->> 'name', ''))
  on conflict (id) do nothing;
  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- ============================================================
-- 2. cart_items：購物車，每個會員一份
-- ============================================================
create table if not exists public.cart_items (
  id           bigint generated always as identity primary key,
  user_id      uuid not null references auth.users (id) on delete cascade,
  product_name text not null,
  unit_price   integer not null check (unit_price >= 0),
  qty          integer not null check (qty > 0),
  updated_at   timestamptz not null default now(),
  unique (user_id, product_name)
);

alter table public.cart_items enable row level security;

drop policy if exists "cart: 自己的購物車" on public.cart_items;
create policy "cart: 自己的購物車" on public.cart_items
  for all using (auth.uid() = user_id) with check (auth.uid() = user_id);

-- ============================================================
-- 3. orders：訂單，會員只能新增與查看自己的；狀態由老闆在後台改
-- ============================================================
create table if not exists public.orders (
  id         bigint generated always as identity primary key,
  user_id    uuid not null references auth.users (id) on delete cascade,
  email      text,
  name       text not null,
  phone      text not null,
  address    text not null,
  note       text,
  items      jsonb not null,
  total      integer not null check (total >= 0),
  status     text not null default 'pending',
  created_at timestamptz not null default now()
);

alter table public.orders enable row level security;

drop policy if exists "orders: 自己可新增" on public.orders;
create policy "orders: 自己可新增" on public.orders
  for insert with check (auth.uid() = user_id);

drop policy if exists "orders: 自己可查看" on public.orders;
create policy "orders: 自己可查看" on public.orders
  for select using (auth.uid() = user_id);

-- 會員不能修改或刪除訂單（沒有 update / delete 規則）。
-- 老闆在 Supabase 後台（Table Editor）改狀態，不受 RLS 限制。

-- ============================================================
-- 4.（選做）老闆報表：每種商品賣了幾個、賣了多少錢
--    在 SQL Editor 單獨貼這一段執行即可。
-- ============================================================
-- select
--   item ->> 'name'                         as 商品,
--   sum((item ->> 'qty')::int)              as 數量,
--   sum((item ->> 'qty')::int * (item ->> 'price')::int) as 金額
-- from public.orders, jsonb_array_elements(items) as item
-- group by 1
-- order by 3 desc;
