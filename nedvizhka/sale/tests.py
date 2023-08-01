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


class FlatUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.flat = Flat.objects.create(title='Flat 2', description='Description for Flat 2', is_moderated=True,
                                        creator=self.user, price=100000, number_of_rooms=3, floor_number=1,
                                        total_area=70,
                                        living_area=44.0, kitchen=14.0, year_of_construction=2018)
        self.url = reverse('edit_flat', kwargs={'pk': self.flat.pk})

    def test_view_requires_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_view_uses_correct_template(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')

    def test_view_shows_correct_data_in_form(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        form = response.context['form']
        self.assertEqual(form['title'].value(), self.flat.title)
        self.assertEqual(form['description'].value(), self.flat.description)
        self.assertEqual(form['price'].value(), self.flat.price)
        self.assertEqual(form['number_of_rooms'].value(), self.flat.number_of_rooms)
        self.assertEqual(form['floor_number'].value(), self.flat.floor_number)
        self.assertEqual(form['total_area'].value(), self.flat.total_area)
        self.assertEqual(form['living_area'].value(), self.flat.living_area)
        self.assertEqual(form['kitchen'].value(), self.flat.kitchen)
        self.assertEqual(form['year_of_construction'].value(), self.flat.year_of_construction)

    def test_view_updates_object_after_successful_form_submission(
            self):  # чтобы этот тест заработал надо убрать модерацию т.к при update is_moderated != True
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'Updated Flat',
            'description': 'Updated Description',
            'price': 120000,
            'number_of_rooms': 2,
            'floor_number': 2,
            'total_area': 80,
            'living_area': 50.0,
            'kitchen': 15.0,
            'year_of_construction': 2019,
            'is_moderated': True
        }
        response = self.client.post(self.url, data)
        self.flat.refresh_from_db()  # Обновляем объект из базы данных
        self.assertEqual(self.flat.title, 'Updated Flat')
        self.assertEqual(self.flat.description, 'Updated Description')
        self.assertEqual(self.flat.price, 120000)
        self.assertEqual(self.flat.number_of_rooms, 2)
        self.assertEqual(self.flat.floor_number, 2)
        self.assertEqual(self.flat.total_area, 80)
        self.assertEqual(self.flat.living_area, 50.0)
        self.assertEqual(self.flat.kitchen, 15.0)
        self.assertEqual(self.flat.year_of_construction, 2019)

    def test_view_redirects_to_profile_after_successful_form_submission(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'Updated Flat',
            'description': 'Updated Description',
            'price': 120000,
            'number_of_rooms': 2,
            'floor_number': 2,
            'total_area': 80,
            'living_area': 50.0,
            'kitchen': 15.0,
            'year_of_construction': 2019,
            'is_moderated': True
        }


class FlatDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.flat = Flat.objects.create(title='Flat 1', description='Description for Flat 1', is_moderated=True,
                                        creator=self.user, price=100000, number_of_rooms=3, floor_number=1,
                                        total_area=70, living_area=44.0, kitchen=14.0, year_of_construction=2018)
        self.url = reverse('delete_flat', kwargs={'pk': self.flat.pk})

    def test_view_requires_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  # Redirect to login page

    def test_view_redirects_after_successful_delete(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)  # Redirect to success_url

    def test_view_deletes_object(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.url)
        self.assertFalse(Flat.objects.filter(pk=self.flat.pk).exists())

    def test_view_redirects_to_profile_after_successful_delete(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.url)
        self.assertRedirects(response, reverse('profile'))
