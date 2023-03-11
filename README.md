# 🦴 Python `functions-framework` Skeleton

Quickstart skeleton for new serverless functions using `functions-framework` for Python.

## 🌟 Features

- well-prepared `.gitignore` to get started quickly and keep your repository clean
- `pre-commit` config to keep a tidy repository, which include:
  - formatting using `black`
  - fixing files using stock `pre-commit` hooks
  - running `bandit` for security tests
  - linting code using `pylint`
  - keeping hooks updated using `pre-commit autoupdate`
- separated `requirements.txt` files for development and production
- dedicated `app/` directory to separate application logic from the rest of the repository
- prepared `pytest` skeleton and HTTP request fixture
  - including measurement of unit test coverage using `coverage` with a pre-configured `.coveragerc`

## 📦 Installation

```bash
# clone the repository
git clone git@github.com:torbendury/py-functions-framework-skeleton.git

# move into the fresh clone
cd py-functions-framework-skeleton

# OPTIONAL: remove the git history to start from zero
# rm -rf .git/

# Install everything to get up and running
python -m venv venv
source venv/bin/activate

pip install -r requirements-dev.txt

pre-commmit install
pre-commit run -a
```

## 👷 Usage/Examples

To run the application locally, start it with `functions-framework`:

```bash
functions-framework --target entrypoint --debug
```

To run the tests written with `pytest`, run:

```bash
pytest
```

To gain more insights on unit test coverage, run:

```bash
coverage run -m pytest
coverage report -m
```
