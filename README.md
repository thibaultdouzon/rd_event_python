# Live demo instructions

# Install Cpython

## Base - apt

???

## Pyenv

`curl https://pyenv.run | bash`

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

## Additional steps

- `uv add pip` not everyone use exclusively uv, installing the default package manager is important
- `mypy --install-types` to automatically install mypy extensions for dependencies you are using


# Presentation

- sshd -D &
- connect vscode
- Install uv
- source new shell
- uv init
- uv add ruff mypy
- install vscode extensions
  - python
  - ruff
  - mypy
  - (pylance)
- add local vscode configs
```json
{
    "[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.fixAll": "explicit",
            "source.organizeImports": "explicit"
        },
        "editor.defaultFormatter": "charliermarsh.ruff"
    },
    "mypy-type-checker.args": [
        "--strict"
    ]
}
``` 
