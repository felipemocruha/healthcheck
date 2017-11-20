FROM alpine:3.6

RUN apk --update --no-cache add redis tzdata \
    && cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
    && echo "America/Sao_Paulo" > /etc/timezone

CMD redis-server --protected-mode no
