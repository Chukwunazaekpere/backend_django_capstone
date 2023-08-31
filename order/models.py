from django.db import models
from django.contrib.auth.models import User
from menu.models import Menu


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, editable=False)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return str(self.user)



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    cart = models.OneToOneField(Cart, on_delete=models.RESTRICT)
    quantity = models.PositiveBigIntegerField()
    date_created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Order"
    
    def __str__(self):
        # print("\n\t Order-User: ", type(self.user))
        # user = User.objects.get(username=self.user)
        # print("\n\t User: ", user.username)
        return self.menu

