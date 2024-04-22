### virtual python3 ENV
1. Create virtual ENV → `python3 -m venv .venv`
2. Activate → `source .venv/bin/activate`
3. Deactivate → `deactivate` or reopen terminal session


### Run tests
A simple way: `python3 -m unittest discover -s ./tests`

Or beauti → run this: `pytest ./tests`

Prerequarements for beauti tests run:
    * `pip3 install pytest`
    * `export PYTHONPATH="$PWD:$PYTHONPATH"`


### Alpacas Python SDK

The pypi.org [start page](https://pypi.org/project/alpaca-py/).

Oficial Alpacas [documentation about alpaca-py](https://alpaca.markets/sdks/python/getting_started.html).

### Alpacas Tradin API
Start learn from [About Trading API](https://docs.alpaca.markets/docs/trading-api)