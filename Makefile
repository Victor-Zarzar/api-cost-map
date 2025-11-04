# Makefile API Cost Map
DOCKER_IMAGE_NAME = api-cost-map
DOCKER_CONTAINER_NAME = cost-map-api
PORT = 8000
DEV_COMPOSE = docker-compose.dev.yaml


build-dev:
	@echo "Building development image dev..."
	docker compose -f $(DEV_COMPOSE) build

up-dev:
	@echo "Uploading development environment on port $(PORT)..."
	docker compose -f $(DEV_COMPOSE) up	

down-dev:
	@echo "Stopping server..."
	docker compose -f $(DEV_COMPOSE) down
	@echo "Server stopped."

logs-dev:
	@echo "Development environment logs..."
	docker compose -f $(DEV_COMPOSE) logs -f	

test:
	@echo "Running tests..."
	docker compose -f $(DEV_COMPOSE) exec web pytest
	@echo "Tests completed."

clean:
	@echo "Cleaning local environment..."
	@docker compose -f $(DEV_COMPOSE) down -v --remove-orphans 2>/dev/null || true
	@docker compose -f $(PROD_COMPOSE) down -v --remove-orphans 2>/dev/null || true
	@docker images -q "api-cost-map*" | xargs -r docker rmi -f 2>/dev/null || true
	@docker system prune -f --volumes 2>/dev/null || true
	@docker builder prune -f 2>/dev/null || true
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@find . -name "*.pyc" -type f -delete 2>/dev/null || true
	@rm -rf .pytest_cache .coverage htmlcov 2>/dev/null || true
	@echo "Environment cleaned."