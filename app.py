from flask import Flask, render_template, request, url_for, redirect, jsonify 
# import os
import cv2

app = Flask(__name__)

# flaskApp = os.getenv("FLASK_APP")
# flaskDebug = os.getenv("FLASK_DEBUG")

@app.route("/base")
def about():
  return render_template('base.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)