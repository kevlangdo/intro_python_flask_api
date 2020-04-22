from flask import Flask, jsonify, make_response, request


notes = [
  {
      'id':1,
      'title': u'Write Article',
      'subject':u'Write Flask article',
      'description':u'Need to write Flask article on APIs'
  },
    {
      'id':2,
      'title': u'Write Article',
      'subject':u'Write Python Microservices',
      'description':u'Need to write Python Microservices article'
  }

]


app = Flask(__name__)

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify({'notes': notes})

@app.route('/notes/<int:id>', methods=['GET'])
def get_all_notes(id): 
    note = [note for note in notes if note['id'] == id]
    return jsonify({'notes': note})


@app.route('/notes', methods=['POST'])
def insert_notes():
    note = {
        'id':3,
        'title':'Introduction Flask React',
        'subject':'Write a Flask React article',
        'Description': 'Write a Flask/React tutorial'
    }
    notes.append(note)

    return jsonify({'notes': notes}), 201

@app.route('/notes/<int:id>', methods=['PUT'])
def update_notes(id):
    note = [note for note in notes if note['id'] == id]
    note[0]['title'] = note[0]['title']
    note[0]['subject'] =  note[0]['subject']
    note[0]['description'] = note[0]['description']

    return jsonify({'note': note[0]})

@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_notes(id):
    note = [note for note in notes if note['id'] == id]
    del note[0]["id"]
    del note[0]['title'] 
    del note[0]['subject'] 
    del note[0]['description'] 

    return jsonify({'notes': notes}), 201   

@app.errorhandler(404)
def record_not_found(error):
    return make_response(jsonify({'error': 'Note Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)