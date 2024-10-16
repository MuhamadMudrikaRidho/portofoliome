from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


# Route to display the main portfolio page
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
