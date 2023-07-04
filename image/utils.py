import hashlib
from io import BytesIO
from typing import Optional
from PIL import Image as PIL_Image

from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Image, ResizedImage


def handle_resize(image: Image, new_width: int, new_height: Optional[int]):
    with image.file.open() as file:
        original_img = PIL_Image.open(file)
        width, height = original_img.size

        if not new_height:
            # если новой высоты нет, вычисляем по текущему соотношению сторон
            new_height = (height * new_width) / width

        # проверяем существование требуемого измененного файла
        existing_resized = ResizedImage.objects.filter(image_id=image.id, width=new_width, height=new_height)
        if existing_resized.exists():
            return existing_resized.first()

        resized_img = original_img.resize((new_width, round(new_height)), PIL_Image.NEAREST)

        # формируем имя файла
        md5_hash = hashlib.md5(b'{image.file.name}').hexdigest()
        image_name = f'{str(md5_hash)}_{new_width}x{new_height}.{original_img.format}'

        # формируем файл
        img_buffer = BytesIO()
        resized_img.save(img_buffer, format=original_img.format, quality=100)
        img_buffer.seek(0)
        uploaded_image = SimpleUploadedFile(name=image_name, content=img_buffer.getvalue())

        # создаем новую инстанцию
        resized_image = ResizedImage.objects.create(
            image_id=image.id,
            width=new_width,
            height=new_height,
        )
        resized_image.img.save(image_name, uploaded_image, save=True)

        return resized_image
