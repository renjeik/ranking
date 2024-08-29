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
    method="GET", operation_description="Retrieves a company using its name."
)
@api_view(["GET"])
def companyDetailController(request, name, **kwargs):
    if request.method == "GET":
        """
        Gets a company.
        @Endpoint: /api/companies/:name
        @PathParam: name (name of the company to be fetched)
        """
        try:
            # Gets a company
            userCompany = customerService.getCompany(name)
            return Response(
                {"success": True, "data": userCompany}, status=status.HTTP_200_OK
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
