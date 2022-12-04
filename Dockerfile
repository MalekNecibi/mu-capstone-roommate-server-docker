FROM python:3.10

# WORKDIR /

# RUN pip3 install --upgrade pip3
COPY ./requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt --root-user-action=ignore


COPY /app/ app/
WORKDIR ./app

# to get a string like this run:
# openssl rand -hex 32
ENV JWT_SECRET_KEY "764cdebf12deb87ffb16918fbd5074bc990466aed2eb248e562e341b7b96109c" 

ENV MONGODB_URL "mongodb+srv://GenericUser:Bunkiez@bunkiesv1.jzrjtev.mongodb.net/BunkiesV1"

ENTRYPOINT [ "/usr/local/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "15400" ]




