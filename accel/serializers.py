from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'nickname', 'email', 'phone_number', 'dob', 'gdpr_consent']
