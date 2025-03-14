from flask import Flask, render_template

# Створення екземпляра Flask
app = Flask(__name__)

# Головний маршрут
@app.route('/')
def home():
    return render_template('index.html')  # Вивести шаблон index.html

# Запуск додатку на вказаному порту
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
