from rest_framework import serializers
from apps.manga.models import Manga

class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['id', 
                'titulo',  
                'Autor',
                'descricao', 
                ]
