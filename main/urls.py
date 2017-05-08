from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: about/frogs or about/frogs_and_spiders
    url(r'^about/(?P<topic>[^/]+)$', views.AboutView.as_view(),
        name='about'),
]
