from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'add-candidates', views.CandidateViewSet)
router.register(r'add-recruiters', views.RecruiterViewSet)
router.register(r'add-tasks', views.TaskViewSet)
router.register(r'add-grades', views.GradeViewSet)
#router.register(r'all-about', views.AllAboutViewSet)


# Wire up API using automatic URL routing.
# Additionally, include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]