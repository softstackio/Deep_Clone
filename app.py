"""DeepClone UI mock. Serves a static page only; there is no processing backend."""

from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

STATIC_DIR = Path(__file__).parent / "static"
PORT = 8000


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)


if __name__ == "__main__":
    print(f"DeepClone UI running at http://localhost:{PORT}")
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
