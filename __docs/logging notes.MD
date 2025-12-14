Python’s logging module provides several **logging levels** to indicate the severity or importance of log messages. Here are the standard levels, from lowest to highest severity:

| Level      | Numeric Value | Description                                                                 |
|------------|--------------|-----------------------------------------------------------------------------|
| DEBUG      | 10           | Detailed information, useful for diagnosing problems (development only).     |
| INFO       | 20           | General events, confirmation that things are working as expected.            |
| WARNING    | 30           | An indication that something unexpected happened, but the program is working.|
| ERROR      | 40           | A more serious problem; the program may not be able to perform some function.|
| CRITICAL   | 50           | A very serious error; the program itself may be unable to continue running.  |

**Example usage:**
```python
import logging

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning")
logging.error("This is an error")
logging.critical("This is critical")
```

**How it works:**  
- When you set `logging.basicConfig(level=logging.INFO)`, only messages at INFO level and above (INFO, WARNING, ERROR, CRITICAL) will be shown.
- Lower levels (like DEBUG) will be ignored unless you set the level to `DEBUG`.

**Tip:**  
Use lower levels (DEBUG, INFO) for development and higher levels (WARNING, ERROR, CRITICAL) for production monitoring.

User: so if I set level to info, what levels of warnings would show up?

GitHub Copilot: If you set the logging level to `INFO`:

```python
logging.basicConfig(level=logging.INFO)
```

**The following log levels will be shown:**

- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`

**The `DEBUG` level will NOT be shown.**

**Summary:**  
Setting the level to `INFO` means all messages at `INFO` and higher severity (`WARNING`, `ERROR`, `CRITICAL`) will appear in your logs.