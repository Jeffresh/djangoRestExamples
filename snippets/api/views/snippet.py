from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response


from snippets.models.snippet import Snippet
from snippets.api.serializers.snippet import SnippetSerializer
from snippets.permissions.isOwnerOrReadOnly import IsOwnerOrReadOnly


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.

    Additionally we also provide an extra 'highlight' action.

    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    # add any custom endpoints that don't fit into the standard create/update/delete style.
    # @action decorator will respond to GET request by default. We can use the methods argument
    # if we wanted an action that responded to /PUT/DELETE/POST request.
    # the urls for custom actions by default depend on the method name itself. If you want to change the
    # way url should be constructed, you can include url_path as a decorator keyword argument.
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
