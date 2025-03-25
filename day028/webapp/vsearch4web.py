from flask import Flask, render_template, request
from markupsafe import escape
from vsearch import search4letters

app = Flask(__name__)

def log_request(req: 'flask_request', res: str)->None:
    with open('vsearch.log', 'a') as f:
        print(req.form, req.remote_addr, req.user_agent, res, file=f, sep='|')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_title='Here are your results', the_phrase=phrase, the_letters=letters, the_results=results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')

@app.route('/viewlog')
def view_the_log()-> str:
    with open('vsearch.log') as f:
        contents = f.read()
    return escape(contents)


if __name__ == '__main__':
    app.run(debug=True)