from django.db import models

# Create your models here.
class Record(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email =models.CharField(max_length=100)
  phone = models.CharField(max_length=15)

  def __str__(self):
    return (f"{self.first_name} {self.last_name}")
  

class StreamerInfo(models.Model):
  name = models.CharField(max_length=50)
  twitter = models.CharField(max_length=100, blank=True)
  twitch = models.CharField(max_length=100, blank=True)
  youtube = models.CharField(max_length=100, blank=True)
  team = models.CharField(max_length=50)
  rank = models.CharField(max_length=50, default=0)
  
  def __str__(self):
    return (f"Streamer: {self.name}")