start: 
	uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

# Local development
see-logs-local: start-local
	docker-compose logs -f

start-local:
	docker-compose up -d

stop-local:
	docker-compose down

restart-local: stop-local start-local

run-tests-local: start-local
	docker-compose run backend pytest