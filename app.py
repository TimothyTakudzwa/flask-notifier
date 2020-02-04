from flask_socketio import SocketIO, emit
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
socketio = SocketIO(app, cors_allowed_origins="*", logger=True )


@app.route('/notify', methods = ['POST', 'GET'])
@cross_origin()
def test():
    print('-----------------------------------------------------')
    if request.method == 'POST':
        data = request.get_json()
        notification = data['notification']
        user_id = data['user_id']
        action = data['action']
        url = data['url']
        if action == 'new_offer':
            socketio.emit('new_offer', {'notification': notification, 'user_id':user_id, 'url':url}, namespace='/new_offer')
        elif action == 'new_request':
            socketio.emit('new_request', {'notification': notification, 'user_id':user_id, 'url':url}, namespace='/new_offer')
        elif action == 'offer_accepted':
            socketio.emit('offer_accepted', {'notification': notification, 'user_id':user_id, 'url':url}, namespace='/new_offer')
        elif action == 'offer_rejected':
            socketio.emit('offer_rejected', {'notification': notification, 'user_id':user_id, 'url':url}, namespace='/new_offer')
        elif action == 'counter_offer':
            socketio.emit('counter_offer', {'notification': notification, 'user_id':user_id, 'url':url}, namespace='/new_offer')
        elif action == 'DELIVERY':
            socketio.emit('DELIVERY', {'notification': notification, 'user_id':user_id, 'url':url}, namespace='/new_offer')            

    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')
    
@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')



if __name__ == '__main__':
    socketio.run(app, port=8000)
