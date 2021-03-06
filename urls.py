from django.urls import include, path
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register('heroes', views.HeroViewSet)
router.register('listings', views.ListingsViewSet)
router.register('actors', views.ActorViewSet)
router.register('myapps', views.UserappsViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
    namespace='rest_framework')),
    # path('templates/new/', views.template_new, name='template_new'),
]
