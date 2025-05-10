from django.urls import path
from rest_framework.routers import DefaultRouter,SimpleRouter
from . import views

router = SimpleRouter()
# router.register(r'phones',views.PhoneViewSet,basename="phones")
router.register(r'health-data',views.HealthDataViewSet,basename="health-data")




urlpatterns = [
    

]
urlpatterns+= router.urls