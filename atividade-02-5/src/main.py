from flask import Flask, make_response, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route("/")
def counter():
    if "counter" in request.cookies:
        count = int(request.cookies.get("counter"))
    else:
        count = 1

    resp = make_response(render_template("counter.html", count=count))
    resp.set_cookie("counter", str(count + 1), max_age=10 * 365 * 24 * 60 * 60)

    return resp


if __name__ == "__main__":
    app.run(debug=True)
