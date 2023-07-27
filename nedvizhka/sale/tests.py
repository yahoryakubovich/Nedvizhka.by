from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Flat


class FlatListViewTestCase(TestCase):
    def setUp(self):
        # Создаем пользователя
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Создаем несколько объектов Flat с is_moderated=True и привязываем их к пользователю
        self.flat1 = Flat.objects.create(title='Flat 1', description='Description for Flat 1', is_moderated=True,
                                         creator=self.user, price=100000, number_of_rooms=3, floor_number=1,
                                         total_area=70,
                                         living_area=44.0, kitchen=14.0, year_of_construction=2018)
        self.flat2 = Flat.objects.create(title='Flat 2', description='Description for Flat 2', is_moderated=True,
                                         creator=self.user, price=100000, number_of_rooms=3, floor_number=1,
                                         total_area=70,
                                         living_area=44.0, kitchen=14.0, year_of_construction=2018)
        self.flat3 = Flat.objects.create(title='Flat 3', description='Description for Flat 3', is_moderated=False,
                                         creator=self.user, price=100000, number_of_rooms=3, floor_number=1,
                                         total_area=70,
                                         living_area=44.0, kitchen=14.0, year_of_construction=2018)

    def test_flat_list_view(self):
        # Входим в систему как созданный пользователь
        self.client.login(username='testuser', password='testpassword')

        # Получаем URL для просмотра списка квартир
        url = reverse('flat')

        # Отправляем GET-запрос к URL
        response = self.client.get(url)

        # Проверяем, что ответ имеет код 200 (успех)
        self.assertEqual(response.status_code, 200)

        # Проверяем, что выводятся только квартиры с is_moderated=True
        self.assertContains(response, self.flat1.title)
        self.assertContains(response, self.flat2.title)
        self.assertNotContains(response, self.flat3.title)


class FlatDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        # Создание тестового объекта Flat
        self.flat = Flat.objects.create(title='Flat 1', description='Description for Flat 1', is_moderated=True,
                                        creator=self.user, price=100000, number_of_rooms=3, floor_number=1,
                                        total_area=70, living_area=44.0, kitchen=14.0, year_of_construction=2018)

    def test_flat_detail_view(self):
        # Получение URL для просмотра деталей квартиры
        url = reverse("flat", args=[self.flat.pk])
        response = self.client.get(url)

        # Проверка, что запрос завершился успешно
        self.assertEqual(response.status_code, 200)

        # Проверка, что используется правильный шаблон
        self.assertTemplateUsed(response, "flatdetailview.html")

        # Проверка, что данные объекта Flat отображаются на странице
        self.assertContains(response, self.flat.title)
        self.assertContains(response, self.flat.description)
        self.assertContains(response, str(self.flat.total_area))
        self.assertContains(response, self.flat.address)
