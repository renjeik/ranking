from UserManagement.dummyData import (
    getDummyCompanies,
)

from UserManagement.models import Company

class CustomerService:
    """Encapsulates User's actions"""

    def __init__(self):
        pass

    # For now, this function gets all companies.
    def getCompanies(self):

        # Check if the Company table is empty
        if not Company.objects.exists():
            companiesList = getDummyCompanies()

            for company in companiesList:
                Company.objects.create(
                    name=company['name'],
                    location=company['location'],
                    description=company['description']
                )
            print("Database was empty. Companies have been added.")

        companies = Company.objects.all()

        # Convert the queryset to a list of dictionaries
        companiesList = [
            {
                "name": company.name,
                "location": company.location,
                "description": company.description,
            }
            for company in companies
        ]
        return companiesList

    # For now, this function gets a company.
    def getCompany(self, searchedCompany):
        # Check if the Company table is empty
        if not Company.objects.exists():
            companiesList = getDummyCompanies()

            for company in companiesList:
                Company.objects.create(
                    name=company['name'],
                    location=company['location'],
                    description=company['description']
                )
            print("Database was empty. Companies have been added.")

        company = Company.objects.get(name=searchedCompany)

        # Format the company data into a dictionary
        companyData = {
            "name": company.name,
            "location": company.location,
            "description": company.description,
        }
        return companyData
