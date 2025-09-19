from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """
    represent a user in the system
    Inherits from AbstractUser to utilize Django's built-in user management features.
    username (CharField): The username of the user.
    email (EmailField): The email address of the user.
    password (CharField): The password of the user.
    profile_pic (ImageField): The profile picture of the user.
    first_name (CharField): The first name of the user.
    last_name (CharField): The last name of the user.
    """

    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username

class Currency(models.Model):
    """
        represent a country currency

        code (CharField): The three letter representation of a currency.
        name (CharField): The name of the currency.
        country (CharField): The country to which the currency belong to.
    """
    
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code}: {self.name}"



class SavedConversion(models.Model):
    """
        represent a saved conversion by a user

        user (ForeignKey): The user who saved the conversion.
        base (ForeignKey): The base currency in the conversion.
        quote (ForeignKey): The quote currency in the conversion.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    base = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="base")
    quote = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="quote")

    class Meta:
        unique_together = ('user', 'base', 'quote')  # Ensure uniqueness

    def __str__(self):
        return f"{self.base.code} : {self.base.name} - {self.quote.code} : {self.quote.name}"


class RecentConversion(models.Model):
    """
        represent a recent conversion by a user

        user (ForeignKey): The user who made the conversion.
        base (ForeignKey): The base currency in the conversion.
        quote (ForeignKey): The quote currency in the conversion.
        timestamp (DateTimeField): The time when the conversion was made.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recent_user")
    base = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="recent_base")
    quote = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="recent_quote")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']  # Order by most recent first
        unique_together = ('user', 'base', 'quote')  # Ensure uniqueness

    def __str__(self):
        return f"{self.base.code} : {self.base.name} - {self.quote.code} : {self.quote.name} at {self.timestamp}"
    