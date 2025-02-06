from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    tg_id = models.CharField(null=False,max_length=30)
    token = models.CharField(max_length=100, null=False,blank=False)
    real_name = models.CharField(max_length=100, null=True, blank=True,default=None)
    role = models.CharField(max_length=100,default='User')
    phone_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.phone_number