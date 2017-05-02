# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.modules import ScreenModule
from screen.models import Screen, DocumentKind, ScreenContent


@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    actions = ['regenerate_screen_secret']

    fieldsets = (
        (_(u'Base Informations'), {
            'fields' : ('name',),
        }),
        (_(u'Screen Informations'), {
            'fields' : (
                'is_active', 'screen_key',
                'screen_secret', 'create_date', 'update_date'
            )
        }),
    )

    list_display = (
        'name', 'screen_key', 'screen_secret', 
        'create_date', 'update_date', 'is_active',
    )
    list_filter = ('create_date', 'update_date', 'is_active')
    search_fields = ('name',)
    readonly_fields = ('create_date', 'update_date', 'screen_key', 'screen_secret')


    def regenerate_screen_secret(self, request, queryset):
        for screen in queryset:
            screen.screen_secret = ScreenModule.create_unique_screen_secret(50)
            screen.save()
    regenerate_screen_secret.short_description = _('Regenerate screen secret')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.screen_key = ScreenModule.create_unique_screen_key(30)
            obj.screen_secret = ScreenModule.create_unique_screen_secret(50)

        obj.save()


@admin.register(DocumentKind)
class DocumentKindAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag')
    search_fields = ('name', 'tag')


@admin.register(ScreenContent)
class ScreenContentAdmin(admin.ModelAdmin):
    fieldsets = (
        (_(u'Base Informations'), {
            'fields' : ('kind', 'screens'),
        }),
        (_(u'Screen Content Informations'), {
            'fields' : (
                'is_active', 'document', 'text'
            )
        }),
    )

    filter_horizontal = ('screens',)
    list_display = ('__str__', 'get_screens')

