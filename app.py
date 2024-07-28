from container import init_db
from views import app


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
