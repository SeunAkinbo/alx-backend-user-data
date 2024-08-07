#!/usr/bin/ env python3
"""Module - auth.py"""
from flask import request
from typing import List, TypeVar


class Auth:
    """The authentication class"""
    def requires_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """The required authentication method"""
        return False

    def authorization_headers(self, request=None) -> str:
        """The authorization headers method"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """The current user method"""
        return None
