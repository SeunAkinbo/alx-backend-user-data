#!/usr/bin/env python3
"""Module - session_auth
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """Session Authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a new session"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """User id for session method"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Current user method

        Args:
            request: Flask request object
        Returns:
            User object if session ID is valid else None
        """
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None):
        """Delete user session on logout"""
        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        self.user_id_by_session_id.pop(session_id)
        return True
