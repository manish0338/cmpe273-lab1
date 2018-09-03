import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient
import datetime

urls = ['https://webhook.site/9b6f0517-b0ef-45d5-9c35-04190d0917b0', 'https://webhook.site/9b6f0517-b0ef-45d5-9c35-04190d0917b0', 'https://webhook.site/9b6f0517-b0ef-45d5-9c35-04190d0917b0']

def handle_response(response):
    if response.error:
        print("Error:", response.error)
    else:
        print(response.headers['Date'])

http_client = AsyncHTTPClient()

print('\n')

i = 0
for url in urls:
	http_client.fetch(url, handle_response)
	i += 1
	print('Async req '+ str(i) + ' timestamp - '+str(datetime.datetime.now()))
	if(i>3):
		break

tornado.ioloop.IOLoop.instance().start()