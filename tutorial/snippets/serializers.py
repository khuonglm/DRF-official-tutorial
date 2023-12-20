from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

"""
Serializers allow complex data such as querysets and model instances 
to be converted to native Python datatypes that can then be easily rendered 
into JSON, XML or other content types
"""
class SnippetSerializer(serializers.ModelSerializer):
    """
    The untyped ReadOnlyField is always read-only, 
    and will be used for serialized representations, 
    but will not be used for updating model instances 
    when they are deserialized. We could have also used CharField(read_only=True) here.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

class UserSerializer(serializers.ModelSerializer):
    """
    Because 'snippets' is a reverse relationship on the User model, 
    it will not be included by default when using the ModelSerializer class, 
    so we needed to add an explicit field for it.
    """
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']