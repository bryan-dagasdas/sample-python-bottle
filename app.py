from bottle import run, request, response
from bottle import get, post

@get('/')
def index():
	api_response = 'Sample Python Bottle'
	return api_response

if __name__ == '__main__':
	run(host='localhost', port=8080)

