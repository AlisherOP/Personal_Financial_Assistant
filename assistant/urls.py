from django.urls import path
from . import views
urlpatterns = [
    path("list/", views.expense_list, name="expense_list"),
    path("dashboard/", views.dashboard, name= "dashboard"),
    path("upload/", views.upload_receipt, name="upload_receipt"),
]
