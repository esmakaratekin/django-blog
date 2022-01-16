from django.contrib.auth.models import User
from django.db import models

from blog.models import KategoriModel


class Makale(models.Model):
    baslik = models.CharField(max_length=30)
    yayinlanma_tarihi = models.DateTimeField(auto_now_add=True, editable=False)
    kategori = models.ForeignKey(KategoriModel, on_delete=models.SET_NULL,null=True)
    yazar = models.ForeignKey(User, on_delete=models.CASCADE)
    icerik = models.TextField()
    resim = models.ImageField(upload_to="blog/")

    def __str__(self):
        return self.baslik