#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import random
import models
import datetime

def allowcate_consultant():
    match_dic ={
        0:'monday',
        1:'tuesday',
        2:'wednesday',
        3:'thursday',
        4:'friday',
        5:'saturday',
        6:'sunday'
    }
    c_weekday =datetime.datetime.now().weekday()
    consultant_list= models.Consultants.objects.filter(**{match_dic[c_weekday]:True})
    pick_one = consultant_list[random.randrange(len(consultant_list))]
    #print('pick consult:',pick_one)
    return pick_one