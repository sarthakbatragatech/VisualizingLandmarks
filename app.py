import os
from flask import Flask, render_template, request, url_for
from map import create_map


app = Flask(__name__)

# Snippet for cache busting CSS files

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route("/", methods=('GET','POST'))
def home():
    if request.method == 'GET':
        create_map()
        return render_template("homepage.html")

if __name__ == "__main__":
	app.run(debug = True)