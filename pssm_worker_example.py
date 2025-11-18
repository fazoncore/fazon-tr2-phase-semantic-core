"""Minimal example of a phase-semantic metrics worker for TR-2."""
import math
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from prometheus_client import Gauge, start_http_server

g_avg_coherence = Gauge('tr2_pssm_avg_coherence', 'Average coherence C_bar', ['session'])
g_avg_phase_weight = Gauge('tr2_pssm_avg_phase_weight', 'Average phase weight W_bar', ['session'])

def huber(u: float, delta: float) -> float:
    au = abs(u)
    if au <= delta:
        return 0.5 * u * u
    return delta * (au - 0.5 * delta)

def process_window(window, session_id="demo", sigma=0.6, delta=0.3, rho=0.7):
    cs = []
    ws = []
    for item in window:
        c = float(item.get("coherence", 0.0))
        dphi = float(item.get("phase_delta", 0.0))
        w = math.exp(-(dphi ** 2) / (2 * sigma * sigma))
        cs.append(c)
        ws.append(w)
    if cs:
        g_avg_coherence.labels(session=session_id).set(sum(cs)/len(cs))
    if ws:
        g_avg_phase_weight.labels(session=session_id).set(sum(ws)/len(ws))

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length)
        try:
            payload = json.loads(body.decode('utf-8'))
        except Exception:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Invalid JSON')
            return
        session_id = payload.get("session", "demo")
        window = payload.get("window", [])
        process_window(window, session_id=session_id)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

    def log_message(self, *args, **kwargs):
        return

def main():
    start_http_server(9105)
    server = HTTPServer(('0.0.0.0', 9095), Handler)
    server.serve_forever()

if __name__ == "__main__":
    main()
