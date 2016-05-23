from django.shortcuts import render

from web import models
import utils


# Create your views here.


def index(request):
    news_obj = models.NotificationLinks.objects.all()
    school_news = news_obj.filter(category__in=('good_news', 'school_news')).order_by("priority")[:5]
    new_classes = news_obj.filter(category="news_class").order_by("priority")[:5]
    stu_dairy = news_obj.filter(category="stu_dairy").order_by("priority")[:10]
    net_clases = news_obj.filter(category="net_class").order_by("priority")[:10]
    senior_dairy = news_obj.filter(category="senior_dairy").order_by("priority")[:10]
    recent_public_classes = models.PublicClass.objects.all().order_by("start_date")[:4]
    recent_graduates = models.NewGraduates.objects.all().order_by("graduate_date")[:4]
    offors = models.Offor.objects.all().order_by('-time')[:10]

    img_banner = models.ImageLink.objects.filter(type=1).order_by("priority")[0:4]
    img_class = models.ImageLink.objects.filter(type=2).order_by("priority")[0:3]
    img_teacher = models.ImageLink.objects.filter(type=3).order_by("priority")[0:3]
    img_netclass = models.ImageLink.objects.filter(type=4).order_by("priority")[0:3]
    img_student = models.ImageLink.objects.filter(type=5).order_by("priority")[0:3]

    pick_one_consultant = utils.allowcate_consultant()
    return render(request, 'web/index.html', {"school_news": school_news,
                                              "new_classes": new_classes,
                                              "stu_dairy": stu_dairy,
                                              "recent_public_classes": recent_public_classes,
                                              "recent_graduates": recent_graduates,
                                              "consultant": pick_one_consultant,
                                              "senior_dairys": senior_dairy,
                                              "net_clases": net_clases,
                                              "offors": offors,
                                              "img_banner": img_banner,
                                              "img_class": img_class,
                                              "img_netclass": img_netclass,
                                              "img_teacher": img_teacher,
                                              "img_student": img_student,
                                              })


def about_us(request):
    return render(request, 'web/about_us.html')


def teachers(request):
    return render(request, 'web/teachers.html')


def course(request):
    net_courses = models.ImageLink.objects.filter(type=6).order_by("priority")[0:2]
    return render(request, 'web/course.html', {"net_courses": net_courses})


def jobs(request):
    return render(request, 'web/jobs.html')


def course_linux_ops(request):
    return render(request, 'web/course_linux_ops.html', {"consultant": utils.allowcate_consultant()})


def course_linux_architect(request):
    pick_one_consultant = utils.allowcate_consultant()

    return render(request, "web/course_linux_architect.html", {"consultant": pick_one_consultant})


def course_py_devops(request):
    return render(request, 'web/course_py_devops.html', {"consultant": utils.allowcate_consultant()})


def course_py_ops(request):
    return render(request, 'web/course_py_ops.html', {"consultant": utils.allowcate_consultant()})


def course_bigdata(request):
    return render(request, 'web/course_bigdata.html', {"consultant": utils.allowcate_consultant()})


def course_linux_senior(request):
    return render(request, 'web/course_linux_senior.html', {"consultant": utils.allowcate_consultant()})


def how_to_enroll(request):
    return render(request, 'web/how_to_enroll.html')


def enroll_pages(request, page_name):
    return render(request, 'web/enrollment/%s.html' % page_name)
