# Generated by Django 4.2.7 on 2023-11-13 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0002_alter_oauthconfig_options_alter_oauthuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oauthuser',
            name='nickname',
            field=models.CharField(max_length=50, verbose_name='nick name'),
        ),
    ]
