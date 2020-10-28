from flask import Flask, request, make_response, jsonify
from usefulfcts import event_add, event_update, event_delete, get_answer, all_fields

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/appointment", methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        # get diologflow request
        json_content = request.get_json(force=True)
        req = json_content['queryResult']
        # extract intent, message and parameters
        intent = req.get('intent', None)['displayName']
        text = req.get('queryText', None)
        params = req.get('parameters', None)

        # process the request and prepare the answer in json format
        answer = get_answer(intent, params)

        reply = {
            "fulfillmentText": answer,
        }

        return jsonify(reply)

if __name__ == "__main__":
    app.run(debug=True)
