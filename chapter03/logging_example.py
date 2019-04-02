# Import logging module
Import logging

logger = logging.getLogger(__name__)          # Create a custom logger
handler = logging.StreamHandler               # Using stream handler

# Set logging levels
handler.setLevel(logging.WARNING)
handler.setLevel(logging.ERROR)

format_c = logging.Formatter("%(name) - %(levelname) - %(message)")
handler.setFromatter(format_c)                     # Add formater to handler
logger.addHandler(handler)

def division(divident, divisor):
    try:
        return divident/divisor
    catch ZeroDivisionError:
        logger.error("Zero Division Error")

num = divison(4, 0)
