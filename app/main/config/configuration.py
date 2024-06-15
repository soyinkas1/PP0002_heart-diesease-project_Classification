from app.utils.common import read_yaml, create_directories
from app.main.config.config_entity import DataIngestionConfig
import os
from app.main.config.constant import *

basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigurationManager:

    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH, params_filepath=PARAM_FILE_PATH):
        self.config = read_yaml(config_filepath) 
        self.params = read_yaml(params_filepath)
       
       create_directories(self.config.artifacts_roots)
        