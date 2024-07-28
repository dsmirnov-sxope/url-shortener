from flask import Flask, request, jsonify, redirect

from container import Container

app = Flask(__name__)
container = Container()
container.init_resources()

url_shortener_service = container.url_shortener_service


@app.route('/shorten', methods=['GET', 'POST'])
def shorten_url():
    data = request.json
    original_url = data['url']
    short_url = url_shortener_service().shorten_url(original_url=original_url)
    return jsonify({'short_url': short_url})


@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
    original_url = url_shortener_service().resolve_url(short_url)
    if original_url:
        return redirect(original_url)
    return jsonify({'error': 'URL not found'}), 404
