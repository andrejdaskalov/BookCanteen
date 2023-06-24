"""
URL configuration for BookCanteen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from BookCanteenPrototype import views
from django.conf import settings    
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('details/<int:book_id>/', views.book_details, name='book'),
    path('buy/<int:book_id>/', views.buy_book, name='buy'),
    path('thankyou/', views.thank_you, name='thank_you'),
    path('thankyou_seller/', views.thank_you_seller, name='thank_you_seller'),
    path('sell/', views.sell, name='sell'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
