import logging
import json5
from requests.exceptions import HTTPError

from rest_framework import status

from django.shortcuts import render
from django.views import View

from UserManagement.services import RequestService

requestService = RequestService()

logger = logging.getLogger(__name__)


class Companies(View):
    def get(self, request, **kwargs):
        """
        Views all companies.
        @Endpoint: /companies
        """
        try:
            response = requestService.sendInternalRequest("companies", request)

            data = response.json()["data"]
            context = {"data": data, "active_nav": "companies", "title": "Companies"}
            return render(request, "companies.html", context)

        # HTTP Error for status codes 400-599
        except HTTPError as err:
            logger.error(str(err))
            statusCode = err.response.status_code
            responseBody = err.response.json()
            statusMessage = (
                responseBody["message"]
                if "message" in responseBody
                else err.response.reason
            )
            context = {"code": statusCode, "message": statusMessage}
            return render(request, "error.html", context)

        except Exception as err:
            logger.error(str(err))
            context = {"code": 500, "message": str(err)}
            return render(request, "error.html", context)


class Company(View):
    def get(self, request, name, **kwargs):
        """
        Views a company.
        @Endpoint: /companies/:name
        @PathParam: name (Name of the company to be fetched)
        """
        try:
            response = requestService.sendInternalRequest(
                "companyDetail", request, [name]
            )

            data = response.json()["data"]
            context = {"company": data, "active_nav": "companies"}
            return render(request, "company.html", context)

        # HTTP Error for status codes 400-599
        except HTTPError as err:
            logger.error(str(err))
            statusCode = err.response.status_code
            responseBody = err.response.json()
            statusMessage = (
                responseBody["message"]
                if "message" in responseBody
                else err.response.reason
            )
            context = {"code": statusCode, "message": statusMessage}
            return render(request, "error.html", context)

        except Exception as err:
            logger.error(str(err))
            context = {"code": 500, "message": str(err)}
            return render(request, "error.html", context)

class AddCompany(View):
    def get(self, request, **kwargs):
        """
        Views add company.
        @Endpoint: /companies/add
        """
        try:
            context = {"active_nav": "add_company"}
            return render(request, "addCompany.html", context)

        # HTTP Error for status codes 400-599
        except HTTPError as err:
            logger.error(str(err))
            statusCode = err.response.status_code
            responseBody = err.response.json()
            statusMessage = (
                responseBody["message"]
                if "message" in responseBody
                else err.response.reason
            )
            context = {"code": statusCode, "message": statusMessage}
            return render(request, "error.html", context)

        except Exception as err:
            logger.error(str(err))
            context = {"code": 500, "message": str(err)}
            return render(request, "error.html", context)

class RankCompanies(View):
    def post(self, request, **kwargs):
        """
        Views rank all companies.
        @Endpoint: /companies/rank
        """
        try:
            companies = json5.loads(request.POST.get('companies'))
            companiesList = companies.pop("data")

            context = {"data": companiesList, "active_nav": "companies", "title": "Ranked Companies"}
            return render(request, "companies.html", context)

        # HTTP Error for status codes 400-599
        except HTTPError as err:
            logger.error(str(err))
            statusCode = err.response.status_code
            responseBody = err.response.json()
            statusMessage = (
                responseBody["message"]
                if "message" in responseBody
                else err.response.reason
            )
            context = {"code": statusCode, "message": statusMessage}
            return render(request, "error.html", context)

        except Exception as err:
            logger.error(str(err))
            context = {"code": 500, "message": str(err)}
            return render(request, "error.html", context)