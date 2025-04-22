#!/bin/bash

cd ..
export PYTHONPATH=.
python -m pytest src/tests/unittest_db.py
