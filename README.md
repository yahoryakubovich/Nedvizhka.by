# Nedvizka.by - Сайт для продажи недвижимости

## О проекте
Nedvizka.by - это онлайн платформа, предназначенная исключительно для удобной и безопасной купли-продажи недвижимости. Сайт позволяет пользователям размещать объявления о продаже квартир, домов, офисов, складов и другой недвижимости.

### Основные возможности проекта:
- Регистрация и авторизация пользователей.
- Создание и редактирование объявлений о продаже недвижимости.
- Поиск и фильтрация объявлений по различным параметрам, таким как цена, район и т.д.
- Просмотр деталей объявления, включая все характеристики недвижимости и контактную информацию продавца.
- Управление объявлениями, возможность просматривать, редактировать и удалять свои собственные объявления.
- Возможность связаться с авторами объявлений, при нажатии на кнопку "Контакты" напрямую и получить более подробные сведения о предлагаемой недвижимости.

## Требования
Для работы с проектом вам понадобятся следующие зависимости:
- Python 3.11
- Django 4.2.3
- django-allauth 0.54.0
- Django Rest Framework (DRF)

## Установка
1. Склонируйте репозиторий проекта на свой локальный компьютер:
- git clone https://github.com/yahoryakubovich/Nedvizhka.by.git
3. Создайте и активируйте виртуальное окружение:
- poetry env use python3
- poetry shell
4. Установите необходимые зависимости из файла pyproject.toml:
- poetry install
5. Примените миграции базы данных:
- python manage.py migrate
5. Запустите сервер разработки:
- python manage.py runserver

## Использование
1. Откройте браузер и перейдите на страницу http://127.0.0.1:8000/ для просмотра сайта.
2. Для создания нового объявления, необходимо зарегистрироваться на сайте или авторизоваться, если у вас уже есть аккаунт.
3. После авторизации, нажмите на кнопку "Создать объявление" и заполните необходимую информацию о недвижимости.
4. Воспользуйтесь поиском и фильтрами, чтобы найти подходящие объявления.
5. Чтобы связаться с автором объявления, используйте кнопку "Контакты" или перейдите на страницу объявления.

## Разработка
Если вы хотите принять участие в разработке проекта, выполните следующие шаги:
1. Сделайте форк репозитория проекта на GitHub.
2. Создайте новую ветку для ваших изменений:
-git checkout -b feature-branch
3. Внесите необходимые изменения в код.
4. Создайте коммит и отправьте вашу ветку на GitHub:
- git commit -m "Add new feature"
- git push origin feature-branch
5. Откройте pull request на GitHub и опишите ваши изменения.

## Лицензия
Nedvizka.бай распространяется под лицензией MIT. Подробную информацию можно найти в файле LICENSE.

## Контакты
Если у вас возникли вопросы или предложения, вы можете связаться с нами по адресу: officialegoryakubovich@gmail.com

## Благодарности
Я хочу поблагодарить школу программирования TeachMeSkills, нашего преподавателя Дениса, нашего менеджера Тамару, всех участников моей группы Py83 за cовместную работу и поддержку.

## TODO
- Реализация контакта с продавцом непосредственно через сайт для получения дополнительной информации о недвижимости или оформления покупки.
- Система уведомлений, которая информирует пользователей о новых объявлениях, ответах на запросы и других важных событиях.
- Возможность оставлять отзывы о недвижимости и продавцах, а также ставить рейтинг объявлениям и продавцам.
- Адаптивный дизайн, чтобы корректно отображаться на различных устройствах, включая компьютеры, планшеты и смартфоны.
