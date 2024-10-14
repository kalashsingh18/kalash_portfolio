"""
URL configuration for kalash_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from update_project import urls as update_urls
from add_project import urls as add_p_urls
from add_aboutyou import urls as add_about_url
from acess_the_Cam import urls as acess_the_CamUrl
urlpatterns = [
    path('admin/', admin.site.urls),
    path("update_project",include(update_urls)),
    path("add_project",include(add_p_urls)),
    path("add_aboutyou",include(add_about_url)),
    path('api-auth/', include('rest_framework.urls')),
    path("acess_the_Cam/",include(acess_the_CamUrl)),
    
]
