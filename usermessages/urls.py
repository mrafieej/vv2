from django.conf.urls import url
from . import views

app_name = 'usermessages'

urlpatterns = [
    url(r'^inbox/(?P<pk>[0-9a-fA-F]+)/$', views.InboxView.as_view(), name='inbox'),
    # url(r'^message/$', views.message_detail, name='message_detail'),
    url(r'^message/(?P<user_id_other>[0-9a-fA-F]+)/listing/(?P<listing_id>[0-9a-fA-F]+)/$', views.message_detail, name='message_detail'),

]

