from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Azure! Aplikasi ini mendukung auto scaling."

@app.route('/heavy')
def heavy():
    import time
    time.sleep(5)  # Simulasi beban tinggi
    return "Processing selesai!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
