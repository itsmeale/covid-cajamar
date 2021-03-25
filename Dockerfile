FROM ubuntu:20.04

ENV POETRY_VERSION 1.1.5

COPY . /app
WORKDIR /app

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends software-properties-common make \
    && add-apt-repository -y ppa:deadsnakes \
    && apt-get install -y --no-install-recommends python3.8-dev python3-pip wget \
    && pip3 install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev \
    && pip3 uninstall --yes poetry

EXPOSE 8501

CMD ["scripts/startapp"]