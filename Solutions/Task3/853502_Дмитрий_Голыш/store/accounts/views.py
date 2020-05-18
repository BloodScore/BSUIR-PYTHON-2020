from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateCustomUserForm, ChangeCustomUserForm, CustomUserInfoForm, OrderToUserForm
from .models import Product, Order, OrderItem, Transaction, CustomUser


def index(request):
    return render(request, 'accounts/index.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect!')

    return render(request, 'accounts/login.html')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CreateCustomUserForm()

    if request.method == 'POST':
        form = CreateCustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was successfully created for {username}')

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('home')

    form = CustomUserInfoForm(instance=request.user)
    context = {'form': form}

    return render(request, 'accounts/profile.html', context)


def update_user(request):
    if not request.user.is_authenticated:
        return redirect('home')

    form = ChangeCustomUserForm(instance=request.user)

    if request.method == 'POST':
        form = ChangeCustomUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'accounts/update_user.html', context)


def delete_user(request):
    if not request.user.is_authenticated:
        return redirect('home')

    user = request.user

    if request.method == 'POST':
        user.delete()
        return redirect('home')

    return render(request, 'accounts/delete_user.html')


def product_page(request, item):
    prod = Product.objects.get(id=item)
    context = {'prod': prod}

    return render(request, 'accounts/single-product.html', context)


def shop(request):
    items = Product.objects.all()
    context = {'items': items}

    return render(request, 'accounts/shop.html', context)


def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(CustomUser, username=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


def add_to_cart(request, item):
    product = Product.objects.get(id=item)

    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(owner=request.user)
    user_order.items.add(order_item)

    return redirect('shop')

# def delete_from_cart(request, item):
#     item_to_delete = OrderItem.objects.get(id=item)
#     item_to_delete.delete()


def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')

    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }

    return render(request, 'accounts/cart.html', context)


def clear_cart(request, order_id):
    order = Order.objects.get(id=order_id)
    items = order.get_cart_items()

    for i in items:
        i.delete()

    return redirect('home')


def checkout(request, order_id):
    order = Order.objects.get(owner=order_id)
    context = {'order': order}

    return render(request, 'accounts/checkout.html', context)


# def related_models(request):
#     form = OrderToUserForm()
#     context = {'form': form}
#
#     return render(request, 'accounts/related_models.html', context)
