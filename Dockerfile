FROM python:3.11-slim

ARG DEBIAN_FRONTEND=noninteractive
ARG DEBCONF_NOWARNINGS="yes"

COPY poetry.lock pyproject.toml /app/

WORKDIR /app

RUN apt-get update \
    && apt-get -qq install \
      git \
    && mkdir -p -m 0600 ~/.ssh \
    && ssh-keyscan github.com >> ~/.ssh/known_hosts \
    && pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false
RUN --mount=type=ssh poetry install --no-root
    # clean
RUN rm -rf /root/.cache \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -qq autoremove \
    && apt-get clean

COPY . /app
RUN --mount=type=ssh poetry install


ENV PYTHONUNBUFFERED 1

EXPOSE 8080
ENTRYPOINT [ "/app/entrypoint.sh" ]
CMD ["sleep", "infinity"]
