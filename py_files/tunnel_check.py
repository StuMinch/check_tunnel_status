import requests
import os
import sys

username = os.environ.get("SAUCE_USERNAME")
access_key = os.environ.get("SAUCE_ACCESS_KEY")

def get_tunnel_list(username, access_key):
   url = f"https://api.us-west-1.saucelabs.com/rest/v1/{username}/tunnels?full=true"
   try:
       response = requests.get(
           url,
           auth=(username, access_key),
           headers={"Content-Type": "application/json"}
       )
       response.raise_for_status()
       output = response.json()
       if output[0]["tunnel_identifier"] == "docker-compose-tunnel" and output[0]["is_ready"] == False:
          print("Tunnel " + output[0]["tunnel_identifier"] + " is ready = " + str(output[0]["is_ready"]))
          sys.exit(1)
       else: print("Tunnel " + output[0]["tunnel_identifier"] + " is ready = " + str(output[0]["is_ready"]))
       sys.exit(0)
   
   except requests.exceptions.RequestException as error:
          print(f"Error occurred: {error}")
          return

   


get_tunnel_list(username, access_key)

