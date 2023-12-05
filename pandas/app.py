from flask import Flask, render_template
from scoreRoute import score

app = Flask(__name__)
app.register_blueprint(score, url_prefix='/score')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True) #서버를 다시 끄지 않아도 적용 실행-> 터미널에서 python app.py