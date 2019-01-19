import os
from googleads import ad_manager

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GOOGLEADS_YAML_FILE = os.path.join(ROOT_DIR, 'googleads.yaml')


def create():
    return ad_manager.AdManagerClient.LoadFromStorage(GOOGLEADS_YAML_FILE)
