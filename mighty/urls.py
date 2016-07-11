"""mighty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mighty_app.views import IndexView, ProfileView, RegisterView, CookOrderUpdateView, OrderCreateView, OrderListView, MeunItemCreateView, MenuUpdateView, MenuItemListView, OrderDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^register/$', RegisterView.as_view(), name='register_view'),
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profile_view'),
    url(r'^order/$', OrderListView.as_view(), name='order_list_view'),
    url(r'^order/add$', OrderCreateView.as_view(), name='order_create_view'),
    url(r'^order/(?P<pk>\d+)/$', OrderDetailView.as_view(), name='order_detail_view'),
    url(r'^order/(?P<pk>\d+)/cook/$', CookOrderUpdateView.as_view(), name='cook_order_detail_view'),
    url(r'^menu/$', MenuItemListView.as_view(), name='menu_item_list_view'),
    url(r'^menu/add/$', MeunItemCreateView.as_view(), name='menu_item_create_view'),
    url(r'^menu/(?P<pk>\d+)$', MenuUpdateView.as_view(), name='menu_item_update_view'),

]
