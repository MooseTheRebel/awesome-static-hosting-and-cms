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

# Preview a PR locally using a git worktree (requires gh CLI).
# Usage: just preview-pr <PR_number> [no-serve=1] [keep-dir=1]
#   no-serve=1  — build only, skip launching the dev server
#   keep-dir=1  — keep the worktree directory after exit (default: clean up)
preview-pr pr_number no_serve='' keep_dir='':
    #!/usr/bin/env bash
    set -euo pipefail
    worktree_path="/tmp/ashc-preview-{{pr_number}}"
    cleanup() {
        if [ -z "{{keep_dir}}" ]; then
            echo "Cleaning up worktree at $worktree_path..."
            git worktree remove --force "$worktree_path" 2>/dev/null || true
        else
            echo "Keeping worktree at $worktree_path"
        fi
    }
    trap cleanup EXIT
    main_root="$(git rev-parse --show-toplevel)"
    echo "Creating worktree at $worktree_path..."
    git worktree add "$worktree_path" HEAD
    cd "$worktree_path"
    git fetch origin pull/{{pr_number}}/head
    git checkout FETCH_HEAD
    # Copy .env into the worktree, falling back to .env.example
    if [ -f "$main_root/github_site/.env" ]; then
        cp "$main_root/github_site/.env" "$worktree_path/github_site/.env"
    else
        cp "$worktree_path/github_site/.env.example" "$worktree_path/github_site/.env"
        echo "Note: no .env found in main worktree; using .env.example defaults."
    fi
    cd "$worktree_path/github_site"
    uv sync
    uv run --env-file .env python app.py build_directory
    if [ -z "{{no_serve}}" ]; then
        uv run --env-file .env coltrane play
    else
        uv run --env-file .env coltrane record
        echo "Build complete. Output at $worktree_path/github_site/output/"
    fi

# Sort `[[providers]]` and `[[systems]]` entries by name
# Dependencies declared via PEP 723 inline script metadata in tools/sort_toml.py.
sort-toml:
    uv run tools/sort_toml.py

# Verify TOML entries are sorted (CI-friendly; exit 1 if not)
check-toml:
    uv run tools/sort_toml.py --check
