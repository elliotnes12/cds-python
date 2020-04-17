import services.service as sv
import argparse
from abstract.constant import Constant
from abstract.AbstractService import AbstractService as AbscIn
import services.CharIdService as CharSv


class Handler(object):
    """
      Service Handler 
      Abstract factory pattern
    """
    __args = None
  

    def __init__(self):
        """
            Constructor: set parameters
        """


        parser = argparse.ArgumentParser()
        parser.add_argument('--service_name',
                            choices=['countryService','charIdService'],
                            default='charIdService',
                            help='Service Name',
                            type=str,
                            required=True)

        parser.add_argument('-actionMethod',
                            '--actionMethod',
                            help='Method',
                            type=str,
                            required=True)

        parser.add_argument('-e',
                            '--env',
                            choices=['dev', 'qa', 'qa-int', 'uat', 'prod'],
                            default='uat',
                            help='Environment',
                            type=str,
                            required=True)

        parser.add_argument('-country',
                            '--countryId',
                            help='Country ID or countryAbbvName',
                            type=str,
                            required=False)

        parser.add_argument('-clientId',
                            '--clientId',
                            help='Client ID or clientAbbvName',
                            type=str,
                            required=False)

        parser.add_argument('-clientInstr',
                            '--clientInstr',
                            help='instructionAbbvName',
                            type=str,
                            required=False)

        parser.add_argument('-output',
                            '--output',
                            help='Ouput ID',
                            type=str,
                            required=False)

        parser.add_argument('-period',
                            '--period',
                            help='Period',
                            type=str,
                            required=False)

        self.__args = vars(parser.parse_args())

    def factory(self):
        """
           Factory method
        """
        factory:AbstractService = None
        if self.__args['service_name'] in Constant.CHARID_SERVICE:
           factory = CharSv.CharIdService();   
        if self.__args['service_name'] in Constant.COUNTRY_SERVICE:
           factory = sv.Service(self.__args['service_name']);
       
        factory.init(self.__args) 

if __name__ == '__main__':
    handler: Handler = Handler()
    handler.factory()
