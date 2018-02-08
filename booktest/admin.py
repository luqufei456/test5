from django.contrib import admin
from .models import *
# Register your models here.
#@admin.register(UserInfo)
#class UserInfoAdmin(admin.ModelAdmin):
    #list_display = ['id', 'uname']

# 注册的两种方式 装饰器是第二种
#admin.site.register(UserInfo, UserInfoAdmin)

admin.site.register(Test1)