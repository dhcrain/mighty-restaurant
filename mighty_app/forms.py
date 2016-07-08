from django import forms
from mighty_app.models import Order, MenuItem, OrderLine
from django.forms import formset_factory


class OrderLineForm(forms.ModelForm):
    class Meta:
        model = OrderLine
        fields = ['quantity', 'order_menu_item']


class OrderForm(forms.ModelForm):
    OrderLineFormSet = formset_factory(OrderLineForm, can_delete=True)
    order_items = OrderLineFormSet()
    # forms.ModelMultipleChoiceField(queryset=OrderLine.objects.all())

    class Meta:
        model = Order
        fields = ['customer_name', 'order_items', 'note', 'is_complete', 'is_paid']
