# Live demo instructions

# Install Cpython

## Base - apt

???

## Pyenv

## UV

`curl -LsSf https://astral.sh/uv/install.sh | sh`
`uv python install 3.12`


# Venv

## UV

`uv venv --python 3.12`

# Project

## UV

`uv init <name>`



# tool configs

## Pyproject toml
```toml

[tool.ruff.lint]
select = ["C", "E", "F", "W"]
unfixable = ["F401"]
```

## Settings

```json

"mypy-type-checker.args": [
"--strict"
],
```