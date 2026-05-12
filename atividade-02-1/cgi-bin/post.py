#!/usr/bin/env python3

import os
import sys
from datetime import datetime
from urllib.parse import parse_qs

content_length = int(os.environ.get("CONTENT_LENGTH", 0))
body = sys.stdin.buffer.read(content_length).decode("utf-8")

params = parse_qs(body, encoding="utf-8")

author = params.get("nome", [""])[0]
message = params.get("mensagem", [""])[0]

# generate timestamp
timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

try:
    with open("database.txt", "r", encoding="utf-8") as f:
        database_content = f.read()
except FileNotFoundError:
    database_content = ""

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

# save the new post at the beginning of the database file
with open("database.txt", "w", encoding="utf-8") as f:
    f.write(f"""
      <li>
      <div>
        <strong>{author}</strong> <em>{timestamp}</em>
        <div>{message}</div>
      </div>
      </li>\n{database_content}
      """)

print("Content-Type: text/html; charset=utf-8")
print("Location: /get.py")
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
       <input type="submit" value="Run">
    </form>

    <h2>Posts:</h2>
    <ul>
    <div>
      <strong>{author}</strong> <em>{timestamp}</em>
      <div>{message}</div>
    </div>
      {database_content}
    </ul>
  </body>
  </html>
  """)
