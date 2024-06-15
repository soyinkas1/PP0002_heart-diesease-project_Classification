from app.utils.common import read_yaml, create_directories
from app.main.config.config_entity import DataIngestionConfig
import os
from app.main.constants import *

basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigurationManager:

    def __init__(self,config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath) 
        # self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(   
        root_dir=config.root_dir,
        n_rows=config.n_rows,
        raw_data_path=config.raw_data_path,
        loaded_data_path=config.loaded_data_path,
        chunk_size=config.chunk_size

        )

        return data_ingestion_config