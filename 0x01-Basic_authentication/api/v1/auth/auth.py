#!/usr/bin/env python3
"""Module - auth.py"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    """The authentication class"""
    def requires_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """The required authentication method"""
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_headers(self, request=None) -> str:
        """The authorization headers method"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """The current user method"""
        return None
