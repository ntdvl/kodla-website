# Third-Party
from channels.routing import route_class
from channels.generic.websockets import WebsocketDemultiplexer

# Local Django
from api.bindings import ScreenContentBinding


class APIDemultiplexer(WebsocketDemultiplexer):
    consumers = {
      'screen_contents': ScreenContentBinding.consumer
    }


channel_routing = [
    route_class(APIDemultiplexer)
]
