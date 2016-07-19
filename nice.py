from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""
    return """
    <!doctype html>
    <html>
      <head>
        <title>Home</title>
      </head>
      <body>
        <h1>"Hi! This is the home page."</h1>
        <h3> If you'd like to go directly to hello() <a href="http://localhost:5000/hello"> click here</h3>
        """
    #return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label><br>
          <h3>Choose a compliment</h3>
          <input type="radio" name="compliment" value="awesome"> awesome
          <input type="radio" name="compliment" value="terrific"> terrific
          <input type="radio" name="compliment" value="fantastic"> fantastic
          <input type="radio" name="compliment" value="neato"> neato
          <input type="radio" name="compliment" value="fantabulous"> fantabulous
          <input type="radio" name="compliment" value="wowza"> wowza
          <input type="radio" name="compliment" value="brilliant"> brilliant
          <input type="radio" name="compliment" value="smashing"> smashing
          <br>
          <input type="submit">
          <form action="/diss">
          <label>What's your name? <input type="text" name="person"></label><br>
          <h3>Choose a diss</h3>
          <input type="radio" name="diss" value="ugly"> ugly
          <input type="radio" name="compliment" value="terrific"> terrific
          <input type="radio" name="compliment" value="fantastic"> fantastic
          <input type="radio" name="compliment" value="neato"> neato
          <input type="radio" name="compliment" value="fantabulous"> fantabulous
          <input type="radio" name="compliment" value="wowza"> wowza
          <input type="radio" name="compliment" value="brilliant"> brilliant
          <input type="radio" name="compliment" value="smashing"> smashing
          <br>
          <input type="submit">
        </form>
      </body>
    </html>
    """

# @app.route('/diss')
# def say_diss():


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    #print x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
