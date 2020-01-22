from rest_framework.routers import DefaultRouter
from snippets.api.views.user import UserViewSet
from snippets.api.views.snippet import SnippetViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)