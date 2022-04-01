from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

# 모델 부분
def makeAnswer(question) :
    if "흡연" in question :
        return '흡연에 대한 답변'
    if "연령" in question :
        return '중단에 대한 답변'
    if "토" in question :
        return '토에 대한 답변'
    else : 
        return question + '에 대한 답변. 학습되지 않음.'

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