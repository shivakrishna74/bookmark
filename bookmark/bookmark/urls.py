from django.conf.urls import url
from django.contrib import admin
from newapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^display/',views.display),
    url(r'^insertnewapp/',views.insertnewapp, name='insertnewapp'),
    url(r'^enter/(?P<decription>[A-Za-z0-9]+)/$',views.enter,name='enter'),
]
