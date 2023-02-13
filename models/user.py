#!/usr/bin/env python3
""" The module creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
