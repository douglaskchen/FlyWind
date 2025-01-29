import json

from opensky_api import OpenSkyApi

api = OpenSkyApi()
# bbox = (min latitude, max latitude, min longitude, max longitude)
states = api.get_states(bbox=(43.516689, 43.790924, -79.856186, -79.372101))

# for s in states.states:
#     print(s)

# Convert StateVector objects to dictionaries
state_dicts = [s.__dict__ for s in states.states]

json_object = json.dumps(state_dicts, indent=4)
 
# Writing to sample.json
with open("/home/douglas/repos/FlyWind/sample.json", "w") as outfile:
    outfile.write(json_object)




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
