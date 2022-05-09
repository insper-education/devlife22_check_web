from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('loja/', include('loja.urls'), name="loja"),
    #path('', include('loja.urls'), name="homepage"),
]
 