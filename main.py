from flask import Flask
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form action="/" method="post">
         Rotate by:<input type="text" name="rot" id:"rot">
        <textarea name="text" rows="10" cols="30">
        Type your message here.
        </textarea>
        <input type="submit" value="Submit">
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

app.run()