FROM python:3

RUN apt-get update -y

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

# RUN pip install flask

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]
