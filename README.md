# detect-disaster-tweets-superdata76

# Getting Started
## Dependencies
python3
docker

## Test Data
Assumes `./slalombuilddatacontest/` exists with required CSV files:
```
ll ./slalombuilddatacontest/
test.csv
train.csv
```

# Testing
Install pytest: `pip3 install pytest`

`./test`
or 
`pytest -v test_main.py`
## test_main.py
Executes a suite against `main.py`, will eventually validate result CSV is created.

