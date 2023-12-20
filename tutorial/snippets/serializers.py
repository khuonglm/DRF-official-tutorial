from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

"""
Serializers allow complex data such as querysets and model instances 
to be converted to native Python datatypes that can then be easily rendered 
into JSON, XML or other content types
"""
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    """
    This field is of the same type as the url field, 
    except that it points to the 'snippet-highlight' url pattern, 
    instead of the 'snippet-detail' url pattern. 
    returned format: html
    """
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Because 'snippets' is a reverse relationship on the User model, 
    it will not be included by default when using the ModelSerializer class, 
    so we needed to add an explicit field for it.
    """
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']