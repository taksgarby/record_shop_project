from flask import Flask, render_template

from controllers.record_shop_controller import record_shop_blueprint

app = Flask(__name__)

app.register_blueprint(record_shop_blueprint)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)