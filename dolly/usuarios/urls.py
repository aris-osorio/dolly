from usuarios.views import UsuariosViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UsuariosViewSet)

urlpatterns = router.urls