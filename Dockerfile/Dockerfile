FROM python:3.8


COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /code

COPY app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]