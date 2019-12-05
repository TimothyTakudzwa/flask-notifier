from flask_socketio import SocketIO, emit
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

socketio = SocketIO(app)


@app.route('/test', methods = ['POST', 'GET'])
def test():
    if request.method == 'POST':
        data = request.get_json()
        message = data['message']
        user = data['user']
        socketio.emit('newnumber', {'message': message, 'user':user}, namespace='/test')
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')
    
@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
