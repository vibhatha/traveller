#!/bin/bash
# format.sh
autoflake --in-place --remove-all-unused-imports --recursive .
isort .
black .
autopep8 --in-place --aggressive --aggressive --recursive .
