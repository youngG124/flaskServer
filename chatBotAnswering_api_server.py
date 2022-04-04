from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

# 모델 부분
def makeAnswer(question) :
    if "흡연" in question :
        return '흡연은 일반적으로 건강에 해롭습니다. \
            특히 조현병 환자들에게 담배는 복용중인 약물의 \
                효과를 떨어뜨릴 수 있습니다. 따라서 흡연은 \
                    가능하면 피하시는 것이 좋겠습니다. '
    if "나이" in question or "연령" in question :
        return '조현병의 진단이 가능하다면 약물치료는 시작할 수 있습니다. \
            다만, 약물에 따라 사용할 수 있는 연령 제한이 있는 경우가 있으니 \
                약물의 종류 선택은 담당 선생님과 상의가 필요합니다.'
    if "토" in question :
        return '약을 먹은지 서너시간이 지나지 않았고 먹은 약을 토했을 정도로 \
            많이 토했다면 약을 다시 복용하시는 것이 좋을 것 같습니다.'
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