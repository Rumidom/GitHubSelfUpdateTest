from flask import Flask, render_template, request, redirect,Response
import git

app = Flask(__name__)

@app.route('/')
def index():
	current = repo.head.commit
	repo.remotes.origin.pull()
	if current != repo.head.commit:
    	print("new update available")

    return render_template('index.html')

@app.route('/update')
def update():
	repo = git.Repo('/')
	repo.remotes.origin.pull()
    return "This is the update page."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)