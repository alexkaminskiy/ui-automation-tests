#!/bin/bash
export PYTHONPATH=$(pwd)
pytest -n auto --dist loadscope -vv -s --alluredir=/tests/reports
mkdir -p allure-report/history