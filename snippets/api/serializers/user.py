from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.api.serializers.snippet import SnippetSerializer


class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.HyperlinkedIdentityField(many=True, view_name='snippet-detail', read_only=True)
    snippets = SnippetSerializer('snippets', many=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']