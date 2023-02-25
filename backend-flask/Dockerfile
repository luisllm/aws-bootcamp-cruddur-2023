FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE ${PORT}
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
ADD start-flask.sh /root/start-flask.sh
RUN chmod +x /root/start-flask.sh
ENTRYPOINT ["/root/start-flask.sh"]