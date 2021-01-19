import uuid
from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _

ICON_CHOISES = {
    ("lni-cog", _("gear")),
    ("lni-stats-up", _("Graphic")),
    ("lni-users", _("Users")),
    ("lni-layers", _("Design")),
    ("lni-mobile", _("Mobile")),
    ("lni-rocket", _("Rocket")),
    ("lni-laptop-phone", _("Phone")),
    ("lni-leaf", _("Leaf")),
    ("lni-layers", _("Layers"))
}


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created_at = models.DateField(_('Create at'), auto_now_add=True)
    modified = models.DateField(_('Update at'), auto_now=True)
    active = models.BooleanField(_('active'), default=True)

    class Meta:
        abstract = True


class Office(Base):
    office = models.CharField(_('Office'), max_length=100)

    class Meta:
        verbose_name = _('Office')
        verbose_name_plural = _('responsibility')

    def __str__(self):
        return self.office


class Employee(Base):
    name = models.CharField(_('Name'), max_length=100)
    office = models.ForeignKey('core.Office', verbose_name=_('Office'), on_delete=models.CASCADE)
    bio = models.TextField(_('Bio'), max_length=200)
    img = StdImageField(_("Image"), upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480,
                                                                                   'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('employees')

    def __str__(self):
        return self.name


class Features(Base):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('description'), max_length=200)
    icon = models.CharField('icon', choices=ICON_CHOISES, max_length=25)

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    def __str__(self):
        return self.name


class Services(Base):
    service = models.CharField(_('Service'), max_length=100)
    description = models.TextField(_('description'), max_length=200)
    icon = models.CharField('icon', choices=ICON_CHOISES, max_length=25)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.service
