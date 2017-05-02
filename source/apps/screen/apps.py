# Django
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ScreenConfig(AppConfig):
    name = 'screen'
    verbose_name = _('Screen')
