from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.response import SimpleTemplateResponse
# from django.utils import timezone
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
# from django.views.generic.simple import direct_to_template

from models import Apartment

class ApartmentListView(ListView):
  queryset = Apartment.objects.all()

class ApartmentDetailView(DetailView):
  model = Apartment
