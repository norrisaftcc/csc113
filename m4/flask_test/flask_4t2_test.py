from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    page =  '''
    <h1 style="background-color:DodgerBlue;">Hello World</h1>
    <h1>Welcome to Flask</h1>
    <a href="/hello">Click here for a special message</a>
    <p>This is the end of the page</p>
    '''
    return page

# say hello to the user
@app.route('/hello')
def hello():
    return '<b><i>Hello, World!</i></b>'

@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        full_name = request.form['full_name']
        if ' ' in full_name:
            first_name, last_name = full_name.rsplit(' ', 1)
            reversed_name = f"Hello {last_name}, {first_name}"
            return reversed_name
        return redirect(url_for('name'))  # Redirect back to the /name route if the condition is not met
    return '''
        <form method="post">
            <label for="full_name">Enter your full name:</label><br>
            <input type="text" id="full_name" name="full_name"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)