from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

"""
Serializers allow complex data such as querysets and model instances 
to be converted to native Python datatypes that can then be easily rendered 
into JSON, XML or other content types
"""
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']