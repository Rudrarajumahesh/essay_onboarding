from rest_framework import serializers
from .models import StudentProfile
import json

with open('dropdowns.json') as f:
    DROPDOWNS = json.load(f)

class StudentProfileSerializer(serializers.ModelSerializer):
    def validate_gender(self, value):
        if value not in DROPDOWNS['gender']:
            raise serializers.ValidationError("Invalid gender option.")
        return value

    def validate_citizenship(self, value):
        if value not in DROPDOWNS['citizenship']:
            raise serializers.ValidationError("Invalid citizenship option.")
        return value

    def validate_state(self, value):
        if value not in DROPDOWNS['state']:
            raise serializers.ValidationError("Invalid state option.")
        return value

    def validate_country(self, value):
        if value not in DROPDOWNS['country']:
            raise serializers.ValidationError("Invalid country option.")
        return value

    def validate_sibling_age(self, value):
        if value not in DROPDOWNS['sibling_age']:
            raise serializers.ValidationError("Invalid sibling_age option.")
        return value

    class Meta:
        model = StudentProfile
        fields = '__all__'

#
# class StudentProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentProfile
#         fields = '__all__'