class Pizza(models.Model):
    name = models.CharField(max_length=50)

class Topping(models.Model):
    name = models.CharField(max_length=50)
    ison = models.ManyToManyField(Pizza, blank=True)


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza

    # Representing the many to many related field in Pizza
    toppings = forms.ModelMultipleChoiceField(queryset=Topping.objects.all())

    # Overriding __init__ here allows us to provide initial
    # data for 'toppings' field
    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['toppings'] = [t.pk for t in kwargs['instance'].topping_set.all()]

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
           instance.topping_set.clear()
           for topping in self.cleaned_data['toppings']:
               instance.topping_set.add(topping)
        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        if commit:
            instance.save()
            self.save_m2m()

        return instance
