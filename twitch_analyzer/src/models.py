from django.db import models
from django.db.models.fields import AutoField
from django.utils import timezone

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

# Create your models here.
class Game(models.Model):
    name = models.CharField(blank=False, null=False, max_length=120)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = AutoDateTimeField(default=timezone.now)

