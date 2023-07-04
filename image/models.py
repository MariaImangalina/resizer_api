from django.db import models


class Image(models.Model):
    """
    Модель для хранения оригинального изображения
    """
    file = models.ImageField("Изображение", upload_to='images')
    filename = models.CharField("Название файла", blank=True, max_length=255)

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        # если инстанция сохраняется впервые присваиваем имя файла полю "filename"
        if not self.pk:
            self.filename = self.file.name
        super().save(*args, **kwargs)


class ResizedImage(models.Model):
    """
    Модель для хранения измененного изображения
    """
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='resized_images')
    img = models.ImageField("Изображение", upload_to='resized_images')
    width = models.IntegerField("Ширина изображения")
    height = models.IntegerField("Высота изображения", null=True)

    def __str__(self):
        return self.img.name
