import os
import argparse
import logging
import logging.config

from common.config import Config
from logconf import LOGGING


class ArgumentParser(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Baboon ! Ook !')
        parser.add_argument('--path', dest='path',
                            default=os.getcwd(),
                            help='Specify the path you want to monitor')
        parser.add_argument('--config', dest='configpath',
                            help='Override the default location of the \
                                config file')
        # logging args
        parser.add_argument('-d', '--debug', help='set logging to DEBUG',
                            action='store_const',
                            dest='loglevel',
                            const=logging.DEBUG,
                            default=logging.INFO)

        self.args = parser.parse_args()


config = Config(ArgumentParser(), LOGGING)