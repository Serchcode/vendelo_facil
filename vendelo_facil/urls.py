
from django.conf.urls import url,include
from django.contrib import admin
from main import urls as mainUrls
from django.conf import settings
from django.views.static import serve 
from django.conf.urls.static import static
from accounts import urls as accUrls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(mainUrls,namespace="main")),
    url(r'^accounts/', include(accUrls)),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}),
]
