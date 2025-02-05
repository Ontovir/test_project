*UI Тестирование главной страницы Effective-Mobile*
—Описание проекта
Этот проект содержит автоматизированные UI-тесты для главной страницы сайта Effective-Mobile.
Тесты проверяют переход по основным разделам (О нас, Контакты и пр.) и соответствие URL-адресов.

—Используемые технологии
Python 3.10
Playwright (для UI тестирования)
Allure (для отчетов)
Docker (для контейнеризации тестов)

—Установка и запуск
1. Установка зависимостей
Убедитесь, что у вас установлен Python 3.10.
Затем установите зависимости:

pip install -r requirements.txt

Важно: Перед запуском убедитесь, что у вас установлен Playwright и браузеры:

playwright install

2. Запуск тестов
Для запуска тестов локально:

pytest --alluredir=allure-results

После выполнения тестов можно сгенерировать отчет:

allure serve allure-results

—Запуск тестов в Docker
1. Сборка Docker-образа

docker build -t ui-tests .

2. Запуск контейнера с тестами

docker run --rm ui-tests

3. Генерация отчета
После выполнения тестов выгрузите отчет:

docker cp <container_id>:/app/allure-results ./allure-results
allure serve allure-results

—Структура проекта
test_project/
┣ pages/             # Page Object Model (POM) для UI тестов
┣ tests/             # Тесты на Playwright
┣ allure-results/    # Результаты Allure
┣ Dockerfile         # Файл для сборки контейнера
┣ requirements.txt   # Зависимости проекта
┣ README.md          # Этот файл

[Дополнительно]
*Следуйте лучшим практикам при написании автотестов.
*Код оформлен по Page Object Model (POM).
*Используется Allure для удобного просмотра отчетов.

