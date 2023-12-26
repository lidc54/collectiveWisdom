from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import json

data = {'result': 'this is a test'}
host = ('你中间转发的本地地址', '对应端口（int类型，不是字符串）')
host = ('128.0.0.1', 8008) #例子

url = "https://twapi.openai-hk.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "api-key"
}


# def get_openai_response(content):
#     response = requests.post(url, headers=headers, data=json.dumps(content).encode('utf-8') )
#     result = response.content.decode("utf-8")
#     return result


class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        datas = self.rfile.read(int(self.headers['content-length']))
        # print('headers', self.headers)
        try:
            print("do post:", self.path, self.client_address, datas)
            question=eval(datas.decode("utf-8"))
            response = requests.post(url, headers=headers, data=datas )
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # self.wfile.write(json.dumps(data).encode())
            content=response.content.replace(b'null',b'None')
            self.wfile.write(content)
        except Exception as e:
            print(e)
            self.send_response(404)

if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()

