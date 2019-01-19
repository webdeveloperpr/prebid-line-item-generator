# #!/usr/bin/env python
# #
# # Copyright 2015 Google Inc. All Rights Reserved.
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #      http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.

# """This example creates a test network.
# You do not need to have an Ad Manager account to run this example, but you do
# need to have a Google account (created at
# http://www.google.com/accounts/newaccount if you currently don't have one) that
# is not associated with any other Ad Manager test networks. Once this network is
# created, you can supply the network code in your settings to make calls to
# other services.
# Alternatively, if you do not wish to run this example, you can create a test
# network at:
# https://dfp-playground.appspot.com
# """


# # Import appropriate modules from the client library.
# from googleads import ad_manager


# def main(client):
#   # Initialize appropriate service.
#   network_service = client.GetService('NetworkService', version='v201811')

#   # Create a test network.
#   network = network_service.makeTestNetwork()

#   # Display results.
#   print ('Test network with network code "%s" and display name "%s" '
#          'created.' % (network['networkCode'], network['displayName']))
#   print ('You may now sign in at '
#          'http://www.google.com/admanager/main?networkCode=%s'
#          % network['networkCode'])

# if __name__ == '__main__':
#   # Initialize client object.
#   ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage(GOOGLEADS_YAML_FILE)
#   main(ad_manager_client)
  

  # Import the library.
from googleads import ad_manager
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GOOGLEADS_YAML_FILE = os.path.join(ROOT_DIR, 'googleads.yaml')

# Initialize a client object, by default uses the credentials in ~/googleads.yaml.
client = ad_manager.AdManagerClient.LoadFromStorage(GOOGLEADS_YAML_FILE)

# Initialize a service.
network_service = client.GetService('NetworkService', version='v201811')

# Make a request.
current_network = network_service.getCurrentNetwork()

print 'Found network %s (%s)!' % (current_network['displayName'],
                                  current_network['networkCode'])