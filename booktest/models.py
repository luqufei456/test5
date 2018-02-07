from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=10)
    upwd = models.CharField(max_length=50)
    idDelete = models.BooleanField(default=False)

class AreaInfo(models.Model):
    title = models.CharField(max_length=10)
    # django2.0 要加上on_delete=models.CASCADE,  ForeignKey
    parea = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,)