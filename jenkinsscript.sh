#!/bin/bash

set -e

echo "#### Setting up Python environment ####"
pyenv global 3.10.12
python3 -m venv myenv
source myenv/bin/activate

echo "#### Installing requirements ####"
pip install -r requirements.txt
pip install pytest-cov

echo "#### Running tests ####"
mkdir -p xmlReport
pytest --cov=main utests --junitxml=./xmlReport/output.xml
python -m coverage xml
