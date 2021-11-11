from rest_framework import fields, serializers

from .models import *


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = "__all__"


