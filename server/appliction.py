# 定义请求处理器类
import urllib
from http.server import BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = urllib.parse.parse_qs(post_data)

        # 在这里处理接收到的POST请求数据
        # 这里的示例是将请求数据打印到控制台
        print("Received POST request data:")
        for key, values in parsed_data.items():
            print(f"{key}: {values}")

        # 返回响应
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'POST request received')
