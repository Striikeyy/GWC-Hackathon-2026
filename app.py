from flask import Flask, request, render_template_string
import os
from main import persons, groups, setup_data
from person import Person

app = Flask(__name__)

setup_data()

FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Group Matcher</title>
</head>
<body>
    <h2>Find a Math Study Group</h2>

    <form method="POST">
        <div>
            <label>First name: </label>
            <input type="text" name="firstNameInput" required>
        </div>

        <div>
            <label>ZIP code: </label>
            <input type="text" name="zipCodeInput" required>
        </div>

        <div>
            <label>Subject: </label>
            <input type="text" name="subjectInput" required>
        </div>

        <div>
            <label>Earliest date (YYYY-MM-DD): </label>
            <input type="text" name="EarliestDateInput" required>
        </div>

        <div>
            <label>Latest date (YYYY-MM-DD): </label>
            <input type="text" name="LatestDateInput" required>
        </div>

        <br>
        <button type="submit">Submit</button>
    </form>

    {% if matches is not none %}
        <hr>
        {% if matches %}
            <h3>Matching Groups:</h3>
            <ul>
                {% for group in matches %}
                    <li>
                        <strong>{{ group.name }}</strong> |
                        Subject: {{ group.subject }} |
                        ZIP: {{ group.zipCode }} |
                        Start Date: {{ group.dateStart }} |
                        End Date: {{ group.dateEnd }}
                    </li>
                {% endfor %}
            </ul>
        {% else %}
            <p>No matching groups found.</p>
        {% endif %}
    {% endif %}
</body>
</html>
"""

@app.route("/t", methods=["GET", "POST"])
def home():
    matches = None

    if request.method == "POST":
        try:
            userInfo = [
                request.form["firstNameInput"],
                request.form["subjectInput"],
                int(request.form["zipCodeInput"]),
                request.form["EarliestDateInput"],
                request.form["LatestDateInput"],
            ]

            new_person = Person(*userInfo)
            persons.append(new_person)

            matches = new_person.findMatches(groups)

            print(f"Matches found: {matches}")

        except ValueError as e:
            matches = []

            print(f"Error with form data: {e}")

    return render_template_string(FORM, matches=matches)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))