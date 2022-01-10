"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include,register_converter
from listings import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls.converters import StringConverter

register_converter(StringConverter, 'username')

urlpatterns = [
path('admin/', admin.site.urls),
path('accounts/', include('django.contrib.auth.urls')),
path('home/', views.home, name='home'),
path('home/register/', views.SignUp.as_view(), name='register'),
path('accounts/login/flux/', views.flux, name='flux'),
path('accounts/login/subs/', views.subs, name='subs'),
path('accounts/login/posts/', views.posts, name='posts'),
path('accounts/login/flux/ask-rev/', views.ask_rev),
path('accounts/login/flux/make-rev/', views.make_rev),
path('accounts/login/flux/<int:id>/answer-rev/', views.answer_rev),
path('accounts/login/posts/<int:id>/update-rev/', views.update_rev),
path('accounts/login/posts/<int:id>/update-tkt/', views.update_tkt),
path('accounts/login/posts/<int:id>/delete-tkt/', views.delete_tkt),
path('accounts/login/posts/<int:id>/delete-rev/', views.delete_rev),
path('accounts/login/subs/<int:id>/delete-follow/', views.delete_follow)
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)