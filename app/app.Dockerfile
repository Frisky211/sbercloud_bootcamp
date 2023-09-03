FROM python:3.10-bullseye

WORKDIR /app
COPY app.py ./
RUN pip install --no-cache-dir flask
EXPOSE 8000

CMD ["python3", "app.py"]
