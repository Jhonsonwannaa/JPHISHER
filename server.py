
from http.server import HTTPServer, BaseHTTPRequestHandler

from rich.console import Console

console = Console()
try :
    def handle_post(request):
    	content_length = int(request.headers['Content-Length'])
    	post_data = request.rfile.read(content_length)
    	
    	var=post_data.decode('utf-8')
    	console.print(f'[bod green]{var}+'\n\n\n')
    
    	
    	
    	
    	request.send_response(200)
    	request.send_header('Content-type', 'text/html')
    	request.end_headers()
    	
    def do_post(request):
        if request.command == 'POST':
        	handle_post(request)
    if __name__ == '__main__':
    	server_address = ('0.0.0.0', 8000)
    	httpd = HTTPServer(server_address, BaseHTTPRequestHandler)
    	console.print('[bold green]The receiving server to be started ... on port 8000\n\n')
    	httpd.RequestHandlerClass.do_POST = do_post
    	
    	httpd.serve_forever()
    	
except self.finish_request(request, client_address) :
	print('')
except self.RequestHandlerClass(request, client_address, self):
	print('')
except self.handle():
	print('')
except self.handle_one_request():
	print('')
except self._sock.sendall(b):
	print('')				
