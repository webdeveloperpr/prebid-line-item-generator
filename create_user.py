#!/usr/bin/env python

from googleads import ad_manager
import os
import create_client

"""
  This file allows you to create users.
"""


def main(client, email, name):
    user_service = client.GetService('UserService', version='v201811')

    # Create a new user
    users = [
        {
            'name': name,
            'email': email
        }
    ]

    for user in users:
        user['roleId'] = -1

    users = user_service.createUsers(users)

    for user in users:
        print('Users with id "%s", email "%s", and role "%s", was created.'
              % (user['id'], user['email'], user['role']))


if __name__ == '__main__':
    NEW_USER_EMAIL = 'webdeveloperpr@gmail.com'
    NEW_USERNAME = 'Luis Betancourt'
    main(create_client.create(), NEW_USER_EMAIL, NEW_USERNAME)
