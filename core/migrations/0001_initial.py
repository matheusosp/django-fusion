# Generated by Django 3.1.5 on 2021-01-16 22:34

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Create at')),
                ('modified', models.DateField(auto_now=True, verbose_name='Update at')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('office', models.CharField(max_length=100, verbose_name='Office')),
            ],
            options={
                'verbose_name': 'Office',
                'verbose_name_plural': 'responsibility',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Create at')),
                ('modified', models.DateField(auto_now=True, verbose_name='Update at')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('service', models.CharField(max_length=100, verbose_name='Service')),
                ('description', models.TextField(max_length=200, verbose_name='description')),
                ('icon', models.CharField(choices=[('lni-cog', 'gear'), ('lni-mobile', 'Mobile'), ('lni-stats-up', 'Graphic'), ('lni-layers', 'Design'), ('lni-users', 'Users'), ('lni-rocket', 'Rocket')], max_length=15, verbose_name='icon')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Create at')),
                ('modified', models.DateField(auto_now=True, verbose_name='Update at')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('bio', models.TextField(max_length=200, verbose_name='Bio')),
                ('img', stdimage.models.StdImageField(upload_to='team', verbose_name='Image')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.office', verbose_name='Office')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'employees',
            },
        ),
    ]