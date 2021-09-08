from django.urls import path
from .views import *

app_name = "manage_lenders"

urlpatterns = [
    path("lenders/list", ListLenders.as_view(), name="list_lenders"),
    path("lenders/list/active", ListActiveLenders.as_view(), name="list_active_lenders"),
    path("lenders/create", CreateLender.as_view(), name="create_lender"),
    path("lenders/get/<int:pk>", GetLender.as_view(), name="get_lender"),
    path("lenders/update/<int:pk>", UpdateLender.as_view(), name="update_lender"),
    path("lenders/delete/<int:pk>", DeleteLender.as_view(), name="delete_lender"),
    path("lenders/upload", BulkCSVUpload.as_view(), name="bulk_csv_upload"),
    path("lenders/download", BulkCSVDownload.as_view(), name="bulk_csv_download"),
]