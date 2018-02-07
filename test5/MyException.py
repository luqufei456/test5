from django.http import HttpResponse
from  django.utils import deprecation

# 2.0.2中需要设置继承 from  django.utils import deprecation 不然报错
class MyException(deprecation.MiddlewareMixin):
    def process_exception(request,response, exception):
        # 这里exception不能按课件上写 exception.message  可见做了一些改动
        return HttpResponse(exception)