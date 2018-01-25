from flask import Flask

from ch04_functions_modules.vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello World from Flask'


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!'))


app.run()