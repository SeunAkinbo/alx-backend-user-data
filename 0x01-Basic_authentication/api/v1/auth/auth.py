#!/usr/bin/ env python3
"""Module - auth.py"""
from flask import request
from typing import List, TypeVar


class Auth:
    """The authentication class"""
    def requires_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """The required authentication method"""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_headers(self, request=None) -> str:
        """The authorization headers method"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """The current user method"""
        return None
