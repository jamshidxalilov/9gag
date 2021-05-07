# Generated by Django 3.2 on 2021-05-06 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gag.helpers
import gag.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=50)),
                ('name_ru', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=gag.helpers.UploadTo('category'))),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
            bases=(gag.mixins.TranslateMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Izoh')),
                ('file', models.FileField(upload_to=gag.helpers.UploadTo('post'), verbose_name='Rasm/Video')),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.category', verbose_name='Kategoriya')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=gag.helpers.UploadTo('comment'))),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.postcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
