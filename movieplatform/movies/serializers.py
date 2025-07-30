from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    video_file = serializers.FileField(required=False, allow_null=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'date_added', 'video_file']
        read_only_fields = ['id', 'date_added']
    
    def to_representation(self, instance):
        """Custom representation to return video file path as string"""
        data = super().to_representation(instance)
        if instance.video_file:
            data['video_file'] = str(instance.video_file)
        return data 