from rest_framework import generics
from rest_framework.views import APIView
from .models import Lender
from .serializers import LenderSerializer

class ListLenders(APIView):

    """
    Returns a list of all Lenders split in groups
    of five for Pagination
    """

    pass

class ListActiveLenders(APIView):

    """
    Returns a list of all active Lenders split in groups
    of five for Pagination
    """

    pass

class CreateLender(generics.CreateAPIView):

    """Creates a single lender record"""

    queryset = Lender
    serializer_class = LenderSerializer

class GetLender(generics.RetrieveAPIView):
    
    """Returns a single lender record specified by record id"""
    
    queryset = Lender
    serializer_class = LenderSerializer

class UpdateLender(generics.UpdateAPIView):
    
    """
    Updates a single lender record specified by record id,
    a partial update is done with PATCH method and a 
    full update done with PUT method
    """

    queryset = Lender
    serializer_class = LenderSerializer

class DeleteLender(generics.DestroyAPIView):

    """Deletes a single lender record specified by record id"""

    queryset = Lender
    serializer_class = LenderSerializer

class BulkCSVUpload(APIView):

    """
    Creates an indefinite amount of new records by data
    provided in csv format 
    """

    pass

class BulkCSVDownload(APIView):

    """
    Downloads all lenders in csv format to cilent 
    """

    pass