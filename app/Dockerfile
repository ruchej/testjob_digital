###########
# BUILDER #
###########

FROM python:3.10.5-slim as builder

WORKDIR /usr/src/app

LABEL Author="Aleksandr Vinogradov"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED 1


RUN pip install --upgrade pip \
    && pip install poetry

COPY poetry.lock pyproject.toml /usr/src/app

RUN poetry export -f requirements.txt --output requirements.txt


#########
# FINAL #
#########

FROM python:3.10.5-slim


RUN apt-get update \
    && apt-get install -y netcat \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/app
RUN addgroup app && adduser --ingroup app app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

RUN mkdir $APP_HOME

WORKDIR $APP_HOME

COPY --chown=app:app . $APP_HOME
COPY --chown=app:app --from=builder /usr/src/app/requirements.txt .

RUN pip install -r requirements.txt

RUN chown app:app $APP_HOME

COPY --chown=app:app ./entrypoint.sh $APP_HOME

USER app

RUN mkdir $APP_HOME/static

ENTRYPOINT ["/home/app/web/entrypoint.sh"]
