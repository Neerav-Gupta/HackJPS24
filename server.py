from flask import Flask, send_from_directory, request, redirect, url_for
from main import fetchResults, getReponse
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def base():
    if request.method == "POST":
        query = request.form["search"]
        return redirect(url_for("search", q=query))
    else:
        return send_from_directory('public', 'index.html')
    
@app.route("/<path:path>")
def home(path):
    return send_from_directory('public', path)

@app.route("/search/<q>", methods=["POST", "GET"])
def search(q):
    if request.method == "POST":
        try:
            title = request.form["title"]
            print(title)
            return redirect(url_for("getSummary", title=title))
        except Exception:
            query = request.form["search"]
            return redirect(url_for("search", q=query))
    else:
        return send_from_directory('public', 'index.html')
    
@app.route("/search/summary/<title>/", methods=["POST", "GET"])
def getSummary(title):
    if request.method == "POST":
        query = request.form["search"]
        return redirect(url_for("search", q=query))
    else:
        return send_from_directory('public', 'index.html')
    
@app.route("/search/query")
def getRequest():
    args = request.args
    return fetchResults(args["search"])

@app.route("/search/summary/<a>/query")
def getSummaryData(a):
    args = request.args
    return getReponse(args["search"])

if __name__ == "__main__":
    app.run(debug=True)