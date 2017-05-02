# Django
from django.utils.crypto import get_random_string

# Local Django
from screen.models import Screen


class ScreenModule(object):

    @staticmethod
    def create_unique_screen_key(length=30):
        screen = True

        while screen:
            try:
                screen_key = get_random_string(length=length)
                screen = Screen.objects.get(screen_key=screen_key)
            except Screen.DoesNotExist:
                screen = None

        return screen_key

    @staticmethod
    def create_unique_screen_secret(length=50):
        screen = True

        while screen:
            try:
                screen_secret = get_random_string(length=length)
                screen = Screen.objects.get(screen_secret=screen_secret)
            except Screen.DoesNotExist:
                screen = None

        return screen_secret

    @staticmethod
    def get_screen(screen_key, screen_secret):
        try:
            screen = Screen.objects.get(
                screen_key=screen_key, screen_secret=screen_secret, is_active=True
            )
        except Screen.DoesNotExist:
            screen = None

        return screen
