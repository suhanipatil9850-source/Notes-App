from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
    except FileNotFoundError:
        notes = []
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form.get('note')
    if note:
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear_notes():
    with open("notes.txt", "w") as file:
        file.write("")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
