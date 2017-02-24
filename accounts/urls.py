from django.conf.urls import url, include
from django.contrib.auth.views import logout, login , logout_then_login
from . import views
from products import urls as productsurls
urlpatterns = [
	url(r'^registro/$', views.Registration.as_view(),name="registro"),
	url(r'^profile/$', views.Dashboard.as_view(), name="profile"),
	url(r'^login/$', login, name="login"),
	url(r'^logout/$', logout, name="logout"),
	url(r'^logout-then-login/$', logout_then_login, name="logout_then_login"),
	url(r'^product/',include(productsurls, namespace="product")),

]