from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ('is_deleted', 'user')
    
    def validate_title(self, value):
        if len(value) < 3 :
            raise serializers.ValidationError("Title must be at least 3 characters.")
        return value