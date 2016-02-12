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
    img = models.ImageField(u"页面显示图片",help_text=u"确保图片裁剪至650x397,且分辨率为300",upload_to="statics/img/home/public_class/")

    def __unicode__(self):
        return self.title


class NewGraduates(models.Model):
    course_name = models.CharField(u"课程名称",max_length=64)
    semester = models.CharField(u"学期",max_length=32)
    graduate_date = models.DateField(u"毕业日期",default=timezone.now)
    average_salary = models.IntegerField(u"平均工资",help_text=u"写数字",default=10000)
    stu_num = models.IntegerField(u"班级人数",help_text=u"写数字",default=65)

    link = models.URLField(u"详细列表")
    img = models.ImageField(u"页面显示图片",help_text=u"确保图片裁剪至650x397,且分辨率为300",upload_to="statics/img/home//")

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