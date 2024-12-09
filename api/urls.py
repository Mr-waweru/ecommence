from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("users", views.UserViewSet, basename="user")
router.register("products", views.ProductViewSet)
router.register("categories", views.CategoryViewSet)
router.register("orders", views.OrderViewSet)

urlpatterns = [] + router.urls