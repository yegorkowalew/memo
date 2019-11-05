from .models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # username = serializers.ReadOnlyField(source='user.username')
    url = serializers.ReadOnlyField(source='get_absolute_url')
    email = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Profile
        fields = ['url', 'email', 'fullname', 'fullname_small', 'user_no']

