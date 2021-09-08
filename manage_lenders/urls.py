from django.urls import path
from .views import *

app_name = "manage_lenders"

urlpattern = [
    path("", ListLenders.as_view(), name="list_lenders"),
    path("", ListActiveLenders.as_view(), name="list_active_lenders"),
    path("", CreateLender.as_view(), name="create_lender"),
    path("", GetLender.as_view(), name="get_lender"),
    path("", UpdateLender.as_view(), name="update_lender"),
    path("", DeleteLender.as_view(), name="delete_lender"),
    path("", BulkCSVUpload.as_view(), name="bulk_csv_upload"),
    path("", BulkCSVDownload.as_view(), name="bulk_csv_download"),
]