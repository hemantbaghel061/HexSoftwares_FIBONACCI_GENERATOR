from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    n = int(request.form['number'])
    fibonacci_sequence = generate_fibonacci(n)
    return jsonify(fibonacci_sequence)

if __name__ == '__main__':
    app.run(debug=True)
