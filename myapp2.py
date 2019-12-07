from flask import Flask, request, url_for, render_template
from werkzeug.utils import redirect

from Employee import Employee

employees = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def employees_view():
    if request.method == "POST":
        employee_id = request.form.get("employee_id", "")
        employee_first_name = request.form.get("employee_first_name", "")
        employee_last_name = request.form.get("employee_last_name", "")
        new_employee = Employee(1, "John", "Smith")
        employees.append(new_employee)

        return redirect(url_for('employees_view'))

    return render_template("index.html", employees=employees)


if __name__ == "__main__":
    app.run(debug=True)
