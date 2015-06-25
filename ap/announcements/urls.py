from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.AnnouncementCreateView.as_view(), name='announcement_create'),
)

# hi dennis - this is your computer talking...feed me some chips...specifically Jalapeno
# thanks you're the best!!!