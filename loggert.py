# Author: Zaher Abdul Azeez
# Tagline: It is better to burn out than to fade away

# Date: 2017-12-27
# Subject: Generic logging module for cerebro

import logging

logger = logging.getLogger("TARS")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.propogate = False