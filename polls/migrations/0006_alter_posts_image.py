# Generated by Django 3.2 on 2021-04-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to=''),
        ),
    ]