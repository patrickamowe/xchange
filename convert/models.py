from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    def __str__(self):
        return self.username

class Currency(models.Model):
    """
        represent a country currency

        id(AutoField): A unique value identify
        code (CharField): The three letter representation of a currency.
        name (CharField): The name of the currency.
        country (CharField): The country to which the currency belong to.
    """
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code}: {self.name}"


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name="wishlists")
    base_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="base_currency")
    quote_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="quote_currency")

    class Meta:
        unique_together = ('wishlist', 'base_currency', 'quote_currency')  # Ensure uniqueness of wishlist items

    def __str__(self):
        return f"{self.base_currency.code} : {self.base_currency.name} - {self.quote_currency.code} : {self.quote_currency.name}"