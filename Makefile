#SHELL := /bin/sh

start:  ## Start local Docker environment
	@echo "\nStarting container.. 🐳"
	docker-compose up -d
.PHONY: start

stop:  ## Stop local Docker environment
	@echo "\nStopping container.. 👋" && \
	docker-compose stop
.PHONY: stop