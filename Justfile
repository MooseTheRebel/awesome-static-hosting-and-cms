# Show available commands
default:
    @just --list

# Install dependencies and make app.py executable
install:
    uv sync
    chmod +x app.py

# Run local development server (requires .env)
dev:
    uv run --env-file .env coltrane play

# Build static site (requires .env)
build:
    uv run --env-file .env coltrane record

# Clean build output
clean:
    rm -rf output/

# Bootstrap: copy .env.example to .env if it doesn't exist, then install
bootstrap:
    #!/usr/bin/env bash
    if [ ! -f .env ]; then
        cp .env.example .env
        echo "Created .env from .env.example — update SECRET_KEY before deploying."
    fi
    just install
