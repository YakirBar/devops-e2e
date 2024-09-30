FROM python:3.8-slim

RUN pip install selenium

WORKDIR /app

COPY . .

CMD ["python", "isAlive.py"]