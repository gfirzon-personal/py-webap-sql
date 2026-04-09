# logging_config.py
import os
import logging
from .log_filter import CustomDimensionFilter

class CustomFormatter(logging.Formatter):
    def format(self, record):
        base = super().format(record)
        # Add correlation_id if present
        if hasattr(record, "custom_dimensions"):
            base += f" | correlation_id={record.custom_dimensions.get('correlation_id')}"
        return base

def setup_logging():
    logger = logging.getLogger()  # root logger

    file_handler = logging.FileHandler("app.log")
    file_handler.addFilter(CustomDimensionFilter())
    formatter = CustomFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Ensure all StreamHandlers use UTF-8 encoding
    for handler in logger.handlers:
        if isinstance(handler, logging.StreamHandler):
            handler.stream.reconfigure(encoding='utf-8')        

    logger.setLevel(logging.INFO)