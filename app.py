from flask import Flask, render_template, request
from flask import jsonify
from flask import json

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/save-points-to-file', methods=['POST'])
def save_points_to_file():

    file = open('rez3.txt', 'r')
    resList = json.load(file)
    file.close()

    file = open('rez3.txt', 'w')
    resList.append(request.json)
    json.dump(resList, file)
    file.close()

    sortedList = sorted(resList, key=lambda vi: vi['points'], reverse=True)

    return json.dumps(sortedList)


if __name__ == '__main__':
    app.run()
