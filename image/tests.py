import shutil

from rest_framework.test import APITestCase
from django.test import Client
from django.urls import reverse
from django.test import override_settings

from resizer_api.settings import MEDIA_ROOT


@override_settings(MEDIA_ROOT=(MEDIA_ROOT+"_test"))
class ImageAPIView(APITestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('image:resize')

    def test_upload_image(self):
        with open("media_test/slowpoke.png", "rb") as image_test_file:
            with self.assertNumQueries(5):
                response = self.client.post(self.url, {'file': image_test_file, "width": 100, "height": 40})

            response_data = response.json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(1, len(response_data))
            self.assertIn("d4db41dc09d80337f59ad1e9623befaa_100x40", response_data["url"])

    def test_float_width(self):
        with open("media_test/slowpoke.png", "rb") as image_test_file:
            response = self.client.post(self.url, {'file': image_test_file, "width": 100.5, "height": 40})

            response_data = response.json()
            self.assertEqual(response.status_code, 400)
            self.assertEqual(1, len(response_data))
            self.assertIn("A valid integer is required", response_data["Error"])

    def test_without_image(self):
        response = self.client.post(self.url, {"width": 100, "height": 40})

        response_data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(1, len(response_data))
        self.assertIn("No file was submitted", response_data["Error"])

    def test_wrong_format(self):
        with open("media_test/hello.txt", "rb") as wrong_test_file:
            response = self.client.post(self.url, {"file": wrong_test_file, "width": 100, "height": 40})

            response_data = response.json()
            self.assertEqual(response.status_code, 400)
            self.assertEqual(1, len(response_data))
            self.assertIn("The file you uploaded was either not an image or a corrupted image", response_data["Error"])

    def tearDown(self):
        print("Deleting temporary files...")
        try:
            shutil.rmtree(f'{MEDIA_ROOT}_test/images')
            shutil.rmtree(f'{MEDIA_ROOT}_test/resized_images')
        except OSError:
            pass
