from flask import Flask
app = Flask(__name__)
import datetime

@app.route("/")
def getUtc():
	now = datetime.datetime.utcnow()
	difference = (now - datetime.datetime(1970, 1, 1)).total_seconds()
	return str(difference)

if __name__ == "__main__":
	app.run()