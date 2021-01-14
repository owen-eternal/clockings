import os
import secrets
from flask import Blueprint
from clocking_api import db
from base64 import decodebytes
from flask_restful import Resource
from flask_cors import cross_origin
from flask import request, current_app
from .models import EmployClockings

clocking_bp = Blueprint('clockings_bp', __name__)


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


@clocking_bp.route('/api/1.0/clockings/upload', methods=["POST"])
@cross_origin()
def upload():
    if req:
        req = request.get_json()
        root_path = current_app.root_path
        f_name = save_image(req['png'], root_path)
        empl = EmployClockings(
            status=req['status'], image=f_name,
            location=req['location'],  comment=req['comment'])
        db.session.add(empl)
        db.session.commit()
    print(f'{f_name} has been saved int the database!')
    return "hi"
