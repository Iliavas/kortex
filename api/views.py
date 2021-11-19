from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from .serializers import CameraSerializer, FavoriteSerializer, ProfileSerializer
from backend.models import Camera, Favorites, Profile
from django.http import HttpResponse, FileResponse
import os


from .service import report_handler


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
        report_handler(request)
        with open("gen.docx", 'rb') as report:
            response = HttpResponse(FileResponse(report),
                                    content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=report.docx'
            os.remove("gen.docx")
            return response
