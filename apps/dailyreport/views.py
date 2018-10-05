import json
import re
from datetime import datetime, timedelta

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model

from system.mixin import LoginRequiredMixin
from .models import DailyReport
from .forms import DailyReportForm

User = get_user_model()


class MyReportView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        my_report_all = DailyReport.objects.filter(user=int(request.user.id))
        ret['my_report_all'] = my_report_all
        return render(request, 'dailyreport/myreport.html', ret)


class ReportCreateView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        category_all = [{'key': i[0], 'value': i[1]} for i in DailyReport.cat_choices]
        user_all = User.objects.exclude(username__in=['admin', request.user.username])
        ret['category_all'] = category_all
        ret['user_all'] = user_all
        if 'calDate' in request.GET and request.GET['calDate']:
            calDate = re.split('[-: ]', request.GET['calDate'])
            Y, M, D, h, m = map(int, calDate)
            start_time = datetime(Y, M, D, h, m)
            end_time = start_time + timedelta(hours=1)
            ret['start_time'] = start_time
            ret['end_time'] = end_time
        return render(request, 'dailyreport/report_create.html', ret)

    def post(self, request):
        res = dict(result=False)
        daily_report_form = DailyReportForm(request.POST)
        if daily_report_form.is_valid():
            daily_report_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')




