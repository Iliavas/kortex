from rest_framework.serializers import ModelSerializer
from backend.models import Position, Camera, Favorites, Profile, History
from django.contrib.auth.models import User


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = ["longitude", "latitude"]


class CameraSerializer(ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = Camera
        fields = ["image", "position", "id", "name"]


class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favorites
        fields = ["name", "camera", "id"]


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "name", "surname", "midname", "photo", "email", "tel"]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
            'profile_set': {'read_only': True}
        }


class HistorySerializer(ModelSerializer):
    class Meta:
        model = History
        fields = ["file","date","id"]
