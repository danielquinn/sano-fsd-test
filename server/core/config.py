import json
import logging
import os

import boto3

config = {
    # SHARED CONFIG
    "token_expiration_seconds": 5 * 60,  # 5 minutes
    "refresh_expiration_seconds": 2 * 60 * 60,  # 2 hours
    "reset_token_duration_in_seconds": 10 * 60,  # 10 minutes
    "validation_token_duration_in_seconds": 86400,  # 1 day
    "connection_string": os.getenv("DATABASE_CONNECTION"),
    "jwt_secret": os.getenv("JWT_SECRET"),
    "secret_salt": os.getenv("SALT_SECRET"),
    "base_url": os.getenv("BASE_URL")
}
