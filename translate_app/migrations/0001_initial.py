# Generated by Django 4.1 on 2022-09-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TranslateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_to_translate', models.CharField(choices=[('ar', 'arabic'), ('az', 'azerbaijani'), ('zh-cn', 'chinese (simplified)'), ('hr', 'croatian'), ('cs', 'czech'), ('da', 'danish'), ('en', 'english'), ('fr', 'french'), ('de', 'german'), ('el', 'greek'), ('it', 'italian'), ('ja', 'japanese'), ('pl', 'polish'), ('pt', 'portuguese'), ('ru', 'russian'), ('es', 'spanish'), ('tr', 'turkish'), ('uz', 'uzbek')], default='en', max_length=20)),
                ('language_to_be_translated', models.CharField(choices=[('ar', 'arabic'), ('az', 'azerbaijani'), ('zh-cn', 'chinese (simplified)'), ('hr', 'croatian'), ('cs', 'czech'), ('da', 'danish'), ('en', 'english'), ('fr', 'french'), ('de', 'german'), ('el', 'greek'), ('it', 'italian'), ('ja', 'japanese'), ('pl', 'polish'), ('pt', 'portuguese'), ('ru', 'russian'), ('es', 'spanish'), ('tr', 'turkish'), ('uz', 'uzbek')], default='ru', max_length=20)),
                ('text_to_translate', models.CharField(max_length=10000)),
                ('translated_text', models.CharField(max_length=12000)),
            ],
        ),
    ]
