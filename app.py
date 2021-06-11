from flask import Flask
from datetime import datetime
from flask import render_template, request

app = Flask ( __name__ )


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

# A decorator used to tell the application
# which URL is associated function
@app.route('/KFormOne', methods =["GET", "POST"])
def KFormOne():
    if request.method == "POST":
       first_name = request.form.get("Name")
       last_name = request.form.get("City")
       return "Your name is "+first_name + last_name
    return render_template("KFormOne.html")

# A decorator used to tell the application
# which URL is associated function
@app.route('/KFormOneJ', methods =["GET", "POST"])
def KFormOneJ():
    if request.method == "POST":

       first_name = "ken" #request.form.get("Name")

       last_name = "Ceg" #request.form.get("City")
       return "Your name is "+first_name + last_name
    return render_template("KFormOneJ.html")

@app.route('/KFormOneX')
def KFormOneX():
    """Renders the contact page."""
    return render_template(
        'KFormOne.html'
    )

@app.route ( '/data/', methods=['POST', 'GET'] )
def data() :
    if request.method == 'GET' :
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST' :
        form_data = request.form
        return render_template ( 'data.html', form_data=form_data )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


if __name__ == '__main__' :
    app.run ()
