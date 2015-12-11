"""digitalmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from checkout.views import CheckoutTestView, CheckoutAjaxView
from dashboard.views import DashboardView
from products.views import UserLibraryListView

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^test/$', CheckoutTestView.as_view(), name='test'),
    url(r'^checkout/$', CheckoutAjaxView.as_view(), name='checkout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^seller/', include("sellers.urls", namespace='sellers')),
    url(r'^tags/', include("tags.urls", namespace='tags')),
    url(r'^library/', UserLibraryListView.as_view(), name='library'),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
