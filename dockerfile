FROM python:3-alpine

WORKDIR /app
ADD ./serverstarter.py /app/
ADD ./pessoa.py /app/
ADD ./templates/home.html /app/
ADD ./swagger.yml /app/

COPY requirements.txt ./
RUN pip install connexion[swagger-ui] -t .
RUN pip install --no-cache-dir -r requirements.txt -t .

EXPOSE 5000
#RUN python serverstarter.py
CMD [ "python3", "serverstarter.py" ]
