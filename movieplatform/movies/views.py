from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie
from .serializers import MovieSerializer
import logging

logger = logging.getLogger(__name__)

# Views are created here
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        logger.info(f"Creating movie with the data: {request.data}")
        logger.info(f"Files in request: {request.FILES}")
        try:
            # Handle case where no video file is provided
            if 'video_file' not in request.FILES:
                logger.info("No video file provided, creating movie without video")
            else:
                logger.info(f"Video file found: {request.FILES['video_file']}")
            
            result = super().create(request, *args, **kwargs)
            logger.info(f"Movie created successfully: {result.data}")
            return result
        except Exception as e:
            logger.error(f"Error creating the movie: {e}")
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def list(self, request, *args, **kwargs):
        logger.info("Listing movies")
        return super().list(request, *args, **kwargs)