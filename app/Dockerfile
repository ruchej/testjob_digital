###########
# BUILDER #
###########

FROM python:3.10.5 as builder

WORKDIR /usr/src/app

LABEL Author="Aleksandr Vinogradov"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED 1


RUN pip install --upgrade pip \
    && pip install poetry

COPY poetry.lock pyproject.toml /usr/src/app

RUN poetry export -f requirements.txt --output requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

COPY . /usr/src/app


#########
# FINAL #
#########

FROM python:3.10.5


RUN apt-get update \
    && apt-get install -y netcat \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/app
RUN addgroup app && adduser --ingroup app app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

RUN mkdir $APP_HOME

WORKDIR $APP_HOME

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY ./entrypoint.sh $APP_HOME
COPY . $APP_HOME

RUN chown -R app:app $APP_HOME

USER app

ENTRYPOINT ["/home/app/web/entrypoint.sh"]
