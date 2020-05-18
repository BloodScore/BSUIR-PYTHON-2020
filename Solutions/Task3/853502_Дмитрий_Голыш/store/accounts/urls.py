from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update_user, name='update'),
    path('delete/', views.delete_user, name='delete'),
    path('shop/', views.shop, name='shop'),
    # path('product/', views.product_page, name='product'),
    path('product_info/<str:item>', views.product_page, name='product'),
    path('add_to_cart/<str:item>', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/<str:order_id>', views.checkout, name='checkout'),
    path('clr/<str:order_id>', views.clear_cart, name='clear_cart'),
    # path('related_models/', views.related_models, name='related_models'),
]
