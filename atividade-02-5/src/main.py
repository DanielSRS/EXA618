from flask import Flask, make_response, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta, timezone

app = Flask(__name__, template_folder="templates")
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)
app.secret_key = 'EXA844'

@app.route("/")
def counter(_name=''):
    if "counter" in request.cookies:
        count = int(request.cookies.get("counter"))
        name = request.cookies.get("name")
    else:
        name = ''
        count = 1

    if _name != '':
        name = _name
    resp = make_response(render_template("counter.html", count=count, name=name))
    resp.set_cookie("counter", str(count + 1), max_age=10 * 365 * 24 * 60 * 60)
    if _name != '':
        resp.set_cookie("name", _name, max_age=10 * 365 * 24 * 60 * 60)

    return resp

@app.route("/process-name", methods=["POST"])
def process_name():
  name_input = request.form.get("user_name")
  return redirect(url_for('save_name', nome=name_input))

@app.route("/nome/<nome>")
def save_name(nome):
  if "counter" in request.cookies:
      count = int(request.cookies.get("counter"))
  else:
      count = 1

  resp = make_response(render_template("counter.html", count=count, name=nome))
  resp.set_cookie("counter", str(count + 1), max_age=10 * 365 * 24 * 60 * 60)
  resp.set_cookie("name", nome, max_age=10 * 365 * 24 * 60 * 60)

  return resp

@app.route("/perfil")
def profile():
  if 'username' in session:
    username = session["username"]
    running_time = (datetime.now(timezone.utc) - session.get('_creation_time'))
    remaining_time = app.permanent_session_lifetime - running_time
    if remaining_time.total_seconds() > 0:
      return render_template("profile.html", username=username, remaining_time=remaining_time.total_seconds())
  return redirect(url_for('login'))

@app.route("/login", methods=['GET'])
def login():
    if 'username' in session:
      username = session["username"]
      running_time = (datetime.now(timezone.utc) - session.get('_creation_time'))
      remaining_time = app.permanent_session_lifetime - running_time
      if remaining_time.total_seconds() > 0:
        return redirect(url_for('profile'))
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def loginS():
  username = request.form['username']
  password = request.form['password']
  session['username'] = username
  session['_creation_time'] = datetime.now(timezone.utc)
  return redirect(url_for('profile'))

@app.route('/logout')
def logout():
  session.pop('username', None)
  session.pop('password', None)
  session.pop('_creation_time', None)
  return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
