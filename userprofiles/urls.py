from django.conf.urls import url
from . import views

app_name = 'userprofiles'

urlpatterns = [
    # url(r'^register2/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^user/(?P<pk>[0-9a-fA-F]+)/$', views.UserProfileView.as_view(), name='user_profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^terms/$', views.terms, name='terms'),
    # url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^edit_profile/(?P<pk>[0-9a-fA-F]+)/$', views.EditUserProfileView.as_view(), name='edit_profile'),

]

