from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.AnnouncementListView.as_view(), name='announcement_list'),
	url(r'^create$', views.AnnouncementCreateView.as_view(), name='announcement_create'),
	url(r'^(?P<pk>\d+)/detail-delete$', views.AnnouncementDeleteView.as_view(), name='announcement_delete'),

)

# hi dennis - this is your computer talking...feed me some chips...specifically Jalapeno
# thanks you're the best!!!