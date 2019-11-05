from .models import History
from rest_framework import serializers

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    # username = serializers.ReadOnlyField(source='user.username')
    # email = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = History
        fields = ['icon', 'color', 'name', 'link', 'short_text', 'full_text', 'last_updated']

