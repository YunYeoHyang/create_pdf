from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from normal.create_pdf import create_pdf


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.path = '/generate-pdf'
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # 解析JSON数据
        json_data = json.loads(post_data.decode('utf-8'))

        # 构建响应
        response_json = json.dumps(create_pdf(json_data)).encode('utf-8')

        # 设置响应头
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(response_json)))
        self.end_headers()

        # 发送响应
        self.wfile.write(response_json)


def run_server():
    server_address = ('', 7501)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server on port 7501...')
    httpd.serve_forever()


