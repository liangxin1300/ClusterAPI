
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        URL_PREFIX = '/api/v1'
    )

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from resources import cluster
    app.register_blueprint(cluster.bp,
                           url_prefix=app.config['URL_PREFIX'])

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
