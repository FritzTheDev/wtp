from django.db import models
from django.conf import settings

# Create your models here.
class Listing(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  listing_datetime = models.DateTimeField(auto_now_add=True)
  af_available = models.IntegerField()
  price_per_af = models.IntegerField
  water_district = models.CharField(max_length=50)
  def __str__(self):
    return (self.user.username + ' ' + str(self.listing_datetime)[:16])