from googleads import ad_manager
import create_client

# Create the client
client = create_client.create()

# Initialize a service.
network_service = client.GetService('NetworkService', version='v201811')

# Make a request.
current_network = network_service.getCurrentNetwork()

print 'Found network %s (%s)!' % (current_network['displayName'], current_network['networkCode'])