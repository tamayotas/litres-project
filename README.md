# Проект по тестированию сервиса электронных и аудиокниг [Литрес](https://www.litres.ru")</h1>


![This is an image](resources/images/ui/main_page_litres.png)

<h3> Список проверок, реализованных в автотестах:</h3>

### UI-тесты

- [x] Авторизация пользователя на сайте(успешная и неуспешная)
- [x] Поиск книги(успешный и неуспешный)
- [x] Регистрация нового пользователя на сайте(успешная и неуспешная)
- [x] Проверка отображения страницы о компании

### Проект реализован с использованием:

<img src="resources/images/logo/python.svg" width="50"> <img src="resources/images/logo/pytest.png" width="50"> <img src="resources/images/logo/pycharm.png" width="50"> <img src="resources/images/logo/selene.png" width="50"> <img src="resources/images/logo/selenoid.png" width="50"> <img src="resources/images/logo/jenkins.png" width="50"> <img src="resources/images/logo/Allure.svg" width="50"> <img src="resources/images/logo/Allure_TO.svg" width="50"> <img src="resources/images/logo/telegram.svg" width="50"> <img src="resources/images/logo/jira.svg" width="50">

----

### Локальный запуск

1. Клонируйте репозиторий на свой локальный компьютер при помощи git clone
2. Создайте и активируйте виртуальное окружение

  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```

3. Установите зависимости с помощью pip

  ```bash
  pip install -r requirements.txt
  ```

4. Для запусков тестов локально используйте команды:

  ```bash
  pytest .
  ```

Получение отчёта allure:

```bash
allure serve allure-results
```

----

### Удаленный запуск автотестов выполняется на сервере Jenkins

> <a target="_blank" href="https://jenkins.autotests.cloud/job/litres-project/">Ссылка на проект в Jenkins</a>

### Параметры сборки
Данные параметры не обязательны для заполнения.

* `ENVIRONMENT` - параметр определяет окружение для запуска тестов, по умолчанию DEV
* `COMMENT` - комментарий к сборке
* `BROWSER_NAME` - выбор браузера для запуска тестов, по умолчанию chrome
* `BROWSER_VERSION` - выбор версии браузера для запуска тестов, по умолчанию 100.0

![This is an image](resources/images/ui/jenkins_run.PNG)

### Запуск автотестов в Jenkins

#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/litres-project/">проект</a>

![This is an image](resources/images/ui/jenkins.PNG)

#### 2. Выбрать пункт **Build with Parameters**

#### 3. Внести изменения в конфигурации сборки, при необходимости

#### 4. Нажать **Build**

#### 5. Результат запуска сборки можно посмотреть в классическом формате Allure Results

----

### Allure отчет

#### Общие результаты

![This is an image](resources/images/ui/allure.PNG)

----

### Интеграция с Allure TestOps

> <a target="_blank" href="https://allure.autotests.cloud/project/4083/dashboards">Ссылка на проект в
> AllureTestOps</a> (запрос доступа `admin@qa.guru`)

#### Список всех кейсов, имеющихся в проекте

![This is an image](resources/images/ui/allure_testops.PNG)

#### Отображение результатов прогона тестов

![This is an image](resources/images/ui/testops.PNG)

----

### Интеграция с Jira

> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1128">Ссылка на проект в Jira</a>

![This is an image](resources/images/ui/jira.png)

----

### Оповещение о результатах прогона тестов в Telegram

![This is an image](resources/images/ui/telegram.PNG)

----

### Пример видео прохождения автотеста

![autotest_gif](resources/images/ui/video.gif)


