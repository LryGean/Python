# flask
from lib2to3.pgen2.pgen import generate_grammar
from urllib import request


@api.route('/get', methods=['GET'])
def test_javascript_http():
    p = request.args.get('name')
    return p, 200

@api.route('/psw', methods=['GET'])
@auth.login_required
def get_psw():
    p = request.args.get('psw')
    r = generate_password_hash(p)
    return 'aaaaaa', 200