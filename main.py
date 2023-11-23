from http.server import HTTPServer

from server.appliction import RequestHandler


# 启动服务器
def start_server(port):
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Server started on port {port}")
    httpd.serve_forever()


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    port_number = 8000
    start_server(port_number)
