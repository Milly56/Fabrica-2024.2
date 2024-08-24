from rest_framework import viewsets
from .serializer import MangaSerializers
from apps.manga.models import Manga

class MangaSerializers(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializers

    def create(self,request,*args, **kwargs):
        title: request
        requesicao=f"https://api.mangadex.org/manga/{id}"

        requesicao=request.get(
            f"https://api.mangadex.org/manga/{id}"
        )
    
        manga_salvo=Manga.objects.create()  
        titulo=requesicao["titulo"]
        Autor=requesicao['Autor']
        descricacao=requesicao['descricao'] 




