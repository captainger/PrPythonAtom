from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/get_classifier_result/<version>", methods=['GET', 'POST'])
def return_classifier_result(version):
    data = {'version': int(version)}
    if request.method == 'POST':
        arg = request.json
        if version == '1':
            data['predict'] = arg['predict']
        if version == '0':
            data['predict'] = arg['old_predict'] 
        return jsonify(data)

@app.route("/")
def hello():
    return render_template('Help.html')


if __name__ == "__main__":
    app.run()
