from flask import Flask, render_template, request

app = Flask(__name__)

# 1. This route displays your frontend webpage
@app.route('/')
def home():
    return render_template('index.html')

# 2. This route receives data from the browser, processes it, and returns a result
@app.route('/greet', methods=['POST'])
def greet_user():
    # Grab the name input from the HTML form safely
    username = request.form.get('user_name')
    
    # Process it with Python string manipulation
    processed_name = username.upper()
    
    # Send the result back to the screen
    return f"<h1>Hello, {processed_name}! Welcome to your Python app!</h1>"

if __name__ == '__main__':
    app.run(debug=True)