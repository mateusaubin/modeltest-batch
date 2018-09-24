#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-15s | %(levelname)-8s | %(message)s'
)
logger = logging.getLogger()

print('helo')

time.sleep(2)
logger.debug('buga buga buga')

time.sleep(2)
logger.info('tamo no docker?')

time.sleep(2)
logger.warning('avizao')

time.sleep(2)
logger.error('errado')

time.sleep(2)
logger.critical('ja era')

time.sleep(2)
print('goodbye')
