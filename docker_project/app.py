from flask import Flask
from bp.crud import bp_crud
from db.mongo_db import get_db
app = Flask(__name__)

app.register_blueprint(bp_crud)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'




if __name__ == '__main__':
    collection = get_db()
    app.run()
