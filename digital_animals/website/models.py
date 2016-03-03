from django.db import models

class Benefit(models.Model):
    title = models.CharField(max_length=100)
    text  = models.CharField(max_length=500)
    icon  = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length=100)
    text  = models.CharField(max_length=200)
    image = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=100)
    icon  = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Pricing(models.Model):
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.category

    @property
    def price(self):
        return "%s ₴" % self.price

class Contact(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.IntegerField(max_length=12)

    # Move this to twig filter
    @property
    def phone(self):

        international = self.phone[0:3]
        local = self.phone[3:5]
        number = (self.phone[5:8], self.phone[8:10], self.phone[10:12])

        pattern = "+{international} ({local}) {number_I}-{number_II}-{number_III}"

        return pattern.format(
            international = international,
            local = local,
            number_I = number.0,
            number_II = number.1,
            number_III = number.2
        )
