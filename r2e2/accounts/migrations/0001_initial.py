# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BuildingAdmin',
            fields=[
                ('customuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('priorityLevel', models.IntegerField(default=2, editable=False)),
                ('additionalProperties', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Building Administrator',
            },
            bases=('accounts.customuser',),
        ),
        migrations.CreateModel(
            name='DepartmentChair',
            fields=[
                ('customuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('priorityLevel', models.IntegerField(default=1, editable=False)),
                ('additionalProperties', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Department Chair',
            },
            bases=('accounts.customuser',),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('customuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('priorityLevel', models.IntegerField(default=3, editable=False)),
                ('additionalProperties', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Faculty Member',
            },
            bases=('accounts.customuser',),
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('customuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('priorityLevel', models.IntegerField(default=5, editable=False)),
                ('additionalProperties', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Guest',
            },
            bases=('accounts.customuser',),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('customuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('priorityLevel', models.IntegerField(default=4, editable=False)),
                ('additionalProperties', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name': 'Organization',
            },
            bases=('accounts.customuser',),
        ),
        migrations.AddField(
            model_name='adviser',
            name='faculty',
            field=models.ForeignKey(to='accounts.Faculty'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='adviser',
            name='organization',
            field=models.ForeignKey(to='accounts.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
