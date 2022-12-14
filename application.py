from flask import Flask, render_template

from wtform_fields import *

# Configure app

app = Flask(__name__) # WSGI standard
# make it central callable object

app.secret_key = 'secretkey'

@app.route("/", methods=['GET','POST'])
def index():
    
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        return "Success!"
    
    return render_template("index.html",form=reg_form)


if __name__ == '__main__':
    app.run(debug=True)
