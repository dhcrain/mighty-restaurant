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
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.title

class Order(models.Model):
    customer_name = models.CharField(max_length=20)
    items = models.ManyToManyField(MenuItem)
    note = models.TextField()
    total = models.DecimalField(max_digits=4, decimal_places=2)
    complete = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get("created")
    instance = kwargs.get("instance")
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save, sender='auth.User')
# def create_token(**kwargs):
#     created = kwargs.get('created')
#     instance = kwargs.get('instance')
#     if created:
#         Token.objects.create(user=instance)
