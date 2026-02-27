from flask import Flask, request, render_template_string
import os
app = Flask(__name__)


referenceForm = """
<!DOCTYPE html> This tells program its in HTML
<html>
<body> Everything in body is shown on screen
    <form method="POST"> # When submit clicked, post method used; sends to flask
        <input type="text" name="user_input" placeholder="Type something..."> # input type easy, name = name of variable, placeholder = txtbox hint
        <button type="submit">Submit</button>
    </form>
    {% if result %}
        <p>You entered: {{ result }}</p>
    {% endif %}
</body>
</html>
"""

FORM = """
<!DOCTYPE html>
<html>
<body>
    <form method="POST">
        <div>
            <label>First name: </label><input type="text" name="firstNameInput" placeholder="Type here: ">
        </div>
        <div>
            <label>ZIP code: </label><input type="text" name="zipCodeInput" placeholder="Type here: ">
        </div>
        <div>
            <label>Subject: </label><input type="text" name="subjectInput" placeholder="Type here: ">
        </div>
        <div>
            <label>Earliest date: </label><input type="text" name="EarliestDateInput" placeholder="Type here: ">
        </div>
        <div>
            <label>Latest date: </label><input type="text" name="LatestDateInput" placeholder="Type here: ">
        </div>
        <button type="submit">Submit</button>
    </form>
    {% if userInfo %}
        <p>Submitted!</p>
    {% endif %}
</body>
</html>
"""

@app.route("/t", methods=["GET","POST"])
def home():
    userInfo = None
    if request.method == "POST":
        userInfo = [request.form["firstNameInput"], request.form["zipCodeInput"], request.form["subjectInput"], request.form["EarliestDateInput"], request.form["LatestDateInput"],]
        print(userInfo)
    return render_template_string(FORM, userInfo=userInfo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
