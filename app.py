from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        name = request.form.get('name')
        result = f"Hello, {name}!"
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=8000)
