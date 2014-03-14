from django.contrib.auth.models import User, Group
from rest_framework import serializers
from server.models import Course

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    courses = serializers.RelatedField(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'courses')
        read_only_fields = ('username')

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)	

# 	TODO: Implement this
    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.title = attrs.get('title', instance.title)
            instance.code = attrs.get('code', instance.code)
            instance.linenos = attrs.get('linenos', instance.linenos)
            instance.language = attrs.get('language', instance.language)
            instance.style = attrs.get('style', instance.style)
            return instance

        # Create new instance
        return Course(**attrs)        