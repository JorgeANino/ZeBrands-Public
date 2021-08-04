from catalog_system.core.views import CatalogSystemModelViewset
from .serializers import ProductSerializer
from .models import Product


class ProductView(CatalogSystemModelViewset):
    """View to interact with Product model"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("-created_at")
