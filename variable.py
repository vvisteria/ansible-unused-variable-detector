#!/usr/bin/env python3
import yaml
import fileutil

def variable_list(directory):
  pathlist = fileutil.vars_yml(directory)
  keys = []

  for path in pathlist:
    with open(path, 'r+') as file:
      data = yaml.safe_load(file)
      keys.extend(data.keys())

  return keys
