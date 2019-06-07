from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{1 : 'JavaScript'}, {2 : 'Python'}, {3 : 'Ruby'}]

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message':
    'OK'})

@app.route('/languages', methods=['GET'])
def get_languages():
    return jsonify({'languages':
    languages})

@app.route('/add-language', methods=['POST'])
def add_language():
    id = list(languages[-1].keys())[0] + 1
    l = {id: request.json['language']}
    languages.append(l)
    return jsonify({'languages':
    languages})

@app.route('/lang/<int:id>', methods=['GET'])
def returnOne(id):
	lang = languages[id-1]
	return jsonify({'language' : lang})

if __name__ == '__main__':
    app.run(debug=True)