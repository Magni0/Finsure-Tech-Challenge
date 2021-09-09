from django.http.response import HttpResponse, HttpResponseBadRequest
from rest_framework import generics
from rest_framework.views import APIView
from .models import Lender
from .serializers import LenderSerializer
from django.core.paginator import Paginator
from django.core import serializers
from json import dumps, loads


class ListLenders(APIView):

    """
    Returns a list of all Lenders split in groups
    of five for Pagination
    """

    def get(self, request, *args, **kwargs):
        page_num = request.GET.get('page', 1)

        # if querystring active=true list only active lenders
        if request.GET.get('active', False):
            lenders = Lender.objects.filter(active=True)
        else:
            lenders = Lender.objects.all()

        # split lenders into pages of 5
        lender_pages = Paginator(lenders, 5)
        
        # find the max amount of pages  
        pages = lender_pages.page_range[-1]
        
        # get lenders of specified page
        # use querystring: page={page number}
        try:
            page = lender_pages.page(page_num)
        except:
            return HttpResponseBadRequest()

        lender_objects = page.object_list

        lender_json = serializers.serialize('json', lender_objects)

        lender_list = []

        for lender in loads(lender_json):
            lender_list.append({
                'id': lender['pk'],
                'name': lender['fields']['name'],
                'code': lender['fields']['code'],
                'upfront_commission_rate': lender['fields']['upfront_commission_rate'],
                'trial_commission_rate': lender['fields']['trial_commission_rate'],
                'active': lender['fields']['active'],
            })

        lender_dict = {'pages': pages, 'lenders': lender_list}

        content = dumps(lender_dict)

        return HttpResponse(content, content_type='application/json')


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
