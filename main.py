from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>
<html lang="en-US">
    <body>
        <form action="/hello">
            <label for="first-name">First Name:</label>
            <input id="first-name" type="text" name="first_name"/>
            <input type="submit"/>
        </form>
    </body>
</html>    
"""

@app.route("/")
def index():
    return form

@app.route("/hello")
def hello():
    first_name = request.args.get("first_name")
    return "Hello, " + first_name + ". Enjoy your stay."   

app.run()    