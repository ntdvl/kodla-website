# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import DateModel


class Screen(DateModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    screen_key = models.CharField(
        verbose_name=_('Screen Key'), max_length=30, unique=True
    )
    screen_secret = models.CharField(
        verbose_name=_('Screen Secret'), max_length=50, unique=True
    )
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)

    class Meta:
        verbose_name = _(u'Screen')
        verbose_name_plural = _(u'Screens')
        ordering = ('name',)

    def __str__(self):
        return '{name}'.format(name=self.name)
    


class DocumentKind(DateModel):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    tag = models.CharField(verbose_name=_('Tag'), max_length=100)

    class Meta:
        verbose_name = _('Document Kind')
        verbose_name_plural = _('Document Kinds')
        ordering = ('name',)

    def __str__(self):
        return '{name}'.format(name=self.name)



def set_screen_document_upload_path(instance, filename):
    return '/'.join([
        'screen_contents', 'screen_content_%d' % instance.id, 'document', filename]
    )


class ScreenContent(DateModel):
    document = models.FileField(
        verbose_name=_('Document'), null=True, blank=True,
        upload_to=set_screen_document_upload_path
    )
    text = models.TextField(
        verbose_name=_('Text'), max_length=2000, null=True, blank=True
    )
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    kind = models.ForeignKey(verbose_name=_('Kind'), to='screen.DocumentKind')
    screens = models.ManyToManyField(
        verbose_name=_('Screens'), to='screen.Screen', blank=True
    )

    class Meta:
        verbose_name = _('Screen Content')
        verbose_name_plural = _('Screen Contents')
        ordering = ('-update_date',)

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_document = self.document
            self.document = None
            super(ScreenContent, self).save(*args, **kwargs)
            self.document = saved_document

        return super(ScreenContent, self).save(*args, **kwargs)

    def __str__(self):
        if self.document:
            return self.get_document_name()
        else:
            return '{text}...'.format(text=self.text[:10])

    def get_document_name(self):
        if self.document:
            return str(self.document.file).split('/')[-1]
        else:
            return None

    def get_screens(self):
        return ', '.join([screen.name for screen in self.screens.all()])
