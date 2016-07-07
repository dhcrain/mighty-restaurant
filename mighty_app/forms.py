from django import forms
from mighty_app.models import Order, MenuItem

# Create the form class.
class OrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=MenuItem.objects.all())

    class Meta:
        model = Order
        fields = ['customer_name', 'items', 'note']


# class YourModelForm(forms.ModelForm):
#     items = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
#             queryset = YourCategory.objects.all())#here you can filter for what choices you need
#
# class YourModelAdmin(admin.ModelAdmin):
#     form = YourModelForm
