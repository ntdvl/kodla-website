# Third-Party
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import generics, permissions

# Local Django
from api.serializers import ScreenControlSerializer


class ScreenControlView(generics.GenericAPIView):
    serializer_class = ScreenControlSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self._action(serializer)

    def _action(self, serializer):
        if serializer.screen:
            return Response(
                data={'name': serializer.screen.name}, status=status.HTTP_200_OK
            )
        else:
            return Response(status=status.HTTP_404_OK)
