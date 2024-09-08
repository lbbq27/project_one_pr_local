from flask import Blueprint


main = Blueprint('blueprint', __name__)


@main.route('/one', methods=['GET'])
def one():
    return ('<h1>HOME</h1>')

