from django.shortcuts import render, get_object_or_404

from blog.models import KategoriModel
from blog.models.makale import Makale


def anasayfa(request):
    context = {
        "makaleler": Makale.objects.all(),
        "kategoriler": KategoriModel.objects.all()
    }
    return render(request, "anasayfa.html", context)

def blog_detay(request, id):
    makale = get_object_or_404(Makale, id=id)
    context ={
        "makale": makale,
        "kategoriler": KategoriModel.objects.all()
    }
    return render(request ,"blog-detay.html", context)