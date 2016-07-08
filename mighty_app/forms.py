from django import forms
from mighty_app.models import Order, MenuItem

class OrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=MenuItem.objects.all())

    class Meta:
        model = Order
        fields = ['customer_name', 'items', 'note', 'complete', 'paid']
