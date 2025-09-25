import json
import base64

class LambdaEventHelper:
    @staticmethod
    def parse_body(event):
        body = {}
        body_content = event.get('body')
        if isinstance(body_content, str):
            try:
                body = json.loads(body_content) if body_content else {}
            except json.JSONDecodeError:
                body = {}
        else:
            body = body_content or {}
        return body

