import os
import datetime
from datetime import date

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from .serializers import CameraSerializer, FavoriteSerializer, ProfileSerializer, HistorySerializer
from backend.models import Camera, Favorites, Profile, History

from django.http import HttpResponse

from api.service.report_handler import report_handler, report_to_save, file_response
from api.service.mask_union import mask_union


class GetCameras(ListAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class GetFavorites(ListCreateAPIView):
    queryset = Favorites.objects.all()
    serializer_class = FavoriteSerializer


class SetFavorites(RetrieveUpdateDestroyAPIView):
    queryset = Favorites.objects.all()
    serializer_class = FavoriteSerializer


class ProfileDetails(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# class GetUser(APIView):
#     authentication_classes = [JSONWebTokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request, format=None):
#
#         photo = request.user.profile_set.get().photo if request.user.profile_set.get().photo else "/images/user.jpg"
#
#         result = {
#             "name": request.user.profile_set.get().name,
#             "surname": request.user.profile_set.get().surname,
#             "midname": request.user.profile_set.get().midname,
#             "photo": photo,
#             "email": request.user.profile_set.get().email,
#             "tel": request.user.profile_set.get().tel,
#         }
#         return Response(result)


class CreateReport(APIView):
    def post(self, request):
        now = date.today()
        name = now.strftime("%d-%m-%Y") + '-Report.docx'
        data=request.data
        doc = report_handler(data, History)
        doc.save(name)
        try:
            response = report_to_save(History, name)
        finally:
            os.remove(name)
        return response

    def get_report(self, id):
        file = History.objects.get(pk=id).file
        return file_response(file)


class ReportList(ListAPIView):
    serializer_class = HistorySerializer

    def get_queryset(self):
        now = date.today()
        date_before = self.request.query_params.get("date_before") if self.request.query_params.get(
            "date_before") else now.strftime("%Y-%m-%d")
        date_after = self.request.query_params.get("date_after") if self.request.query_params.get(
            "date_after") else (now - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
        return History.objects.filter(date__range=[date_after, date_before])

class MaskUnion(APIView):
    def get(self,request):
        response=""
        data=request.data
        response="data:image/jpeg;base64,"+mask_union(data)
        return HttpResponse(response)
