from rest_framework import serializers
from app.models import EmployeeListing



class EmployeeListingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.CharField(allow_blank=True, required=False)
    class Meta:
        model = EmployeeListing
        fields = ['id', 'applicant_name','applicant_email','applicant_phone','position_applying_for','date_applying','post_resume_or_cover','user']
        def validate_user(self, value):

            if value and len(value) > 0:
                raise serializers.ValidationError('Error')
                return value

    def create(self, validated_data):
        if "user" in validated_data:
            del validated_data["user"]
        return EmployeeListing.objects.create(**validated_data)
