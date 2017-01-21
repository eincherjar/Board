from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone


class Notice(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    title = models.CharField(max_length=500, verbose_name="Tytuł")
    content = models.TextField(verbose_name="Treść")
    create_date = models.DateTimeField(verbose_name="Data publikacji", auto_now_add=True)
    notice_poster = models.FileField(verbose_name="Ścieżka do zdjęcia głównego", upload_to='Notice/%Y-%m-%d')
    notice_image1 = models.FileField(verbose_name="Ścieżka do zdjęcia", upload_to='Notice/%Y-%m-%d')
    notice_image2 = models.FileField(verbose_name="Ścieżka do zdjęcia", upload_to='Notice/%Y-%m-%d')
    notice_image3 = models.FileField(verbose_name="Ścieżka do zdjęcia", upload_to='Notice/%Y-%m-%d')
    notice_image4 = models.FileField(verbose_name="Ścieżka do zdjęcia", upload_to='Notice/%Y-%m-%d')

    def get_absolute_url(self):
        return reverse('board:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ogłoszenie'
        verbose_name_plural = 'Ogłoszenia'