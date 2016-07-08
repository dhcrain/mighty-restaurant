from django import forms
from mighty_app.models import Order, MenuItem, OrderLine



class OrderLineForm(forms.ModelForm):
    class Meta:
        model = OrderLine
        fields = ['quantity', 'order_menu_item', 'orderline_menu']


class OrderForm(forms.ModelForm):
    # order_items = forms.ModelMultipleChoiceField(queryset=OrderLine.objects.all())

    class Meta:
        model = Order
        fields = ['customer_name', 'order_items', 'note', 'is_complete', 'is_paid']
