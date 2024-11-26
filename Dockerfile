FROM python:3.12

WORKDIR /app/src

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./src /app/src

CMD ["python", "main.py"]
