from rest_framework.decorators import action
from rest_framework.response import Response

from user.models import CatalogUser
from catalog_system.core.views import CatalogSystemModelViewset
from .serializers import UserSerializer


class UserView(CatalogSystemModelViewset):
    """Retrieve user information"""

    serializer_class = UserSerializer
    queryset = CatalogUser.objects.all()

    @action(detail=False)
    def me(self, request):
        serializer = self.get_serializer(self.request.user)
        return Response(serializer.data)
