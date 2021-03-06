from django.http.response import HttpResponse, HttpResponseBadRequest
from rest_framework import generics
from rest_framework.views import APIView
from .models import Lender
from .serializers import LenderSerializer
from django.core.paginator import Paginator
from django.core import serializers
from json import dumps, loads
import csv


class ListLenders(APIView):

    """
    Returns a list of all Lenders split in groups
    of five for Pagination use query string active=true
    to only return active lenders
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

    def post(self, request, *args, **kwargs):
        csv_file = request.FILES['lenders']

        # checks that the file is csv
        if not csv_file.name.endswith(".csv"):
            return HttpResponseBadRequest()

        lenders = csv_file.readlines()
        lenders.pop(0)
        for lender in lenders:
            lender = str(lender)
            lender_list = lender.split(",")
            lender_record = Lender(
                name=lender_list[0],
                code=lender_list[1],
                upfront_commission_rate=lender_list[2],
                trial_commission_rate=lender_list[3],
                active=bool(lender_list[4])
            )
            lender_record.save()

        return HttpResponse(status=201)


class BulkCSVDownload(APIView):

    """
    Downloads all lenders in csv format to cilent 
    """

    def get(self, request, *args, **kwargs):
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="lenders.csv"'},
        )
        lenders = Lender.objects.all()

        writer = csv.writer(response)
        writer.writerow([
            'ID',
            'NAME',
            'CODE',
            'UPRONT COMMISSION RATE',
            'TRIAL COMMISSION RATE',
            'ACTIVE'
        ])

        lender_values = lenders.values_list(
            'id',
            'name',
            'code',
            'upfront_commission_rate',
            'trial_commission_rate',
            'active'
        )

        for lender in lender_values:
            writer.writerow(lender)

        return response
