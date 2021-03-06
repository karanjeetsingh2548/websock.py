
  from flask import Flask, jsonify, render_template, request
  from flask_socketio import SocketIO, emit

  app = Flask(__name__)
    socketio = SocketIO(app)

  votes = {"yes": 0, "no": 0, "maybe": 0}

  @app.route("/")
  def index():
      return render_template("index.html", votes=votes)
   
    @app.route("/hello")
  def hello():
      return render_template("hello.html")

  @socketio.on("submit vote")
  def vote(data):
      selection = data["selection"]
      votes[selection] += 1
      emit("vote totals", votes, broadcast=True)
