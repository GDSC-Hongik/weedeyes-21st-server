# users/authentication_backends.py

from django.contrib.auth.backends import BaseBackend
from firebase_admin import auth

class FirebaseAuthenticationBackend(BaseBackend):
    def authenticate(self, request, uid=None, **kwargs):
        try:
            user = auth.get_user(uid)
            return user
        except auth.AuthError:
            return None

    def get_user(self, user_id):
        # 사용자 ID로 사용자 가져오기 (이 예제에서는 사용하지 않음)
        pass
