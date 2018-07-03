from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index_view, name='main'),
    url(r'^bikes/(?P<prod_num>[0-3]{1})/$', views.bike_view),
    url(r'^CD/(?P<prod_num>[0-5]{1})/$', views.cd_type_view),
    url(r'^book/(?P<prod_num>[0-3]{1})/$', views.book_type_view),
    url(r'^p-buy/(?P<prod_name>[-\w]+)/$', views.product_zoom_view),
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^(?P<prod_name>[-\w]+)/$', views.endbuy_view),
    url(r'^aux/(?P<orderID>[0-9]{2})/$', views.confirm_view),
    url(r'^cart/see/$', views.cart_view),
    url(r'^AJAX$', views.myAJAX_view),
    url(r'^confirm/cart$', views.confirm_cart)
]
