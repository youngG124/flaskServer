from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

# 모델 부분
def makeAnswer(question) :
    return '(' + question + ") 이라는 질문을 주셨습니다. 저의 답변은 다음과 같습니다."

@app.route('/')
def default() :
    return "return of default_api"

# 질문에 대한 답변 return 하는 api
@app.route('/<question>')
def exportAnswer(question):
    print(question)
    return jsonify({"answer" : makeAnswer(question)})

if __name__ == '__main__' :
    app.run(debug=True, host="127.0.0.1", port=5000)