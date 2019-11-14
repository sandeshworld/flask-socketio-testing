from flask import Flask, render_template
from flask_socketio import SocketIO

#create a flask object called app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'

#socketio is being applied to the app
socketio = SocketIO(app)


#we will use flask view

#the following marker indicates the user visiting the home page.
#which is indicated by the router decorator '/'
@app.route('/')
def sessions():
	return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)



#if another program is importing main.py then the if __name__ == '__main__' is
#false, this helps seperate the executable part from the library part
#when main.py is imported everything but the below is executed
if __name__ == '__main__':
	
	socketio.run(app, debug=True) #the run method takes optional host
	#and port arguments but by default will listen on localhost:5000.
	#debug=True enables us to sort out the errors with ease
