import logging

a = 90
b = 0

try:
    c = a / b
except Exception as e:
    logging.error("Exception ", exc_info=True)
