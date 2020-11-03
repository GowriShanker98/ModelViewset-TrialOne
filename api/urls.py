from django.urls import path,include
from api import views

app_name="api"
from rest_framework import routers
router=routers.DefaultRouter()
router.register('modelviewsets',views.UserProfileModelViewSet),

urlpatterns = [
    path('sampleapiview/',views.SampleApiView.as_view(),name="apiview"),
    path('',include(router.urls)),
]
