import json, jsonify
import os

from flask import Flask, request, make_response, jsonify

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
    return make_response(jsonify({'fulfillmentText': answer}))


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='127.0.0.1')
