from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import os
from django.conf import settings
from .models import *
from django.core.paginator import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.
def index(request):
    return render(request, 'booktest/index.html')

def myExp(request):
    #a1 = int('abc') 设置一个出错 看看会输出什么
    return HttpResponse('hello')

def uploadPic(request):
    return render(request, 'booktest/uploadPic.html')

def uploadHandle(request):
    pic1 = request.FILES['pic1']
    picName = os.path.join(settings.MEDIA_ROOT, pic1.name)
    # 这里打开方式使用wb  用w会报错 不能使用字节写入
    with open(picName, 'wb') as pic:
        for c in pic1.chunks():
            pic.write(c)
    return HttpResponse(picName)

# 进行分页练习
def userlist(request,pindex):
    if pindex == '':
        pindex = 1
    list = UserInfo.objects.all()
    paginator = Paginator(list, 3)
    page = paginator.page(int(pindex))
    context = {'page': page}
    return render(request, 'booktest/userlist.html', context)

#省市区选择
def area(request):
    return render(request, 'booktest/area.html')

def area2(request, id):
    id1 = int(id)
    if id1==0:
        # values()  将数据转成字典
        data = AreaInfo.objects.filter(parea__isnull=True)
    else:
        data=[{}]
    # data1 = {'data': data}  这种方法不能转 自己遍历
    list = []
    #[[1,'北京'], [2,'上海']]  设计构造想要的数据列表
    for area in data:
        list.append([area.id, area.title])
    return JsonResponse({'data': list})

# 这个视图可以重复使用
def city(request, id):
    # parea__id 和 parea_id 的区别是  两个下划线代表关联 得到父级对象的parea_id  而一个下划线代表自己的parea_id属性
    # parea_id 这个属性是自动生成的 可以自己去数据库里查看表结构 表结构根据 models定义生成
    citylist = AreaInfo.objects.filter(parea_id=id)
    list = []
    # 构建第二种格式 [{id:1, title:'北京'}, {id:2, title:'上海'}...]
    for item in citylist:
        list.append({'id': item.id, 'title': item.title})
    return JsonResponse({'data': list})

#自定义编辑器
def htmlEditor(request):
    return render(request, 'booktest/htmlEditor.html')

def htmlEditorHandle(request):
    html = request.POST['hcontent']
    # 修改操作
    #test1 = Test1.objects.get(pk=1)
    #test1.hcontent = html
    #test1.save()

    # 添加操作
    test1 = Test1()
    test1.hcontent = html
    test1.save()
    context = {'hcontent': html}
    return render(request, 'booktest/htmlShow.html', context)

# 缓存  过期时间 60s  X 15  15分钟  也可以直接写900
#@cache_page(60 * 15)
def cache1(request):
    #return HttpResponse('hello chunjue')
    #cache.set('key1', 'value1', 600)  向cache中手动缓存
    #print(cache.get('key1'))
    #cache.clear() 清空缓存
    #return render(request, 'booktest/cache1.html')
    return HttpResponse('lalala')

# 全文检索+中文分词
def mysearch(request):
    return render(request, 'booktest/mysearch.html')

#用django1.7.6创建的工程，在想数据库mysql同步表格时，出现问题;django.db.utils.OperationalError: (1050, "Table 'devtypeinfo' already exists;

#环境：创建完项目之后，已经同步了一次，后来又需要添加表格，又在models.py中加入了一个class类，进行同步时(./manage.py makemigrations 没有错误信息，执行,.manage.py migrate时出现错误)

#解决方法：

                  #用./manage.py migrate myapp 命令同步；

 # Running migrations: No migrations to apply.
 # 解决方案 删掉数据库中的  django_migrations表