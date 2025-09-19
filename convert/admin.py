from django.contrib import admin
from convert.models import Currency, User, SavedConversion, RecentConversion

# Register your models here.

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'country')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password', 'profile_pic')

@admin.register(SavedConversion)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'base', 'quote')

@admin.register(RecentConversion)
class RecentConversionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'base', 'quote', 'timestamp')