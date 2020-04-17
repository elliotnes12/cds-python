import os

class Constant(object):
    """Services"""

    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PROJECT_DIR = os.path.dirname(os.path.abspath(__file__)) 
    DATA_ROOT = os.path.join(PROJECT_DIR, "data")

    COUNTRY_SERVICE: str = "countryService"
    CHARID_SERVICE: str = "charIdService"

    CONFIG_PATH = DATA_ROOT + '/data-distiller-audit/services.json'

    PATH_METADATA = '/data/app/{environment}/stormbreaker/data/joe/ready/' \
                   '{country_id}/{client_id}/{output}/{period}/METADATA.csv'