FROM alpine:3.6 as base

COPY requirements.txt /
RUN apk update && apk add --no-cache --virtual build-deps \
	linux-headers \
	gcc \
	g++ \
	build-base \
	python3-dev \
	&& apk add --no-cache \
	   ca-certificates \
	   python3 \
	   tzdata \
	   libffi-dev \
	   openssl-dev \
	&& cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
	&& echo "America/Sao_Paulo" > /etc/timezone \
	&& ln -s /usr/include/locale.h /usr/include/xlocale.h \
	&& pip3 install -r requirements.txt \
	&& mkdir -p /server \
	&& apk del build-deps

FROM base

COPY ./server /server/server
COPY ./scripts/start_server.sh /server
COPY ["./run.py", "./config/gunicorn_conf.py", "/server/"]

WORKDIR /server
