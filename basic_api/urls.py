from django.urls import path, include
from .views import ArticalModelViewSet, artical, artical_details, ArticalAPIView, ArticalDetailsAPIView, ArticalGenericAPIView, ArticalViewSet, ArticalGenericViewSet, ArticalModelViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('artical', ArticalViewSet, basename = 'artical')

router1 = DefaultRouter()
router1.register('artical1', ArticalGenericViewSet, basename = 'artical1')

router2 = DefaultRouter()
router2.register('artical2', ArticalModelViewSet, basename = 'artical2')

urlpatterns = [
    #AUTHOR: FAISAL PORAG
    #View set Url example
    path('api/viewset/', include(router.urls)),
    path('api/viewset/<int:pk>/', include(router.urls)),

    #Generic View set Url example
    path('api/genericviewset/', include(router1.urls)),
    path('api/genericviewset/<int:pk>/', include(router1.urls)),

    #Model View set Url example
    path('api/modelviewset/', include(router2.urls)),
    path('api/modelviewset/<int:pk>/', include(router2.urls)),


    path('api/artical/', artical, name='artical'),
    #Url for class view api
    path('api/artical_v1/', ArticalAPIView.as_view()),
    path('api/articalDetails/<int:id>/', artical_details, name='articalDetails'),
    #Url for class view api
    path('api/articalDetails_v1/<int:id>/', ArticalDetailsAPIView.as_view()),
    #Url for generic view api
    path('api/artical_v2/<int:id>/', ArticalGenericAPIView.as_view()),
]
