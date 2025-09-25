import requests
import base64

class NegotiateAuth(requests.auth.AuthBase):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.auth_attempts = 0

    def __call__(self, r):
        if self.auth_attempts == 0:
            # First attempt without auth header
            self.auth_attempts += 1
            return r
        
        # On subsequent attempts, add basic credentials
        # encoded in Negotiate format
        if self.username and self.password:
            auth_string = f"{self.username}:{self.password}"
            encoded = base64.b64encode(auth_string.encode()).decode()
            r.headers['Authorization'] = f'Negotiate {encoded}'
        
        return r