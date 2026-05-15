from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def calculator_page():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    a = float(request.form["a"])
    b = float(request.form["b"])
    op = request.form["op"]

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b if b != 0 else "NaN"
    else:
        result = "Invalid operation"

    return f"Result: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
