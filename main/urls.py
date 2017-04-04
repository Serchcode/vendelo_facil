from django.conf.urls import url, include
from . import views
from products import urls as productsurls


urlpatterns=[
	url(r'^$',views.HomeView.as_view(),name='home'),
	url(r'^product/',include(productsurls, namespace="product")),

]