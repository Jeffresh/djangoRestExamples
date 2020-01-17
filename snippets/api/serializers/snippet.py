from rest_framework import serializers
from snippets.models.snippet import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']
