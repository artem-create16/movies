FROM python:3.8

WORKDIR /usr/src/app
ADD . /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

#CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "movies.wsgi:application"]
CMD gunicorn --bind 0.0.0.0:$PORT movies.wsgi:application