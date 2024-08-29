import traceback
import logging

from UserManagement.services import (
    CustomerService,
)

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create an instance of services
customerService = CustomerService()

# Create your views here.
@swagger_auto_schema(
    method="GET",
    operation_description="Lists all companies.",
)
@api_view(["GET"])
def companiesController(request, **kwargs):
    if request.method == "GET":
        """
        Lists all companies.
        @Endpoint: /api/companies
        """
        try:
            # Gets all companies
            userCompanies = customerService.getCompanies()
            return Response(
                {"success": True, "data": userCompanies}, status=status.HTTP_200_OK
            )

        except Exception as e:
            logger.error(traceback.format_exc())
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    else:
        return Response(
            {"success": False, "message": "HTTP method is invalid."},
            status=status.HTTP_400_BAD_REQUEST,
        )
