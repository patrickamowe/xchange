from django.contrib import admin
from convert.models import Currency, User, Wishlist, WishlistItem

# Register your models here.

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'country')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password')

@admin.register(Wishlist)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

@admin.register(WishlistItem)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'wishlist', 'base_currency', 'quote_currency')