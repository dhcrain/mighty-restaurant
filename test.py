from django.db import models
from django.core.urlresolvers import reverse


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=200)
    product_price = models.IntegerField(max_length=4)

    def __unicode__(self):
        return self.product_name

    class Meta:
        ordering = ('product_name',)


class Quote(models.Model):
    quotee_name = models.CharField("Name", max_length=40)
    quotee_email = models.EmailField("Email")
    quotee_phone = models.IntegerField("Phone", max_length=10)
    quotee_products = models.ManyToManyField(Product, verbose_name="Products")
    quotee_total = models.IntegerField("Estimate", max_length=10, null=True, blank=True)

    def quotee_total(self):
        return self.quotee_products.aggregate(total=models.Sum('product_price'))['total']
        
    def __unicode__(self):
        return self.quotee_email

    class Meta:
        ordering = ('quotee_email',)

    def get_absolute_url(self):
        return reverse('quote-detail', kwargs={'pk': self.pk, })
