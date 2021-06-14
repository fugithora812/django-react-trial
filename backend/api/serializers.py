from rest_framework import serializers
from react_app.models import User_Models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Models
        fields = ('user_id', 'user_name', 'user_age', 'user_email')
