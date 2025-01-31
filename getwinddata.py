import subprocess
import os
from datetime import datetime, timedelta

# Function to get the closest past UTC time based on UTC-5
def get_closest_past_utc_time():
    now = datetime.utcnow() - timedelta(hours=5)  # Adjust to UTC-5
    closest_time = now - timedelta(hours=now.hour % 6)  # Round down to the nearest 6-hour interval
    return closest_time.strftime("%Y%m%d"), closest_time.strftime("%H")

# Get the current date and closest past UTC time
date, hour = get_closest_past_utc_time()

# Construct the URL
url = (
    f"https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_1p00.pl?"
    f"file=gfs.t{hour}z.pgrb2.1p00.f000&"
    f"lev_10_m_above_ground=on&var_UGRD=on&var_VGRD=on&"
    f"leftlon=0&rightlon=360&toplat=90&bottomlat=-90&"
    f"dir=%2Fgfs.{date}%2F{hour}%2Fatmos"
)

# Download the GRIB2 file using curl
curl_command = ["curl", url, "-o", "winddata"]
subprocess.run(curl_command, check=True)

# Change to the grib2json bin directory
grib2json_bin_dir = "/home/douglas/repos/FlyWind/grib2json-0.8.0-SNAPSHOT/bin"  # Update this path
os.chdir(grib2json_bin_dir)

# Convert the GRIB2 file to JSON using grib2json
grib2json_command = [
    "./grib2json",  # Execute grib2json from the current directory
    "-d", "-n", "-o", "../../winddata.json", "../../winddata"
]
subprocess.run(grib2json_command, check=True)

print("Data downloaded and converted successfully!")