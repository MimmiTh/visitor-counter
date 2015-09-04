from flask import Flask
from lockfile import LockFile
app = Flask(__name__)

@app.route('/')
def visitcount():
	lock = LockFile("visitors.txt")
	with lock:
		file = open("visitors.txt", 'w+')
		nr = int(file.read()) + 1;
		file.write(nr)
		
if __name__ == '__main__':
    app.run()