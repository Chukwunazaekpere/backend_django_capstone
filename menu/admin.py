from typing import Any
from django.contrib import (
    admin, 
    messages
)
from django.contrib.auth.models import User
# Register your models here.
from .models import (
    Booking,
    Category,
    Menu
)

class BookingAdmin(admin.ModelAdmin):
    list_display = ['fullname']



class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_by", "date_created"]

    fieldsets = [
        ("Category Details", {
            "fields": ["name"]
        })
    ]

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        print("\n\t Req: ", request.POST['name'])
        if not change:
            user = User.objects.get(username=request.user)
            self.created_by = user.pk
            category = Category()
            category.created_by = user
            category.name = request.POST['name']
            category.save()
        return self

class MenuAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price", "image", "description", "date_created", "created_by"]

    fieldsets = [
        ("Menu-item Details", {
            "fields": ["category", "name", "price", "description", "image"]
        })
    ]

    def save_model(self, request: Any, form:Any, obj: Any, change: Any) -> None:
        print("\n\t Req-a: ", request.POST)
        try:
            if not change:
                user = User.objects.get(username=request.user)
                category = Category.objects.get(pk=request.POST['category'])
                self.created_by = user.pk
                price = request.POST['price']
                # print("\n\t Price: ", price)
                if "-" in price:
                    raise ValueError("Price must be greater than zero")
                menu_item = Menu()
                menu_item.created_by = user
                menu_item.category = category
                menu_item.name = request.POST['name']
                menu_item.price = price
                menu_item.description = request.POST['description']
                # menu_item.image = request.POST['image']
                menu_item.save()
                return self
        except Exception as error:
            # print("\n\t Error: ", error)
            messages.set_level(request, messages.ERROR)
            self.message_user(request, error, messages.ERROR)
            # return (self, request)


admin.site.register(Booking, BookingAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
