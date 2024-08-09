#!/usr/bin/env python3
""" SessionDBAuth module
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class to manage session with database storage"""

    def create_session(self, user_id=None):
        """Create and store a new session in the database"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None

        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Return the User ID associated with a given session ID"""
        if session_id is None:
            return None

        user_session = UserSession.search({'session_id': session_id})
        if not user_session:
            return None

        return user_session[0].user_id

    def destroy_session(self, request=None):
        """Destroy the session (logout)"""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        user_session = UserSession.search({'session_id': session_id})
        if not user_session:
            return False

        user_session[0].remove()
        return True
