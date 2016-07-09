from django.contrib import admin
from mighty_app.models import Profile, MenuItem, Order, OrderLine
# Register your models here.

admin.site.register(Profile)
admin.site.register(OrderLine)


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 1

class MenuItemAdmin(admin.ModelAdmin):
    inlines = (OrderLineInline,)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineInline,)

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Order, OrderAdmin)
