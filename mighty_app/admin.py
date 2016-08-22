from django.contrib import admin
from mighty_app.models import Profile, MenuItem, Order, OrderLine
# Register your models here.

admin.site.register(Profile)
admin.site.register(OrderLine)
admin.site.register(MenuItem)


# https://docs.djangoproject.com/en/1.9/ref/contrib/admin/#working-with-many-to-many-intermediary-models
class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineInline,)

admin.site.register(Order, OrderAdmin)
