# -*- coding: utf-8 -*-

import logging
import logstash

logstash_conf = {"host": "localhost", "port": 5000}


class LogstashLogger:
    def __init__(self):
        pass

    def get_logger():
        logger = logging.getLogger()

        logger.setLevel(logging.INFO)

        if logger.hasHandlers():
            return logger

        logger.addHandler(
            logstash.TCPLogstashHandler(
                logstash_conf["host"], logstash_conf["port"], version=1
            )
        )
        logger.addHandler(logging.StreamHandler())

        return logger


log = LogstashLogger().get_logger()
