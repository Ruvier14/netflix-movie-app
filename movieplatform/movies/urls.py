from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet
from django.http import JsonResponse

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')


#This is for debug purposes: Prings the registered URLS

print("Register URLS:")
for url in router.urls:
    print(f" {url}")

# Adding a simple test endpoint
def test_api(request):
    return JsonResponse({'message': 'API is working'})

urlpatterns = [
    path('test/', test_api, name='test-api'),
    path('', include(router.urls)),
]