from django.shortcuts import render

from web import models
# Create your views here.


def index(request):
    news_obj = models.NotificationLinks.objects.all()
    school_news = news_obj.filter(category__in=('good_news','school_news')).order_by("priority")[:5]
    new_classes = news_obj.filter(category="news_class").order_by("priority")[:5]
    stu_dairy = news_obj.filter(category="stu_dairy").order_by("priority")[:10]
    recent_public_classes = models.PublicClass.objects.all().order_by("start_date")[:4]
    recent_graduates = models.NewGraduates.objects.all().order_by("graduate_date")[:4]
    return render(request,'web/index.html',{"school_news":school_news,
                                            "new_classes": new_classes,
                                            "stu_dairy": stu_dairy,
                                            "recent_public_classes": recent_public_classes,
                                            "recent_graduates": recent_graduates
                                            })


def about_us(request):
    return render(request,'web/about_us.html')
def course_py_devops(request):
    return render(request,'web/course_py_devops.html')