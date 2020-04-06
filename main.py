#!/usr/bin/env python3
import fileutil
import search
import variable
import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-r', '--root-dir', action='store', type=str, help='playbook root dir', required=True)
  args = parser.parse_args()

  files = fileutil.all_file(args.root_dir)
  variables = variable.variable_list(args.root_dir)

  result = search.search_all(variables, files)