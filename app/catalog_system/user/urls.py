from rest_framework import routers

from .views import UserView

router = routers.SimpleRouter()
router.register(r"user", UserView, basename="user")

urlpatterns = router.urls
