FROM python:3.14.5-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "calculator.py"]
