from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProdutcList.as_view(), name='list'),
    path('<slug>', views.ProdutcDetail.as_view(), name='detail'),
    path('addtocart/', views.AddToCart.as_view(), name='addToCart'),
    path('removefromcart/', views.RemoveFromCart.as_view(), name='removeFromCart'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('finish/', views.Finish.as_view(), name='finish'),
]
