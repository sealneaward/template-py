from flask import Flask, render_template, redirect, session, jsonify, url_for, request
import db.helper as DB
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
static_location = '127.0.0.1:5000/static'

# create connection object
db = DB()


@app.route('/', methods=['GET'])
def index():
    data = db.get_data()
    return render_template("")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

