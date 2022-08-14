import json

from flask import Flask, Response


class FlaskApp(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_handler()

    def register_handler(self):
        def known_except(e):
            return Response(
                response=json.dumps({"errors": e.errors, "msg": e.msg}),
                status=e.code,
                mimetype="application/json",
            )

    def ready(self):
        pass


app = FlaskApp(__name__)
