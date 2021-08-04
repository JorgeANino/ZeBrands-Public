from .catalog.urls import urlpatterns as catalog_urlpatterns
from .user.urls import urlpatterns as user_urllpatterns


app_name = "catalog_system"

urlpatterns = []

urlpatterns += catalog_urlpatterns
urlpatterns += user_urllpatterns
