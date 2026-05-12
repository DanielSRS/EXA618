#!/usr/bin/env python3
import os
from urllib.parse import parse_qs

try:
    with open("database.txt", "r", encoding="utf-8") as f:
        database_content = f.read()
except FileNotFoundError:
    database_content = "No data available."

# get index.css file content
try:
    with open("index.css", "r", encoding="utf-8") as f:
        css_content = f.read()
except FileNotFoundError:
    css_content = ""


try:
    with open("reset.css", "r", encoding="utf-8") as f:
        rcss_content = f.read()
except FileNotFoundError:
    rcss_content = ""

print("Content-type: text/html;charset=utf-8")
print()
print(f"""
  <html>
  <head>
  <title>Teste CGI POST</title>
  <style>
  {rcss_content}
  </style>
  <style>
  {css_content}
  </style>
  </head>
  <body>
    <form method="POST" action="http://localhost:8000/cgi-bin/post.py" accept-charset="UTF-8">
       Nome: <input type="text" size="15" name="nome">
       Message: <input type="text" size="300" name="mensagem">
       <br />
       <input type="submit" value="Run">
    </form>

    <h2><a href="http://localhost:8000/cgi-bin/get.py">Posts:</a></h2>
    <ul>
      {database_content}
    </ul>
  </body>
  </html>
  """)
