FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV FILES_DIR=/files
VOLUME /files

EXPOSE 5000

CMD ["python", "run.py"]
