from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    tg_id = models.IntegerField(null=False)
    username = models.CharField(max_length=100, null=True,blank=True)
    phone_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.phone_number