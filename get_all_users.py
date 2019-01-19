# Import appropriate modules from the client library.
from googleads import ad_manager
import create_client

def main(client):
  # Initialize appropriate service.
  user_service = client.GetService('UserService', version='v201811')

  # Create a statement to select users.
  statement = ad_manager.StatementBuilder(version='v201811')

  while True:
    response = user_service.getUsersByStatement(statement.ToStatement())

    if 'results' in response and len(response['results']):
      for user in response['results']:
        print('User with Id "%d", name "%s", roleId "%s" was found.\n' 
        % (user['id'], user['name'], user['roleId'])) 
        statement.offset += statement.limit
    else:
      break

    print ('\nNumber of results found: %s' % (response['totalResultSetSize']))


if __name__ == '__main__':
  # Initialize client object.
  main(create_client.create())