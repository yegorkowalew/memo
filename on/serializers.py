# from .models import History
from rest_framework import serializers

class GraphSerializer(serializers.HyperlinkedModelSerializer):
    # username = serializers.ReadOnlyField(source='user.username')
    # email = serializers.ReadOnlyField(source='user.email')
    class Meta:
        pass
        # model = History
        # fields = ['icon', 'color', 'name', 'link', 'short_text', 'full_text', 'last_updated']

