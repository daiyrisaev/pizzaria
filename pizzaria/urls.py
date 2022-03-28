"""pizzaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.pizzamarket.views import FoodsListView, FoodsDetailView, MenuView, add_comment_publication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('publication-list/',FoodsListView.as_view(),
         name='publication-list-url'),                             #маршитизатор
    path('publication-list/<int:pub_pk>/',FoodsDetailView.as_view(),
         name='publication-detail-url'),
    path('menu/', MenuView.as_view(),
         name='publication-menu-url'),
    path('blog/<int:pk>/comment-add/',add_comment_publication, name='add-publication-comment-url'),
    path('django-rq/', include('django_rq.urls')),
    # path('email/',show_my_email)

]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
