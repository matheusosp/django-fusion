import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created_at = models.DateField('Create at', auto_now_add=True)
    modified = models.DateField('Update at', auto_now=True)
    active = models.BooleanField('active', default=True)

    class Meta:
        abstract = True


class Services(Base):
    ICON_CHOISES = {
        ('lni-cog', 'gear'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
        ('lni-laptop-phone', 'Phone'),
        ('lni-leaf', 'Leaf'),
        ('lni-layers', 'Layers')
    }
    service = models.CharField('Service', max_length=100)
    description = models.TextField('description', max_length=200)
    icon = models.CharField('icon', max_length=25, choices=ICON_CHOISES)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service


class Office(Base):
    office = models.CharField('Office', max_length=100)

    class Meta:
        verbose_name = 'Office'
        verbose_name_plural = 'responsibility'

    def __str__(self):
        return self.office


class Employee(Base):
    name = models.CharField('Name', max_length=100)
    office = models.ForeignKey('core.Office', verbose_name='Office', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    img = StdImageField("Image", upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'employees'

    def __str__(self):
        return self.name


class Features(Base):
    ICON_CHOISES = {
        ('lni-cog', 'gear'),
        ('lni-stats-up', 'Graphic'),
        ('lni-users', 'Users'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
        ('lni-laptop-phone', 'Phone'),
        ('lni-leaf', 'Leaf'),
        ('lni-layers', 'Layers'),
    }
    name = models.CharField('Name', max_length=100)
    description = models.TextField('description', max_length=200)
    icon = models.CharField('icon', max_length=25, choices=ICON_CHOISES)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.name
