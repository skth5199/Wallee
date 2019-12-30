from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username','name', 'address', 'dob', 'phone', 'country','count')

class WalletAdmin(admin.ModelAdmin):
    list_display = ('amount','owner')


class ItemAdmin(admin.ModelAdmin):
    item_display = ('Name','Cost')

class CartAdmin(admin.ModelAdmin):
    cart_display = ('i1c','q1c','i2c','q2c','i3c','q3c','i4c','q4c','i5c','q5c','i6c','q6c')


class SavedcardsAdmin(admin.ModelAdmin):
    list_display = ('name','month','year','number','cvv','ownername','amount','password')

class BankaccountAdmin(admin.ModelAdmin):
    list_display = ('username','number','ifsc','password','amount')

class MovieBookAdmin(admin.ModelAdmin):
    mb_display = ('user','movie','date','seats','amount')

class MovieAdmin(admin.ModelAdmin):
    movie_display = ('name','cost')

class BusBookAdmin(admin.ModelAdmin):
    mb_display = ('user','bus','date','seats','amount')

class BusAdmin(admin.ModelAdmin):
    bus_display = ('name','cost','starting','dest')


class BillAdmin(admin.ModelAdmin):
    bill_display = ('amount','phone')

class PromoAdmin(admin.ModelAdmin):
    p_display = ('name','perc')


admin.site.register(profile, ProfileAdmin)
admin.site.register(wallet,WalletAdmin)
admin.site.register(item,ItemAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(savedcards, SavedcardsAdmin)
admin.site.register(bankaccount, BankaccountAdmin)
admin.site.register(TicketBook, MovieBookAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(TicketBookBus, BusBookAdmin)
admin.site.register(Bus, BusAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Promo, PromoAdmin)








'''


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
'''