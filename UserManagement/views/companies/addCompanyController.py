import traceback
import logging

from UserManagement.models import Company

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
@swagger_auto_schema(
    method="POST", operation_description="Add a company."
)
@api_view(["POST"])
def addCompanyController(request, **kwargs):
    if request.method == "POST":
        """
        Adds a company.
        @Endpoint: /api/companies/add
        """
        try:
            name = request.POST.get('name')
            location = request.POST.get('location')
            description = request.POST.get('description')

            # Adds a company
            if not Company.objects.filter(name=name).exists():
                company = Company.objects.create(
                    name=name,
                    location=location,
                    description=description
                )

            return Response(
                {"success": True}, status=status.HTTP_200_OK
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
