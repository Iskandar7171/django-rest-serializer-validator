from rest_framework import serializers
from .models import Post
from rest_framework.exceptions import ValidationError

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def validate_title(self, value):
        if len(value) > 200:
            raise ValidationError("Title 200 tadan kam bolishi kere")
        return value

    def validate_description(self, value):
        if len(value) > 1000:
            raise ValidationError("Description 1000 tadan kam bolishi kere")
        return value