# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created by CWENG at 2020-11-04
Current project: VeldiPython


"""
import logging.config
import os
import yaml

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
CFG_DIR = os.path.join(CURR_DIR, "..", "cfg")
LOG_CONFIG_PATH = os.path.join(CFG_DIR, "log_config.yaml")

print(LOG_CONFIG_PATH)
with open(LOG_CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
