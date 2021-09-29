from django.urls import path
from .views import *

app_name = "manage_lenders"

urlpatterns = [
    path("lenders", ListCreateLender.as_view(), name="list_create_lender"),
    path("lenders/<int:pk>", GetUpdateDeleteLender.as_view(), name="get_update_delete_lender"),
    path("lenders/upload", BulkCSVUpload.as_view(), name="bulk_csv_upload"),
    path("lenders/download", BulkCSVDownload.as_view(), name="bulk_csv_download"),
]