from rest_framework import viewsets
from .serializer import MangaSerializers
from apps.manga.models import Manga

class MangaSerializers(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializers

    def create(self,request,*args, **kwargs):
        title: request
        requesicao=f"https://api.mangadex.org/manga?title={title}"

        requesicao=request.get(
            f"https://api.mangadex.org/manga?title={title}"
        )
    
        manga_salvo=Manga.objects.create()
        Title=requesicao["title"]
        descricacao=requesicao['descricao']



