from rest_framework import routers

from .views import ProductView

router = routers.SimpleRouter()
router.register(r"product", ProductView, basename="product")
urlpatterns = router.urls
