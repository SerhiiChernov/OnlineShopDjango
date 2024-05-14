"""
URL configuration for OnlineShopDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from main.views import home
from shopItem.views import shopItemHome
from main.views import order_view
from itemList.views import ItemListHome
from main.views import show_category_items
from shopItem.views import shop_item_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # path('shop/', shopItemHome, name='shopItemHome'),
    path('order/', order_view, name='order'),
    path('itemListHome/', ItemListHome, name='itemListHome'),
    path('category/<int:category_id>/', show_category_items, name='category_items'),
    # path('shopItem/', shopItemHome, name='shopItemHome'),
    path('shopItem/<slug:cloth_slug>/', shop_item_detail, name='shop_item_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
