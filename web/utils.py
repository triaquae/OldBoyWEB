#_*_coding:utf-8_*_
__author__ = 'Alex Li'
import random
import models
import datetime
import logging
logger = logging.getLogger(__name__)

def allowcate_consultant():
    u"""
    分配 客服
    :return:
    """
    match_dic ={
        0: 'monday',
        1: 'tuesday',
        2: 'wednesday',
        3: 'thursday',
        4: 'friday',
        5: 'saturday',
        6: 'sunday'
    }
    pick_one = None
    c_weekday = datetime.datetime.now().weekday()
    try:
        consultant_list = models.Consultants.objects.filter(**{match_dic[c_weekday]:True})
        if not consultant_list:
            raise Exception(u'当前客服列表为空.请注意!!!')
        pick_one = consultant_list[random.randrange(len(consultant_list))]
        if pick_one is not None:
            raise Exception(u'当前客服列表整形失败')
    except Exception as e:
        logger.warning(e.message)
    return pick_one