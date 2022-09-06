from django.db import models

# Create your models here.
class TranslateModel(models.Model):
    LANGUAGES = [
    ('ar', 'arabic'),
    ('az', 'azerbaijani'),('zh-cn', 'chinese (simplified)'),
    ('hr', 'croatian'),
    ('cs', 'czech'), ('da', 'danish'),('en', 'english'),
    ('fr', 'french'),('de', 'german'),
    ('el', 'greek'),('it', 'italian'), ('ja', 'japanese'),
    ('pl', 'polish'), ('pt', 'portuguese'),('ru', 'russian'),('es', 'spanish'),
    ('tr', 'turkish'),('uz', 'uzbek')]
    language_to_translate = models.CharField(max_length=20,choices=LANGUAGES,default='en')
    language_to_be_translated = models.CharField(max_length=20,choices=LANGUAGES,default='ru')
    text_to_translate = models.CharField(max_length=10000)
    translated_text = models.CharField(max_length=12000)
    
    def __str__(self):
        return f'"{self.text_to_translate[:20]}..." [{self.language_to_translate}] --> "{self.translated_text[:20]}..." [{self.language_to_be_translated}]. '
    
    