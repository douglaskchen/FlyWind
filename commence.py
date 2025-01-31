import subprocess
import time
import threading

get_aircraft_data_script = "/home/douglas/repos/FlyWind/getaircraftdata.py"


def run_python_script(script_path):
    """Run a Python script and print its output."""
    print(f"Running {script_path}...")
    result = subprocess.run(["python3", script_path], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_path}: {result.stderr}")
    else:
        print(f"Output from {script_path}: {result.stdout}")

def start_http_server(port=8000, directory="."):
    """Start the Python HTTP server."""
    print(f"Starting HTTP server on port {port}...")
    try:
        # Start the HTTP server
        server_process = subprocess.Popen(["python3", "-m", "http.server", str(port), "--directory", directory])
        return server_process
    except Exception as e:
        print(f"Error starting HTTP server: {e}")
        return None
    
def update_aircraft_data():
    while True:
        run_python_script(get_aircraft_data_script)
        # Add your code block here
        time.sleep(10)

def main():
    # Paths to the Python scripts
    get_wind_data_script = "/home/douglas/repos/FlyWind/getwinddata.py"

    # Run the Python scripts
    run_python_script(get_wind_data_script)
    run_python_script(get_aircraft_data_script)

    # Start the HTTP server
    http_server_process = start_http_server(port=8000, directory="/home/douglas/repos/FlyWind")

    thread = threading.Thread(target=update_aircraft_data)
    thread.daemon = True  # Daemonize the thread to ensure it exits when the main program exits
    thread.start()

    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Terminate the HTTP server on Ctrl+C
        if http_server_process:
            http_server_process.terminate()
        print("HTTP server stopped.")

if __name__ == "__main__":
    main()



# import os
# print("Current Working Directory:", os.getcwd())

# import http.server
# import socketserver

# class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def end_headers(self):
#         self.send_cache_headers()
#         super().end_headers()

#     def send_cache_headers(self):
#         self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, post-check=0, pre-check=0")
#         self.send_header("Pragma", "no-cache")

# PORT = 3000

# Handler = CustomHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print(f"Serving at port {PORT}")
#     httpd.serve_forever()