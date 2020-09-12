FROM python:3.8

COPY . /app

RUN \
  apt-get update && \
  apt-get install -y \
    netcat \
    postgresql-client

RUN \
  cd /app && \
  pip download -r requirements.txt

RUN \
  cd /app && \
  pip install -r requirements.txt

ENTRYPOINT ["/app/entrypoint"]

CMD ["/app/run/server"]
