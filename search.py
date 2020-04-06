#!/usr/bin/env python3
import fileutil
import re

def search_all(variables, files):
  result = {}
  for var in variables:
    result[var] = search_files(var, files)
    print("variable: %s, result: %s" % (var, result[var]))

  return result

def search_files(variable_name, files):
  for f in files:
    if search_file(variable_name, f):
      return True

  return False

def search_file(variable_name, file):
  body = fileutil.read_text(file)
  if body is None:
    return False

  return re.search(variable_name + '[^:]', body)
