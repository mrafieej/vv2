from django.conf.urls import url
from . import views

app_name = 'listing'

urlpatterns = [
    url(r'^(?P<filter_id>[0-9]+)/$', views.home, name='home'),
    url(r'^listing/(?P<listing_id>[0-9a-fA-F]+)/$', views.listing_detail, name='listing_detail'),
    url(r'^create_listing/$', views.create_listing, name='create_listing'),
    url(r'^edit_listing/(?P<pk>[0-9a-fA-F]+)/$', views.EditListingView.as_view(), name='edit_listing'),
    url(r'^delete_listing/(?P<pk>[0-9a-fA-F]+)/$', views.DeleteListingView.as_view(), name='delete_listing'),

]

