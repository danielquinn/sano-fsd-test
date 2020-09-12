FROM node:12

COPY . /app

RUN \
  cd /app && \
  npm ci && \
  npm install

CMD ["run/client"]
