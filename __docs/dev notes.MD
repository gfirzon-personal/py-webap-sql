Uvicorn is the ASGI server that runs your FastAPI app, but it does not need to be 
imported or referenced in your code unless you want to run it programmatically (which is uncommon for most projects).

An ASGI server (Asynchronous Server Gateway Interface) is a server that runs Python web applications using the ASGI specification. ASGI is a modern standard for Python web servers and applications, designed to support both synchronous and asynchronous code, enabling features like WebSockets and long-lived connections.

Uvicorn is a popular ASGI server.
FastAPI apps are built to run on ASGI servers.

Summary:

ASGI is a standard interface between Python web apps and servers.
ASGI servers (like Uvicorn, Daphne, Hypercorn) run FastAPI and other modern Python web frameworks.
ASGI supports async features, unlike the older WSGI standard.

## Get ODBC drivers SQL Server
https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17