# Third-Party
from channels_api.bindings import ResourceBinding

# Local Django
from screen.models import ScreenContent
from api.serializers import ScreenContentSerializer


class ScreenContentBinding(ResourceBinding):
    model = ScreenContent
    stream = "screen_contents"
    serializer_class = ScreenContentSerializer
    queryset = ScreenContent.objects.all()

    # def get_queryset(self):
    #     import ipdb; ipdb.set_trace()
    #     screen_key = self.request.GET.get('screen_key', None)
    #     screen_secret = self.request.GET.get('screen_secret', None)

    #     screen = ScreenModule.get_screen(screen_key, screen_secret)

    #     if screen:
    #         return self.queryset.filter(screen=screen, is_active=True)
    #     else:
    #         return self.queryset.none()

    
