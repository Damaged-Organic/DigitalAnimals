from django.db import models


class Benefit(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    image = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Pricing(models.Model):
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Pricing'

    def __str__(self):
        return self.category


class Contact(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=19)

    def __str__(self):
        return self.email
