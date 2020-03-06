.PHONY: doctest

virtualenv: create_venv update_venv

create_venv:
	if [ -n "${VIRTUAL_ENV}" ]; then echo "you appear to already be in a venv. To update it, run 'make update_venv'" && exit 1; fi
	python3.6 -m virtualenv -p "$(which python3.6)" --prompt '|> trade-prom <| ' venv
	venv/bin/pip install -r requirements.txt
	venv/bin/pip install -r requirements-dev.txt

update_venv:
	venv/bin/pip install -r requirements.txt
	venv/bin/pip install -r requirements-dev.txt
