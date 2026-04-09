from contextvars import ContextVar

custom_value_ctx = ContextVar("custom_value_ctx", default=None)