import json
import logging.config

def load_logging_config(file='logging.json'):
    with open(file, 'r') as f:
        logging_config = json.load(f)

    logging.config.dictConfig(logging_config)