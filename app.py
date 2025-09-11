from flask import Flask, request, render_template

app = Flask(__name__)


#''' defines multi-line strings
#<p> displays text on the browser
#"POST" - Sends data to a server, in this app my server to display the name
#"GET" - Retrieves data


# @app.route('/')
# def index():
#     # Renders the HTML template containing the form
#     return render_template('form.html')

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        return f"<p>Nice to meet you, {full_name}!</p>"

    # This part checks:
    # If the user submitted the form
    # Then extracts the name from the submitted data
    # Then sends back a custom greeting

    return '''
        <p>Hello!</p>
        <p>What is your full name?</p>
        <form method="post">
            <input type="text" name="full_name" placeholder="Enter your full name" required>
            <button type="submit">Submit</button>
        </form>
    '''
# @app.get("/", methods=["POST"])
# def index():
#
# def home():
#     name = request.form.get("What is your full name?")
#
#     return f"Hello, {name}!"

#heara
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)