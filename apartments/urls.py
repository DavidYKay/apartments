from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tracker.views import ApartmentListView, ApartmentDetailView

urlpatterns = patterns('',
    # Examples:
     #url(r'^$', 'apartments.views.home', name='home'),
    url(r'^$', ApartmentListView.as_view(), name='home'),
    url(r'^apartments/(?P<pk>\d)', ApartmentDetailView.as_view(),
        name='apartment_detail'),
    # url(r'^apartments/', include('apartments.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
