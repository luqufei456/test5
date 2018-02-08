from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=10)
    upwd = models.CharField(max_length=50)
    idDelete = models.BooleanField(default=False)

class AreaInfo(models.Model):
    title = models.CharField(max_length=10)
    # django2.0 要加上on_delete=models.CASCADE,  ForeignKey  blank为True表示在页面表单上添加的时候可以不添加
    parea = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,)

class Test1(models.Model):
    hcontent = HTMLField()