from flask_socketio import SocketIO, emit
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

socketio = SocketIO(app)


@app.route('/notify', methods = ['POST', 'GET'])
def test():
    print('-----------------------------------------------------')
    if request.method == 'POST':
        data = request.get_json()
        notification = data['notification']
        user_id = data['user_id']
        action = data['action']
        if action == 'new_offer':
            socketio.emit('newnumber', {'notification': notification, 'user_id':user_id}, namespace='/test')
        elif action == 'new_request':
            socketio.emit('new_request', {'notification': notification, 'user_id':user_id}, namespace='/new_request')
        elif action == 'ofer_accepted':
            socketio.emit('offer_accepted', {'notification': notification, 'user_id':user_id}, namespace='/offer_accepted')
        elif action == 'offer_rejected':
            socketio.emit('offer_rejected', {'notification': notification, 'user_id':user_id}, namespace='/offer_rejected')
        elif action == 'counter_offer':
            socketio.emit('counter_offer', {'notification': notification, 'user_id':user_id}, namespace='/counter_offer')
    return render_template('index.html')



if __name__ == '__main__':
    socketio.run(app)
