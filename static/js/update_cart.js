document.addEventListener('DOMContentLoaded', function () {
    const updateCart = () => {
        const getCart = localStorage.getItem('cart') || '[]';
        const cart = JSON.parse(getCart);
        const cartDrawer = document.getElementById('cart-drawer-bag');
        cartDrawer.innerHTML = '';

        if (cart && cart.length > 0) {
            cart.forEach(item => {
                const cartItem = document.createElement('div');
                const productTotalPrice = parseInt(item.price) * item.quantity;
                cartItem.className = 'cart-drawer-item d-flex position-relative';
                cartItem.dataset.slug = item.slug;
                cartItem.dataset.size = item.size; 
                cartItem.innerHTML = `
                    <div class="position-relative">
                      <a href="/shop/${item.slug}">
                        <img loading="lazy" class="cart-drawer-item__img" src="${item.image}" alt="">
                      </a>
                    </div>
                    <div class="cart-drawer-item__info flex-grow-1">
                      <h6 class="cart-drawer-item__title fw-normal"><a href="/shop/${item.slug}">${item.name}</a></h6>
                      <p class="cart-drawer-item__option text-secondary">Talla: ${item.size}</p>
                      <div class="d-flex align-items-center justify-content-between mt-1">
                        <div class="qty-control position-relative">
                          <input id="cart-product-quantity" type="number" name="quantity" value="${item.quantity}" min="1" class="qty-control__number border-0 text-center">
                          <div class="qty-control__reduce text-start">-</div>
                          <div class="qty-control__increase text-end">+</div>
                        </div>
                        <span id="cart-product-price" class="cart-drawer-item__price money price">$${productTotalPrice}</span>
                      </div>
                    </div>
                    <button class="btn-close-xs position-absolute top-0 end-0 js-cart-item-remove"></button>
                `;

                cartDrawer.appendChild(cartItem);

                const cartDrawerDivider = document.createElement('hr');
                cartDrawerDivider.className = 'cart-drawer-divider';
                cartDrawer.appendChild(cartDrawerDivider);
            });

            updateCartBadge();
            updateCartTotal();
            assignEventListeners();
        } else {
            cartDrawer.innerHTML = '<p style="text-align: center">No tienes productos en el carrito.</p>';
        }
    };

    const updateCartBadge = () => {
        const getCart = localStorage.getItem('cart') || '[]';
        const cart = JSON.parse(getCart);
        const cartBadge = document.querySelectorAll('.cart-amount')
        cartBadge.forEach((badge) => {
            badge.innerHTML = cart.length;
        });
    }

    const updateCartTotal = () => {
        const getCart = localStorage.getItem('cart') || '[]';
        const cart = JSON.parse(getCart);
        const cartTotal = document.getElementsByClassName('cart-subtotal')
        let total = 0;

        if (cart && cart.length > 0) {
            cart.forEach(item => {
                total += parseInt(item.price) * item.quantity;
            });
        };
        cartTotal.textContent = `$${total}`;
    };

    const assignEventListeners = () => {
        const qtyControlIncrease = document.querySelectorAll('.qty-control__increase');
        const qtyControlReduce = document.querySelectorAll('.qty-control__reduce');
        const cartItemRemove = document.querySelectorAll('.js-cart-item-remove');

        qtyControlIncrease.forEach((btn) => {
            btn.addEventListener('click', function () {
                const parent = this.parentElement;
                const input = parent.querySelector('input');
                const value = parseInt(input.value);
                //input.value = value + 1;

                const cartItem = this.closest('.cart-drawer-item');
                const slug = cartItem.dataset.slug;
                const size = cartItem.dataset.size;

                const cart = JSON.parse(localStorage.getItem('cart'));
                const index = cart.findIndex(item => item.slug === slug && item.size === size);

                if (index !== -1) {
                    cart[index].quantity = value + 1;
                    localStorage.setItem('cart', JSON.stringify(cart));
                    updateCart();
                } else {
                    console.error('Item not found in cart');
                }
            });
        });

        qtyControlReduce.forEach((btn) => {
            btn.addEventListener('click', function () {
                const parent = this.parentElement;
                const input = parent.querySelector('input');
                const value = parseInt(input.value);
                if (value > 1) {
                    //input.value = value - 1;

                    const cartItem = this.closest('.cart-drawer-item');
                    const slug = cartItem.dataset.slug;
                    const size = cartItem.dataset.size;

                    const cart = JSON.parse(localStorage.getItem('cart'));
                    const index = cart.findIndex(item => item.slug === slug && item.size === size);

                    if (index !== -1) {
                        cart[index].quantity = value - 1;
                        localStorage.setItem('cart', JSON.stringify(cart));
                        updateCart();
                    } else {
                        console.error('Item not found in cart');
                    }
                }
            });
        });

        cartItemRemove.forEach((btn) => {
            btn.addEventListener('click', function () {
                const cartItem = this.closest('.cart-drawer-item');
                const slug = cartItem.dataset.slug;
                const size = cartItem.dataset.size;

                const cart = JSON.parse(localStorage.getItem('cart'));
                const newCart = cart.filter(item => !(item.slug === slug && item.size === size));
                localStorage.setItem('cart', JSON.stringify(newCart));
                updateCart();
            });
        });
    };

    updateCart();
    window.updateCart = updateCart;
});
