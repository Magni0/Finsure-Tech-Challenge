from rest_framework import serializers
from .models import Lender


class LenderSerializer(serializers.ModelSerializer):

    """Serializer for all fields of the Lender Model"""

    class Meta:
        model = Lender
        fields = "__all__"