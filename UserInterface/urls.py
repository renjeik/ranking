from django.urls import path

from .views.companies import Companies, Company, AddCompany, RankCompanies

urlpatterns = [
    path("companies", Companies.as_view(), name="companiesView"),
    path("companies/<str:name>/", Company.as_view(), name="companyDetailView"),
    path("companies/add", AddCompany.as_view(), name="addCompanyView"),
    path("companies/rank", RankCompanies.as_view(), name="rankCompaniesView"),
]
