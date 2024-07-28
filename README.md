
# URL Shortener
A simple URL shortening service build with Python and Flask



## Features

- Generate short URLs from long URLs
- Store short and original URLS in a SQLite database
- Redirect from short URLs to the original URLs

## Installation

Install my-project with npm

```bash
  git clone https://github.com/dsmirnov-sxope/url-shortener.git
  cd url-shortener
  python -m venv venv
  source venv/bin/activate
  pip install poetry && poetry install
  python main.py
```
The server will start running on http://localhost:5000/


## Usage/Examples

```bash
curl -X POST -H "Content-Type: application/json" -d '{"url":"https://www.example.com"}' http://localhost:5000/shorten
```

This will return a JSON response with the generated short URL.

To access the original URL, visit the short URL in your browser:
```text
http://localhost:5000/abc123
```
You will be redirected to the original URL.

## Contributing

 Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## License

[MIT](https://choosealicense.com/licenses/mit/)

