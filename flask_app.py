
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
@app.route('/hello/<name>')
def render_hello_world(name=None):
    return render_template('hello.html', name=name)


@app.route('/')
@app.route('/cubemap')
def render_cubemap():
    return render_template('cubemap.html')


@app.route('/stage')
def render_stage():
    return render_template('stage.html')


@app.route('/vr/ballshooter')
def render_ballshooter():
    return render_template('vr-ballshooter.html')

@app.route('/vr/sandbox')
def render_sandbox():
    return render_template('vr-sandbox.html')

@app.route('/vr/skybox')
def render_skybox():
    return render_template('skybox.html')