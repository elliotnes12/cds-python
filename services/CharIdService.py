from abstract.AbstractService import AbstractService
import pandas as pd
import os.path as path
from abstract.constant import Constant
from abstract.encode_generator import read_json_config,put_json


class CharIdService(AbstractService):
    
    def getCharId(self,args):
        
        INPUT_PATH = Constant.PATH_METADATA.format(
            environment=args['env'],
            country_id=args['countryId'],
            client_id=args['clientId'],
            output=args['output'],
            period=args['period'])
            
        chars = []

        if path.exists(INPUT_PATH):
          
           dataFrame = pd.read_csv(INPUT_PATH);
           dim_photo = dataFrame['DIM_ID'][dataFrame['DATAFACT_DSC'] == 'PHOTO']
           
           for dim in dim_photo:
               file_char = 'DIM_{}_CHAR.csv'.format(dim)
               dataframeTwo = pd.read_csv(INPUT_PATH+'\\'+file_char);   
               try:
                form = dataframeTwo['CHAR_ID'][dataframeTwo['CHAR_TYPE'] == 'element']
                for l in form:
                    chars.append("{dim:'%s',chartId:'%s'}" %(dim,l))
               except Exception:
                    chars.append("{dim:'%s',chartId:'%s'}" %(dim,''))

        put_json(chars)
     