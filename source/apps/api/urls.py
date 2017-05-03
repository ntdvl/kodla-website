# Third-Party
from rest_framework import routers

# Django
from django.conf.urls import url, include

# Local Django
from api.views import ScreenControlView


# Django Rest Framework Router
# router_v1 = routers.DefaultRouter()
# router_app = routers.DefaultRouter()

# for api in LIST_V1:
#     router_v1.register(api[0], api[1], base_name=api[2])

# for api in LIST_APP:
#     router_app.register(api[0], api[1], base_name=api[2])


urlpatterns = [
    # url(r'^v1/', include(router_v1.urls, namespace='v1')),
    # url(r'^screen/', include(router_app.urls, namespace='screen')),
    url(r'^screen/control/', ScreenControlView.as_view(), name='screen-control'),
]
