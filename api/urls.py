from django.urls import path
from .views import GetCameras, GetFavorites, SetFavorites, ProfileDetails, CreateReport,ReportList,MaskUnion

urlpatterns = [
    path("camera", GetCameras.as_view()),
    path("favorite/", GetFavorites.as_view()),
    path("favorite/<pk>", SetFavorites.as_view()),
    path("profile_details/<pk>", ProfileDetails.as_view()),
    path("create_report",CreateReport.as_view()),
    path("download_report/<id>", CreateReport.get_report),
    path("show_reports", ReportList.as_view()),
    path("union_image", MaskUnion.as_view()),


]
