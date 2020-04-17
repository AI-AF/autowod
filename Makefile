SHELL=/bin/bash

install-env:
	conda create -n autowod python=3.7
	source activate autowod && pip install -r requirements.txt && conda install ipykernel && python -m ipykernel install --user --name autowod --display-name "autowod"

uninstall-env:
	conda remove --name autowod --all