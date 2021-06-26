from django.urls import path, include
from .views import artical, artical_details, ArticalAPIView, ArticalDetailsAPIView, ArticalGenericAPIView, ArticalViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('artical', ArticalViewSet, basename = 'artical')

urlpatterns = [

    #View set Url example
    path('api/viewset/', include(router.urls)),
    path('api/viewset/<int:pk>/', include(router.urls)),


    path('api/artical/', artical, name='artical'),
    #Url for class view api
    path('api/artical_v1/', ArticalAPIView.as_view()),
    path('api/articalDetails/<int:id>/', artical_details, name='articalDetails'),
    #Url for class view api
    path('api/articalDetails_v1/<int:id>/', ArticalDetailsAPIView.as_view()),
    #Url for generic view api
    path('api/artical_v2/<int:id>/', ArticalGenericAPIView.as_view()),
]