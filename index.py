from flask import Flask, render_template
import codecs
import threading
import time
from pyautogui import hotkey
app = Flask(__name__, template_folder='static')

ser = serial.Serial('COM9',115200) # check your com port

# thread for keyboard input, still needs a way to exit gracefully
def buttonToKeyboard():
    while True:
	result = ser.read(size=1)
	if result==b'\x81':
	    hotkey('left')
	if result==b'\x82':
	    hotkey('right')

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    thread = threading.Thread(target=buttonToKeyboard,daemon=True)
    thread.start()
    app.run(debug=True, host='0.0.0.0')
