from django.conf.urls import url
from . import views

app_name = 'usermessages'

urlpatterns = [
    url(r'^inbox/(?P<pk>[0-9a-fA-F]+)/$', views.InboxView.as_view(), name='inbox'),
]

