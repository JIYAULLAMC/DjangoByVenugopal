from rest_framework import serializers
from clothapp.models import Cloth

class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = "__all__"