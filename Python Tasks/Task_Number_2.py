# -----------------------------------
# Author: KHAWAJA ABDUL MOIZ
# Roll Number: 70288
# Email: khawajaahmedraza4@gmail.com
# ------------------------------------


# Calculator:
# ---------------------------------------------------------------------------------------------------------------------
# This calculator acts as a basic calculator, executing basic arithmetic tasks like addition, subtraction,      multiplication, and division according to the user's choices.The user will be prompted to enter two numbers and then select the operation they wish to perform. The calculator will then display the result of the operation.
# ---------------------------------------------------------------------------------------------------------------------


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)