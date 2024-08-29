from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views.companies import *

urlpatterns = [
    path("api/companies/", companiesController, name="companies"),
    path("api/companies/<str:name>", companyDetailController, name="companyDetail"),
    path("api/companies/add/", addCompanyController, name="addCompany"),
    path("api/companies/rank/", rankCompaniesController, name="rankCompanies"),
]
