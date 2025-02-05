FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install  # Установка браузеров Playwright

COPY . .

CMD ["pytest", "--alluredir=allure-results"]