from flask import Flask, render_template, request, redirect,Response
import git
import os

app = Flask(__name__)
repo = git.Repo(os.path.dirname(os.path.abspath(__file__)))

@app.route('/')
def index():
	repo.remotes.origin.fetch()
	current = repo.head.commit
	latest_commit = repo.remotes.origin.refs[repo.head.ref.remote_head].commit
	if current != latest_commit:
		print("new update available")

	return render_template('index.html')

@app.route('/update')
def update():
	# Stash local changes
	repo.git.stash()
	repo.remotes.origin.fetch()
	repo.remotes.origin.pull(force=True)
	return "This is the update page."


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
