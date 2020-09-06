FROM python:3

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# create user
RUN groupadd chalusr
RUN useradd -ms /bin/bash -g chalusr chalusr

COPY ./src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .
RUN chmod 775 ./server.py

USER chalusr
CMD [ "python3", "./server.py" ]

