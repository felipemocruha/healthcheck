SHELL:= /bin/bash

build:
	docker-compose build

deploy:
	docker stack deploy -c docker-compose.yml --with-registry-auth proteus

.PHONY: build deploy
