from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/" method="post">
         Rotate by:<input type="text" name="rot" value="0">
        <textarea name="text" rows="10" cols="30">{text}</textarea>
        <input type="submit" value="Submit">
      </form>
    </body>
</html>
"""

@app.route('/')
def index():
    return form.format(text='')

@app.route('/', methods=['POST'])
def encrypt():
    form_rot = request.form['rot']
    form_text = request.form['text']

    rot = int(form_rot)
    text = str(form_text)

    encrypted = rotate_string(text,rot)

    return form.format(text=encrypted)

app.run()