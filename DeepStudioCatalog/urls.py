"""DeepStudioCatalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import catalog.views
import taco.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',catalog.views.index, name='home'),
    path('test/',catalog.views.test, name='test'),
    path('tacotron/',taco.views.tacotron_index, name='tacotron_index'),
    path('results/',taco.views.results, name='results'),
    path('tacotron/create/',taco.views.create, name='create'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
