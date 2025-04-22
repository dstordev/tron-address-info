#!/bin/bash

cd ..
export PYTHONPATH=.
python -m pytest src/tests/integration_test_on_address_info.py
