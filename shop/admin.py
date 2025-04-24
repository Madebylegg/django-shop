from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Category, Collection, Product,
    Order, OrderItem, CartItem,
    Address, Payment, Review
)

# CATEGORY
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

# COLLECTION
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    filter_horizontal = ('products',)

# PRODUCT
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'price', 'available', 'stock')
    list_filter = ('available', 'category')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')

# ORDERITEM INLINE
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('price', 'quantity', 'total_price')

# ORDER
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'is_paid', 'created')
    list_filter = ('status', 'is_paid', 'created')
    search_fields = ('user__username', 'paypal_order_id')
    inlines = (OrderItemInline,)

# CART ITEM
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'session_key', 'quantity', 'added')
    list_filter = ('added',)
    search_fields = ('product__name', 'user__username', 'session_key')

# ADDRESS
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'line1', 'city', 'country')
    search_fields = ('user__username', 'line1', 'city', 'country')

# PAYMENT
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'transaction_id', 'status', 'amount', 'created')
    list_filter = ('status', 'created')
    search_fields = ('transaction_id', 'order__id')

# REVIEW
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created')
    list_filter = ('rating', 'created')
    search_fields = ('product__name', 'user__username', 'comment')
