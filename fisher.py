from app import create_app

__author__ = 'kalirfi'


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=app.config['DEBUG'])
