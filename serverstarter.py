from flask import (
    Flask,
    render_template
)

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
