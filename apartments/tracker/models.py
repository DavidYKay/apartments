from django.db import models

# Create your models here.

# from django import forms
# from django.contrib.localflavor.fr.forms import FRPhoneNumberField

class ProCon(models.Model):
  name = models.CharField(max_length=30)

  class Meta:
    abstract = True

  def __unicode__(self):
    return self.name

class Pro(ProCon):
  pass

class Con(ProCon):
  pass

class Apartment(models.Model):
   name = models.CharField(max_length=30)
   photo = models.URLField(blank=True)

   date_added = models.DateField(auto_now_add=True)
   date_viewed = models.DateField(blank=True)

   bedrooms = models.PositiveSmallIntegerField()
   bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
   sqft = models.PositiveIntegerField()
   notes = models.TextField(blank=True)

   rent = models.PositiveIntegerField()
   broker_multiplier = models.DecimalField(default=0, max_digits=3, decimal_places=2)
   broker_fee        = models.PositiveIntegerField(default=0)
   security_multiplier = models.DecimalField(default=0, max_digits=3, decimal_places=2)
   security_fee        = models.PositiveIntegerField(default=0)

   address = models.CharField(max_length=140)
   zip_code = models.CharField(max_length=15)

   latitude  = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=9)
   longitude = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=9)

   pros = models.ManyToManyField(Pro, blank=True)
   cons = models.ManyToManyField(Con, blank=True)

   def sqft_string(self):
     return "%d sqft" % self.sqft

   def broker_amount(self):
     return self.broker_fee + (self.broker_multiplier * self.rent)

   def security_amount(self):
     return self.security_fee + (self.security_multiplier * self.rent)

   def __unicode__(self):
     return self.name
