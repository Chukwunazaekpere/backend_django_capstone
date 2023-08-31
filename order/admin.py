from typing import Any
from django.contrib import (
    admin, 
    messages
)
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.http.response import HttpResponse
# Register your models here.
from menu.models import Menu
from .models import (
    # Category,
    Cart,
    Order
)

class CartAdmin(admin.ModelAdmin):
    list_display = ["user"]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False


class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "menu", "quantity", "cart"]

    fieldsets = [
        ("Order-item Details", {
            "fields": ["menu", "quantity"]
        })
    ]

    def add_view(self, request: HttpRequest, form_url="", extra_context={}) -> HttpResponse:
        try:
            print("\n\t Cart-user: ", request.user)
            user = User.objects.get(username=request.user)
            # print("\n\t type(user)....", type(user))
            cart = Cart.objects.filter(user=user)
            print("\n\t Cart-cart: ", cart)
            if len(cart) == 0:
                # print("\n\t creating Cart....")
                new_cart = Cart()
                new_cart.user = user
                new_cart.save()
            return super().add_view(request, form_url, extra_context)
        except Exception as error:
            print("\n\t Error: ", error)
            return super().add_view(request, form_url, extra_context)
        

    def save_model(self, request: HttpRequest, obj: Any, form: Any, change: Any) -> None:
        print("\n\t Req-a: ", request.POST)
        print("\n\t Req-a-user: ", request.user)
        try:
            if not change:
                user = User.objects.get(username=request.user)
                cart = Cart.objects.get(user=user)
                menu = Menu.objects.get(pk=request.POST['menu'])
                print("\n\t Menu: ", menu)
                print("\n\t user: ", user)
                order_item = Order()
                order_item.user = user
                order_item.cart = cart
                order_item.menu = menu
                order_item.quantity = request.POST['quantity']
                order_item.save()
                return (request, obj, form, change)
        except Exception as error:
            # print("\n\t Error: ", error)
            messages.set_level(request, messages.ERROR)
            self.message_user(request, error, messages.ERROR)
            # return (self, request)


admin.site.register(Cart, CartAdmin)
# admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.site_header = "LittleLemon Admin"
admin.site.site_title = "LittleLemon Administration"
admin.site.index_title = "LittleLemon Administration"