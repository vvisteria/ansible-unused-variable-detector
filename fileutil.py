#!/usr/bin/env python3
import pathlib
import magic
import os

def vars_yml(directory):
  patterns = (
    'host_vars/*.yml',
    'group_vars/*.yml',
    'roles/*/tasks/vars/*.yml',
    'roles/*/defaults/*.yml',
    'vars/*.yml',
  )

  return yml_list(directory, patterns)

def yml_list(directory, patterns):
  files = []

  for pat in patterns:
    path = pathlib.Path(directory)
    files.extend(list(path.glob(pat)))

  return files

def all_file(directory):
  path = pathlib.Path(directory)
  return [ x for x in list(path.glob("**/*")) if os.path.isfile(x) ]

def read_text(file):
  mime = magic.from_file(str(file.absolute()), mime=True)
  # print('file: %s, mime: %s, result: %s' % (str(file), mime, "text/" not in mime))
  if ("text/" not in mime) and ("/json" not in mime):
    return None

  body = file.read_text()

  return body