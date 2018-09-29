# @Time   : 2018/9/29 11:18
# @Author : RobbieHan
# @File   : forms.py

from django import forms
from .models import DailyReport


class DailyReportForm(forms.ModelForm):
    class Meta:
        model = DailyReport
        fields = '__all__'
