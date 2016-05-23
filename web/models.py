#_*_coding:utf8_*_

from django.db import models
from django.utils import timezone
# Create your models here.


class NotificationLinks(models.Model):
    title = models.CharField(u"标题",max_length=64,unique=True,help_text=u"填写标题")
    #title = models.CharField(max_length=64,unique=True,help_text=u'QQ号必须唯一')
    category_choices = (
        ('stu_dairy',u"学员日记"),
        ('good_news',u"喜报"),
        ('school_news',u"公告"),
        ('news_class',u"最新开班"),
        ('senior_dairy',u"师兄说"),
        ('net_class',u'网络学习中心'),
    )
    category= models.CharField(u"文章类型",max_length=32,choices=category_choices)
    link = models.URLField(u"文章链接")
    priority = models.IntegerField(u"权重",help_text=u"文章排名权重,值越小,排名越靠前",default=1000)
    class_open_date = models.DateField(u"开班日期",help_text=u"仅在文章类型为'最新开班'时才使用此项,选择开班日期",blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    hide = models.BooleanField(u"隐藏此文章",default=False)


    def __unicode__(self):
        return self.title


class PublicClass(models.Model):
    title = models.CharField(u"主题",max_length=128,unique=True,help_text=u"公开课主题...")
    start_date = models.DateTimeField(u"开课时间")
    teacher = models.CharField(u"讲师",max_length=32)
    link = models.URLField(u"报名链接")
    img = models.ImageField(u"页面显示图片",help_text=u"确保图片裁剪至650x397,且分辨率为300",upload_to="static/img/home/public_class/")

    def __unicode__(self):
        return self.title


class NewGraduates(models.Model):
    course_name = models.CharField(u"课程名称",max_length=64)
    semester = models.CharField(u"学期",max_length=32)
    graduate_date = models.DateField(u"毕业日期",default=timezone.now)
    average_salary = models.IntegerField(u"平均工资",help_text=u"写数字",default=10000)
    stu_num = models.IntegerField(u"班级人数",help_text=u"写数字",default=65)

    link = models.URLField(u"详细列表")
    img = models.ImageField(u"页面显示图片",help_text=u"确保图片裁剪至650x397,且分辨率为300",upload_to="static/img/home//")

    def __unicode__(self):
        return self.course_name


class Consultants(models.Model):
    qq = models.IntegerField(u"qq",unique=True)
    name = models.CharField(u"招生老师姓名",max_length=32)
    monday = models.BooleanField(u"周一",default=True)
    tuesday = models.BooleanField(u"周二",default=True)
    wednesday = models.BooleanField(u"周三",default=True)
    thursday = models.BooleanField(u"周四",default=True)
    friday = models.BooleanField(u"周五",default=True)
    saturday = models.BooleanField(u"周六",default=True)
    sunday = models.BooleanField(u"周日",default=True)

    def __unicode__(self):
        return self.name


class Offor(models.Model):
    name = models.CharField(u'学员名称',max_length=100)
    education_choices = (
        (1,u"小学"),
        (2,u"初中"),
        (3,u"高中"),
        (4,u"中专"),
        (5,u"大专"),
        (6,u"本科"),
        (7,u"硕士"),
        (8,u"博士"),
    )
    education = models.IntegerField(u'学历', default=6, choices=education_choices)
    course = models.CharField(u'课程', max_length=100)
    enterprise = models.CharField(u'工作单位', max_length=100)
    salary = models.IntegerField(u'薪水', default=10000)
    time = models.DateTimeField()


class ImageLink(models.Model):
    title = models.CharField(u'标题', max_length=200)
    link = models.URLField(u'链接', blank=True)
    priority = models.IntegerField(u"权重", help_text=u"链接排名权重,值越小,排名越靠前", default=1000)
    type_choices = (
        (1, u"首页轮播图"),
        (2, u"首页培训课程图"),
        (3, u"首页师资介绍图"),
        (4, u"首页网络学习中心"),
        (5, u"首页社区推荐"),
        (6, u'网络课程'),
    )
    type = models.IntegerField(u'类型', default=1,choices=type_choices)
    img = models.ImageField(u'图片', upload_to="static/img/home")
    notification = models.ManyToManyField(NotificationLinks, blank=True)

    class Meta:
        verbose_name = u'首页及课程中心链接'
        verbose_name_plural = u'首页及课程中心链接'

