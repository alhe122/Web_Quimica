from flask import Flask
from flask import render_template

app =Flask(__name__,template_folder='theme',static_folder='theme',)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)