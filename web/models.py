#_*_coding:utf8_*_

from django.db import models

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

