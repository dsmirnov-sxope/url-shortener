from shortener.container import init_db
from shortener.views import app

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
