#!/usr/bin/env python
from threading import Lock, Thread
from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect, Namespace
from time import sleep
import subprocess
from subprocess import Popen, PIPE



# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()
COUNT = 0

def background_thread(file, link):
    """Example of how to send server generated events to clients."""
    sleep(1)
    link = link.strip()
    exe = ["C:/ProgramData/chocolatey/bin/axel"]
    args=['-o', file, '-a', '-n', '8', link]
    cmd = exe + args
    try:
        process = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        socketio.emit('my_response',
                    {'file': '[DOWNLOADING]: ', 'link': stdout},
                    namespace='/movie')
        if stderr:
            socketio.emit('my_response',
                    {'file': '[DOWNLOADING]: ', 'link': stderr},
                    namespace='/movie')
            
        
    except Exception as e:
        # An exception happened in this thread
        print(e)
        socketio.emit('my_response',
                {'file': '[ERROR]: ', 'link': 'Could not download the file !!!!'},
                namespace='/movie')
    finally:
        # Mark this task as done, whether an exception happened or not
        socketio.emit('my_response',
                {'file': '[DOWNLOADING]: ', 'link': 'Complete !!!!'},
                namespace='/movie')
   
  
            


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


class MyNamespace(Namespace):
    def on_my_download_event(self, message):
        # if not message.get('link',None):
        #     return
        global COUNT
        COUNT += 1
        print (COUNT)
        global thread
        with thread_lock:
            if thread is None:
                thread = socketio.start_background_task(background_thread,message['file'],message["link"])
        emit('my_response',
             {'file': message['file'], 'link': message['link']})
       
            

    def on_connect(self):
        emit('my_response', {'file': 'Connected', 'link': 0})

  
    
    def on_my_ping(self):
        emit('my_pong')


socketio.on_namespace(MyNamespace('/movie'))


if __name__ == '__main__':
    socketio.run(app, debug=False)

