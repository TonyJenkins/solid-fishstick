#!/usr/bin/env python3
"""
Simple Python web server for the Solid Fishstick Model Railway Club website.
Serves static HTML files on localhost:8000
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Configuration
PORT = 8000
HOST = 'localhost'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve HTML files and handle routing"""
    
    def __init__(self, *args, **kwargs):
        # Set the directory to serve files from (current directory)
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def end_headers(self):
        # Add some basic security headers
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        super().end_headers()
    
    def do_GET(self):
        # Handle root path - serve index.html
        if self.path == '/':
            self.path = '/index.html'
        
        # Call parent method to handle the request
        return super().do_GET()

def main():
    """Start the web server"""
    
    # Check if HTML files exist
    html_files = ['index.html', 'about.html']
    missing_files = []
    
    for file in html_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"Error: Missing HTML files: {', '.join(missing_files)}")
        print("Please ensure index.html and about.html are in the current directory.")
        sys.exit(1)
    
    # Create the server
    try:
        with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
            print(f"Solid Fishstick Model Railway Club Website Server")
            print(f"Serving at http://{HOST}:{PORT}/")
            print(f"Press Ctrl+C to stop the server")
            print()
            print("Available pages:")
            print(f"  - Home: http://{HOST}:{PORT}/")
            print(f"  - About: http://{HOST}:{PORT}/about.html")
            print()
            
            # Start serving requests
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"Error: Port {PORT} is already in use.")
            print(f"Please stop any other server using port {PORT} or modify the PORT variable in this script.")
        else:
            print(f"Error starting server: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()