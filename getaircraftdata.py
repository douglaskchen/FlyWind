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
with open("/home/douglas/repos/FlyWind/aircraftdata.json", "w") as outfile:
    outfile.write(json_object)