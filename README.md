# python-server-template

A very simple client/server setup using Python's `http.server`.

The default setup takes input from a HTML form and makes an AJAX request to the server. The server parses the
data into a Python dict, then back into JSON, then simply echos the JSON back to the client which displays the
parameters in a table.

Run `server.py`, then navigate to http://localhost:8000.
