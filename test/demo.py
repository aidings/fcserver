# import sys

# sys.path.insert(0, '../src')

from fcserver import FalconServer, App
from PIL import Image
import json
from wsgiref.simple_server import make_server
import pudb


class Server(FalconServer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        print('My server model loadding...')
    
    def on_post(self, req, resp):
        # pudb.set_trace()
        # print(req.params)
        # img_a = self.decode_image(req, 'aimg')
        img_a = self.decode_numpy(req, 'aimg')
        self.save_data('aimg.png', img_a)
        img_b = self.decode_image(req, 'bimg')
        self.save_data('bimg.png', img_b)
        resp.body = json.dumps({'aimg': 'is a numpy', 'bimg': 'is a image'})

s = Server()

app = App()
app.add_route('/ding', s)

if __name__ == '__main__':
    with make_server('0.0.0.0', 8080, app) as httpd:
        httpd.serve_forever()