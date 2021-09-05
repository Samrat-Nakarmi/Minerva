# Generated by Django 3.2.7 on 2021-09-04 19:50

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_module_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.TextField()),
                ('options', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='module',
            name='value',
        ),
        migrations.AddField(
            model_name='module',
            name='text_store',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='module',
            name='url_store',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='module',
            name='quiz_store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='course.quiz'),
        ),
    ]
