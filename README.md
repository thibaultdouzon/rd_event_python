# Live demo instructions

# Install Cpython

`curl -LsSf https://astral.sh/uv/install.sh | sh`
`uv python install 3.12`

# Venv

`uv venv --python 3.12`

# Project

`uv init <name>`

Pour un projet existant

`uv sync`

# tool configs

## Pyproject toml

Ruff supprime les imports inutilisés

```toml

[tool.ruff.lint]
select = ["C", "E", "F", "W"]
unfixable = ["F401"]
```

## Settings

```json
{
  "notebook.formatOnSave.enabled": true,
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

## Additional steps

- `uv add pip` not everyone use exclusively uv, installing the default package manager is important
- `mypy --install-types` to automatically install mypy extensions for dependencies you are using

# Presentation

- sshd -D &
- connect vscode (root@localhost:8022, mot de passe root)
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
