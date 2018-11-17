# LabWork-2
[![Python](https://img.shields.io/badge/python-3.6.5-green.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-2.1.1-orange.svg)](https://www.djangoproject.com/)


Лабораторная работа №2 по учебному курсу "Языки и методы программирования"

Данное приложение представляет собой веб-сервис, предназначенный для чтения RSS.
Пользователи имеют возможность добавлять RSS, искать по ключивым словам, разделять источники по категориям.

## Начало работы

Эта инструкция расскажет о том, как установить проект и начать с ним работу.

### Предварительные настройки

Прежде всего необходимо установить Django и requests 

``` 
pip install Django
pip install requests 
```

### Установка

Копируем репозиторий

```
git clone https://github.com/DarinaKuzmina/LabWork-2
```
Переходим в корень

```
cd LabWork-2
```

И запускаем сервер

```
python3 manage.py runserver
```

Теперь можно перейти по ссылке и начинать работу

```
http://127.0.0.1:8000/
```

## Использовано в работе

* [Django](https://www.djangoproject.com) - Фреймворк для веб-приложений на языке Python.
* [Uikit](https://getuikit.com/) - Интерфейсный фреймворк для разработки веб-интерфейсов.

## Автор

* **Кузьмина Дарина** - ПМ-1701 - [DarinaKuzmina](https://github.com/DarinaKuzmina)

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности смотрите в файле [LICENSE](LICENSE).
