#!/usr/bin/env python

import os
import sys

import coltrane

application = coltrane.initialize(
    SECRET_KEY=os.environ.get("SECRET_KEY", "dev-insecure-secret-key-change-in-production"),
    DEBUG=os.environ.get("DEBUG", "True") == "True",
    ALLOWED_HOSTS=os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(","),
    COLTRANE_SITE_URL=os.environ.get("COLTRANE_SITE_URL", "http://localhost:8000"),
    COLTRANE_TITLE=os.environ.get("COLTRANE_TITLE", "Awesome Static Hosting and CMS"),
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
