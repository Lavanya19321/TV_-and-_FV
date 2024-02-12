from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse

# Create your views here.
class templatehtml(TemplateView):
    template_name='directhtml.html'


class BEtoFEbyTV(TemplateView):
    template_name='BEtoFEbyTV.html'
    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['NAME']='LAVANYA'
        ECDO['AGE']=3
        return ECDO
    
class insertschoolbyTV(TemplateView):
    template_name='insertschoolbyTV.html'
    def get_contex_data(self,**kwargs):
        ECDO=super().get_contex_data(**kwargs)
        ECDO['SFO']=SchoolForm
        return ECDO
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insertschoolbyTV is done successfully')


class  insertschoolbyFV(FormView):
    template_name='insertschoolbyFV.html'
    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('InsertSchoolByFV is done')


