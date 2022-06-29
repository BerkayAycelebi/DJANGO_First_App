from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=100, verbose_name='Film Adı:')
    description = models.TextField(verbose_name='Açıklama:')
    image = models.CharField(max_length=50, verbose_name='Resim:')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi:')
    isPublihed=models.BooleanField(default=True, verbose_name='Yayında mı?')

    def __str__(self):
        return self.name
    def get_image_path(self):
        return '/img/'+self.image
