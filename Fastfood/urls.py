"""
URL configuration for Fastfood project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ProductViewSet, CheckoutViewSet, CategoryViewSet, \
    SpacialOfferViewSet, ProductQuantityViewSet

router = DefaultRouter()

# Registering routes without using the `check_token` decorator
router.register(r'products', ProductViewSet)
router.register(r'offers', SpacialOfferViewSet )
router.register(r'checkouts', CheckoutViewSet)
router.register(r'categories', CategoryViewSet)
router.register('quantity',ProductQuantityViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls),name='api'),
    path('user/', include('User.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
