from rest_framework import serializers
from .models import PreApplicationForm


class PreApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreApplicationForm
        fields = "__all__"
