# Generated by Django 5.2 on 2025-05-03 02:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='official_packaging_images',
        ),
        migrations.CreateModel(
            name='ReferenceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_label', models.CharField(choices=[('front', 'Front View'), ('back', 'Back View'), ('side', 'Side View'), ('top', 'Top View'), ('bottom', 'Bottom View')], help_text='Which view of the packaging this image represents', max_length=20)),
                ('image_url', models.URLField(help_text='Cloudinary or static URL to the reference image', max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reference_images', to='medicine.medicine')),
            ],
            options={
                'ordering': ['medicine', 'view_label'],
                'unique_together': {('medicine', 'view_label')},
            },
        ),
    ]
