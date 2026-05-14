from flask import Flask, make_response, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

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

if __name__ == "__main__":
    app.run(debug=True)
