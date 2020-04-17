import os.path as path
from abstract.encode_generator import read_json_config,put_json
import pandas as pd
import logging
from abstract.constant import Constant
from abstract.AbstractService import AbstractService
import os.path as path

class Service(AbstractService):
    __json_response = None
    __key_service = ''
    logging.basicConfig(level=logging.DEBUG)
    
    def __init__(self, service: str):
        self.__key_service = service

    """
      param args: array arguments
      return: boolean   
    """

    def getClientInstruction(self,args):
        if path.exists(Constant.CONFIG_PATH):
           json = read_json_config(Constant.CONFIG_PATH)[self.__key_service]

           if args['countryId'] and args['clientId'] and args['clientInstr']:
              for obj in json:
                if(obj['countryAbbvName'] in args['countryId']):
                   for obj_cli in obj['clients']:
                       if(obj_cli['clientAbbvName'] in args['clientId']):
                          for instruction in obj_cli['instructions']:
                              if(instruction['instructionAbbvName'] in args['clientInstr']):
                                 return put_json({'response':True})
                          
           return put_json({'response':False})
        else:
           raise Exception(" Not found file : general_config.json ")

    def country_service(self,args):
        if path.exists(Constant.CONFIG_PATH):
            put_json(read_json_config(Constant.CONFIG_PATH)[self.__key_service])
            return True
        else:
           raise Exception(" Not found file : general_config.json ")
