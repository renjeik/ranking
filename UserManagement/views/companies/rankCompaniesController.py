import traceback
import logging

from UserManagement.models import Company

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from drf_yasg.utils import swagger_auto_schema

from haystack import Pipeline, component
from haystack.components.retrievers import InMemoryBM25Retriever
from haystack.components.writers import DocumentWriter

from haystack.dataclasses import Document

from haystack.document_stores.in_memory import InMemoryDocumentStore

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
@swagger_auto_schema(
    method="POST", operation_description="Rank companies."
)
@api_view(["POST"])
def rankCompaniesController(request, **kwargs):
    if request.method == "POST":
        """
        Rank companies.
        @Endpoint: /api/companies/rank
        """
        try:
            searchTerm = request.POST.get('search_term')

            # Fetch all companies from MySQL
            companies_queryset = Company.objects.all()

            # Convert queryset to list of dictionaries
            documents = [
                # {"content": company.description, "metadata": {"name": company.name, "location": company.location}}
                Document(content=company.description, meta={"name": company.name, "location": company.location})
                for company in companies_queryset
            ]

            doc_store = InMemoryDocumentStore(embedding_similarity_function="cosine")
            doc_store.write_documents(documents)

            retriever = InMemoryBM25Retriever(document_store=doc_store, top_k=5)

            retrieval_pipeline = Pipeline()
            retrieval_pipeline.add_component("keyword_retriever", retriever)

            result = retrieval_pipeline.run({"keyword_retriever":{ "query": searchTerm, "top_k": 5}})

            # Prepare response
            response_data = []
            for doc in result['keyword_retriever']['documents']:
                doc_res = {
                    "content": doc.content,
                    "name": doc.meta.get('name', 'Unknown'),
                    "location": doc.meta.get('location', 'Unknown'),
                }
                response_data.append(doc_res)

            return Response(
                {"data": response_data}, status=status.HTTP_200_OK
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
