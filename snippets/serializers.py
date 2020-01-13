from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         Create and return a new 'Snippet' instance, given the validated data.
#         :param validated_data:
#         :return:
#         """
#
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing 'Snippet' instance, given the validate data.
#         :param instance:
#         :param validated_data:
#         :return:
#         """
#
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style - validated_data.get('style', instance.style)
#         instance.save()
#
#         return instance

# refactoring using modelserializer

# class SnippetSerializer(serializers.ModelSerializer):
#     # now that snippet are associated with the user that created them, let's update our SnippetSerializer
#     # to reflect that.
#
#     # source  argument controls which attribute is used to populate a field, and can point at any attribute
#     # on the serialized instance. It can also take the dotted notation shown above, in which ase it will
#     # traverse the give attributes, in a similar way as it is used with Django's template language.
#
#     # the untyped ReadOnlyField class, is always read-only, and will be used for serialized representations,
#     # will not be used for updating model instances when they are deserialized.
#     # we could have also used CharField(read_only=True)
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Snippet
#         # and make sure you also add 'owner', to the list of fields in the inner Meta class.
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']
#
#
# # got some users to work with, we'd better add representations of those users to our API.
#
# class UserSerializer(serializers.ModelSerializer):
#     # because 'snippets' is a  reverse relationship on the User model, it will not be included by default when using
#     # the ModelSerializer class, so we need to add an explicit field for it.
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']

# refactored using HyperlinkingModelSerializer

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        field = ['url', 'id', 'highlight', 'owner',
                 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedIdentityField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']