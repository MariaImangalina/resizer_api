from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from .models import ResizedImage


class ImageSerializer(serializers.Serializer):
    """
    Сериализатор для загрузки исходных данных
    :param file - оригинальный файл
    :param width - ширина будущего измененного файла
    :param height - высота будущего измененного файла, опционально
    """
    file = serializers.ImageField(validators=[FileExtensionValidator(["svg", "jpg", "jpeg", "png"])])
    width = serializers.IntegerField(allow_null=False, required=True, write_only=True)
    height = serializers.IntegerField(allow_null=False, required=False, write_only=True)

    class Meta:
        fields = ('file', 'width', 'height')


class ResizedImageSerializer(serializers.ModelSerializer):
    """
    Сериализатор для возвращения измененного файла
    :param url - ссылка на измененный файл
    """
    url = serializers.SerializerMethodField()

    class Meta:
        model = ResizedImage
        fields = ('url', )

    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.img.url)

