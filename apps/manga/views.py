from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Manga
from .api.serializer import MangaSerializer

class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer

    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    