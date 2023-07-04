from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework import status

from .serializers import ImageSerializer, ResizedImageSerializer
from .models import Image
from .utils import handle_resize


class ImageAPIView(APIView):
    """
    API для обработки загруженных изображений
    принимает метод POST
    """

    permission_classes = [AllowAny, ]
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            try:
                width = serializer.validated_data.get("width")
                height = serializer.validated_data.get("height", None)
                file = serializer.validated_data.pop("file")

                # проверка на уже загруженный исходный файл
                image_qs = Image.objects.filter(filename=file.name)
                if image_qs.exists():
                    image = image_qs.first()
                else:
                    image = Image.objects.create(file=file)

                # изменение размера и создание инстанции измененного изображения
                new_image = handle_resize(image, int(width), int(height))
                return Response(
                    ResizedImageSerializer(
                        new_image,
                        context={"request": request},
                    ).data,
                    status=status.HTTP_200_OK,
                )

            except Exception as exc:
                return Response({"Error": str(exc)})

        else:
            return Response({"Error": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)