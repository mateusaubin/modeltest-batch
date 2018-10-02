#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
import time
import os
import subprocess

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s | %(message)s'
)
logger = logging.getLogger()

phyfilepath = sys.argv[1]

time.sleep(2)
logger.debug('buga {} buga'.format(phyfilepath))

time.sleep(2)
logger.info('tamo no docker?')

time.sleep(2)
logger.warning('avizao')

time.sleep(2)
logger.error('errado {} errado'.format(phyfilepath))

time.sleep(2)
logger.critical('ja era')

cwd = os.getcwd()
logger.critical(cwd)

retry = os.getenv("AWS_BATCH_JOB_ATTEMPT", -1)
logger.info("Retry={}".format(retry))


cmdline_args = [os.path.join(cwd, 'lib', 'phyml'), ]
cmdline_args.extend(['-i', 'tmp/big.phy'])
cmdline_args.extend("-d nt -n 1 -b 0 --run_id GTR+I+G -m 012345 -f m -v e -c 4 -a e --no_memory_check --r_seed 12345 -o tlr -s BEST".split())

trace_file = os.path.join(
            cwd,
            'tmp/',
            "trace_{}.log".format('jmodel_runid')
        )

with open(trace_file, "w") as file:
    result = subprocess.run(cmdline_args,
                            stdout=file,
                            stderr=subprocess.STDOUT)

logging.warn("PhyML.ReturnCode={}".format(result.returncode))
resultfiles = [x for x in os.listdir(os.path.join(cwd, 'tmp/')) if x != "_input"]
# debug por enquanto
logging.info(resultfiles)

# bail out if phyml error'd
# TODO: assert a existência dos 3 arquivos [ {filenamewithext}_phyml_stats_{run_id}, {filenamewithext}_phyml_tree_{run_id}, trace.log ]
processData = subprocess.run(
    ["cat", trace_file], 
    stdout=subprocess.PIPE
)
logging.error(processData.stdout.decode('UTF-8'))

if result.returncode != 0:    

    raise subprocess.SubprocessError("Error calling PhyML")

logger.critical('EH TETRAAAAAAA!!!!!!')
