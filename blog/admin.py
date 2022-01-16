from django.contrib import admin
from blog.models import KategoriModel
from blog.models.makale import Makale

admin.site.register(KategoriModel)
admin.site.register(Makale)