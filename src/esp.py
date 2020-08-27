#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys,os
import pathlib
import importlib

def _import_module(expdir: pathlib.Path):
    """
    @TODO: Docs. Contribution is welcome
    """
    # @TODO: better PYTHONPATH handling
    if not isinstance(expdir, pathlib.Path):
        expdir = pathlib.Path(expdir)
    sys.path.insert(0, str(expdir.absolute()))
    sys.path.insert(0, os.path.dirname(str(expdir.absolute())))
    s = importlib.util.spec_from_file_location(
        expdir.name,
        str(expdir.absolute() / "__init__.py"),
        submodule_search_locations=[expdir.absolute()],
    )
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    sys.modules[expdir.name] = m
    return m 

print(os.getenv('PYTHONPATH'))

# esphome = _import_module('./esphome/esphome')
import esphome
from esphome.__main__ import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    ret = main()
    sys.exit(ret)
