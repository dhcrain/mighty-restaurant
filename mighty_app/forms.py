from django import forms
from mighty_app.models import Order, MenuItem, OrderLine


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'order_items', 'note', 'is_complete', 'is_paid']
    # http://stackoverflow.com/questions/2216974/django-modelform-for-many-to-many-fields
    # order_items = forms.ModelMultipleChoiceField(queryset=OrderLine.objects.all())

    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['order_items'] = [t.pk for t in kwargs['instance'].menuitem_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    # Overriding save allows us to process the value of 'toppings' field
    def save(self, commit=True):
        # Get the unsave Pizza instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m
        def save_m2m():
           old_save_m2m()
           # This is where we actually link the pizza with toppings
           instance.menuitem_set.clear()
           for item in self.cleaned_data['order_items']:
               instance.menuitem_set.add(item)
        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        if commit:
            instance.save()
            self.save_m2m()

        return instance

#
#
#
# class OrderLineForm(forms.ModelForm):
#     class Meta:
#         model = OrderLine
#         fields = ['quantity', 'order_menu_item', 'orderline_menu']
