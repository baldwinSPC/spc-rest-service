from django.conf.urls import patterns, url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#router.register(r'architecture', views.ArchitectureViewSet)
#router.register(r'architecture/$', views.ArchitectureList.as_view(), base_name="architecture")
#router.register(r'architecture/(?P<pk>[0-9]+)/$', views.ArchitectureDetail.as_view(), base_name="architecture")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
	url(r'^architecture/$', views.ArchitectureList.as_view()),
	url(r'^architecture/(?P<pk>[0-9]+)/$', views.ArchitectureDetail.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)