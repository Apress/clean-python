def division(dividend, divisor):
    """Perform airthmetic division."""
    try:
        return dividend/divisor
    except ZeroDivisionError as zero:
        raise ZeroDivisionError("Please provide greater than 0 value")
