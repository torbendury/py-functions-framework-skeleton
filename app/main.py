import functions_framework
from flask import Request, Response


@functions_framework.http
def entrypoint(request: Request) -> Response:
    args = request.args
    if len(args) > 0 and "name" in args:
        return f"Hello {args['name']}", 200
    else:
        return "Hello stranger", 200
