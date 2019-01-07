"""findmypg URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static


from main import views as main
from owner import views as owner
from user import views as user

urlpatterns = [
    #Admin
    path(r'owner/', owner.index),
    path(r'owner/register/', owner.register),
    path(r'owner/login/', owner.login),
    path(r'owner/logout/', owner.logout),
    path(r'owner/profile/', owner.profile),
    path(r'owner/profilephoto/', owner.ProfilePhoto),
    path(r'owner/addpg/', owner.addpg),
    path(r'owner/delete/<int:id>', owner.deletepg),
    path(r'owner/update/<int:id>', owner.updatepg),
    path(r'owner/pgs/', owner.pglist),
    path(r'owner/notifications/', owner.Notifications),


    #User
    path(r'', user.index),
    path(r'search/',user.search),
    path(r'search/<int:page>/', user.search),
    path(r'pg/details/<int:pgid>/',user.PGDetail),
    path(r'pg/contact/<int:pgid>',user.Contact),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


