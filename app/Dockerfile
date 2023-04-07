FROM python:3.9.10-alpine3.14
WORKDIR /srv
RUN pip install --upgrade pip
RUN pip install flask==2.2.3 flask-sqlalchemy==3.0.3 flask-login==0.6.2 wtforms==3.0.1 wtforms_alchemy==0.18.0
COPY . /srv
ENV FLASK_APP=app
CMD ["python","run.py"]