from django.urls import path
from .views import ProdutoViewSet
from rest_framework.routers import SimpleRouter

router1 = SimpleRouter()
router1.register('produto', ProdutoViewSet)


