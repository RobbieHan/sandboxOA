from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class DailyReport(models.Model):
    cat_choices = (('0', '工作报告'), ('1', '项目记录'), ('2', '日程安排'))
    category = models.CharField(max_length=20, choices=cat_choices, default='0')
    content = models.TextField(verbose_name='工作日报')
    user = models.ForeignKey(User, related_name='report_user', on_delete=models.DO_NOTHING, default='')
    attention = models.ManyToManyField(User, related_name='attention', blank=True)
    start_time = models.DateTimeField(default='', verbose_name='开始时间')
    end_time = models.DateTimeField(default='', verbose_name='结束时间')
    add_time = models.DateField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = '工作日报'
        verbose_name_plural = verbose_name
