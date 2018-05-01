import json
import os

from flask import Flask
from flask import request
from flask import make_response

from lg import *

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    res = request.get_json(silent=True, force=True)
    name_function = res['queryResult']['intent']['displayName']
    if name_function in lg_functions:
        answer = lg_functions[name_function](res)
    else:
        answer = "Something wrong"
    final_answer = generate_webhook_answer(answer)
    return  json.dumps(final_answer, indent=4)


def generate_webhook_answer(message):
    return {
        "speech": message,
        "displayText": message,
        "source": "API.AI-LGlab"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='127.0.0.1')
