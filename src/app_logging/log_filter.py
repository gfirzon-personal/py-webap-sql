# log_filter.py
import logging
from .context import custom_value_ctx

class CustomDimensionFilter(logging.Filter):
    def filter(self, record):
        value = custom_value_ctx.get()
        record.custom_dimensions = {"correlation_id": value}
        return True