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



class SavedConversion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    base = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="base")
    quote = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="quote")

    class Meta:
        unique_together = ('user', 'base', 'quote')  # Ensure 

    def __str__(self):
        return f"{self.base.code} : {self.base.name} - {self.quote.code} : {self.quote.name}"