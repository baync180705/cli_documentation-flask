from flask import Flask, request
from ai_model import generate_article

app = Flask(__name__)

@app.route('/', methods=['POST'])
def processParagaph():
    if(request.is_json):
        paragraphs = request.get_json()
        article= generate_article(paragraphs)
        return article
    else:
        return 'ERROR'

