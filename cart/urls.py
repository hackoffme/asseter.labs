from django.urls import path
from cart import view_rest

urlpatterns = [
    path('cart/', view_rest.Cart.as_view()),
    path('cart/admin/', view_rest.CartsOfAllUsers.as_view()),

]
