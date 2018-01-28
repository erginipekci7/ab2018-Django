from django.db import models

class Survey(models.Model):
    name = models.CharField('Araştırma Adı', max_length=100)
    active = models.BooleanField('Aktif mi?', null=False, blank=False, default=False)
    created_at = models.DateTimeField('Oluşturulma Tarihi', null=True, blank=True, auto_now=True)
    updated_at = models.DateTimeField('Güncellenme Tarihi', null=True, blank=True, auto_now_add=True)

    class Meta:
        verbose_name = 'Araştırma'
        verbose_name_plural = 'Araştırmalar'

    def __str__(self):
        return str(self.name)
#Survey class ını cağırmak için onun altında olmalı
class Question(models.Model):
    survey = models.ForeignKey(Survey, verbose_name='Araştırma', null=False, blank=False)
    title = models.CharField('Soru Başlığı', max_length=100)
    choice_one = models.CharField('1. Seçenek', max_length=100, blank=True)
    choice_two = models.CharField('2. Seçenek', max_length=100, blank=True)
    choice_three = models.CharField('3. Seçenek', max_length=100, blank=True)
    choice_four = models.CharField('4. Seçenek', max_length=100, blank=True)


    class Meta:
        verbose_name = 'Soru'
        verbose_name_plural = 'Sorular'
    def __str__(self):
        return str(self.title)
