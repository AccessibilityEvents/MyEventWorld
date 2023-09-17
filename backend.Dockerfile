# dockerfile für backend -> excalidraw
FROM python:3.11.5-alpine3.18

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers

ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install flask flask-cors peewee load-dotenv

COPY utils.py server.py schemas.py database.db ./

EXPOSE 5000

CMD ["flask", "run"]
