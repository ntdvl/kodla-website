# Third-Party
from rest_framework import serializers

# Django
from django.utils.translation import ugettext_lazy as _

# Local Django
from screen.models import DocumentKind, Screen, ScreenContent


class ScreenControlSerializer(serializers.Serializer):
    screen_key = serializers.CharField(
        max_length=30, style={'placeholder': 'Screen Key'}
    )
    screen_secret = serializers.CharField(
        max_length=50, style={'placeholder': 'Screen Secret'}
    )

    def __init__(self, *args, **kwargs):
        super(ScreenControlSerializer, self).__init__(*args, **kwargs)
        self.screen = None

    def validate(self, attrs):
        try:
            self.screen = Screen.objects.get(
                screen_key=attrs.get('screen_key'),
                screen_secret=attrs.get('screen_secret')
            )

            return attrs
        except Screen.DoesNotExist:
            raise serializers.ValidationError(_('Screen not found!'))


class DocumentKind(serializers.ModelSerializer):

    class Meta:
        model = DocumentKind
        fields = ('id', 'name', 'tag')


class ScreenContentSerializer(serializers.ModelSerializer):
    kind = DocumentKind()

    class Meta:
        model = ScreenContent
        fields = ('id', 'kind', 'document', 'text')
