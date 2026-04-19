# Show available commands
default:
    @just --list

# Install dependencies and make app.py executable
install:
    cd github_site && uv sync
    chmod +x github_site/app.py

# Run local development server (requires github_site/.env)
dev:
    cd github_site && uv run --env-file .env python app.py build_directory
    cd github_site && uv run --env-file .env coltrane play

# Build static site (requires github_site/.env)
build:
    cd github_site && uv run --env-file .env python app.py build_directory
    cd github_site && uv run --env-file .env coltrane record

# Clean build output
clean:
    rm -rf github_site/output/

# Bootstrap: copy .env.example to .env if it doesn't exist, then install
bootstrap:
    #!/usr/bin/env bash
    if [ ! -f github_site/.env ]; then
        cp github_site/.env.example github_site/.env
        echo "Created github_site/.env from .env.example — update SECRET_KEY before deploying."
    fi
    just install

# Sort `[[providers]]` and `[[systems]]` entries by name
sort-toml:
    uv run python tools/sort_toml.py

# Verify TOML entries are sorted (CI-friendly; exit 1 if not)
check-toml:
    uv run python tools/sort_toml.py --check
