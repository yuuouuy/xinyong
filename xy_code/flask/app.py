from flask import Flask,request
from flask_cors import CORS  # 导入 CORS
from justicegpt.model.search import index_api,page_api,tags_api,detail_api
from justicegpt.model.ai import aiSearch_api,aiAsk_api


app = Flask(__name__)
CORS(app,supports_credentials=True)

@app.route('/index', methods = ["post"])
def index():
    params=request.get_json()
    return index_api(params)

@app.route('/page', methods = ["post"])
def page():
    params=request.get_json()
    return page_api(params)

@app.route('/tags', methods = ["post"])
def tags():
    params=request.get_json()
    return tags_api(params)

@app.route('/detail', methods = ["post"])
def detail():
    params=request.get_json()
    return detail_api(params)

@app.route('/aiSearch', methods = ["post"])
def aiSearch():
    params=request.get_json()
    return aiSearch_api(params)

@app.route('/aiAsk', methods = ["post"])
def aiAsk():
    params=request.get_json()
    return aiAsk_api(params)

if __name__=="__main__":
    app.run(port=2020,host="127.0.0.1",debug=True)

