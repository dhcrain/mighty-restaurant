from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    COOK = 'Cook'
    SERVER = 'Server'
    OWNER = 'Owner'
    job_choices = ((COOK, 'Cook'), (SERVER, 'Server'), (OWNER, 'Owner'))
    user = models.OneToOneField('auth.User')
    job = models.CharField(max_length=10, choices=job_choices)

    def is_cook(self):
        return self.job is self.COOK

    def is_server(self):
        return self.job is self.SERVER

    def is_owner(self):
        return self.job is self.OWNER

    def __str__(self):
        return str(self.user)

class MenuItem(models.Model):
    created_by = models.ForeignKey('auth.User')
    title = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.title

class Order(models.Model):
    customer_name = models.CharField(max_length=20)
    items = models.ManyToManyField(MenuItem)
    note = models.TextField(blank=True)
    # total = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    complete = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    # http://stackoverflow.com/questions/27975251/how-do-i-add-together-fields-from-a-manytomanyfield-in-django
    def order_total(self):
        return self.items.aggregate(total=models.Sum('price'))['total']

    def __str__(self):
        return self.customer_name


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save, sender=Order)
# def create_order_total(**kwargs):
#     created = kwargs.get('created')
#     instance = kwargs.get('instance')
#     if created:
#         total = sum(Order.objects.get(id=instance).items.price)
#         Order.objects.create(total=total)
