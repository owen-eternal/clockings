from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from flask_restful import Resource
from base64 import decodebytes
import secrets
import os


def save_image(base64_img, root):
    f_name = secrets.token_hex(8)
    f_ext = '.png'
    image = f_name+f_ext

    base64_img_bytes = base64_img.encode('utf-8')
    path = os.path.join(root, 'static/images', image)
    with open(path, 'wb') as f:
        decode_image_data = decodebytes(base64_img_bytes)
        f.write(decode_image_data)
    return image


def create_app():

    app = Flask(__name__)

    CORS(app)
    api = Api(app)

    # Create Resources
    class Clockings(Resource):
        def post(self):
            req = request.get_json()
            root_path = app.root_path
            f_name = save_image(req['png'], root_path)
            print(f'{f_name} has been saved int the database!')
            return 'daksdjkasdjkajsdk'

    # add resources
    api.add_resource(Clockings, '/upload')

    return app
