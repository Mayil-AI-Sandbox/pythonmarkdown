import markdown

somemd = """
# Mayil

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/NobleMathews/35f2b25f164a1eacbec260abb0788aaf/raw/pytest-coverage-comment__main.json)



## Run Mayil locally:

### Dashboards

- Redis: http://localhost:8001/redis-stack/browser
- Milvus (Attu): http://localhost:8000/#/connect
- Vault: http://localhost:8200/ui

### Build Mayil

```bash
    docker build -t mayil --platform linux/arm64 --build-arg IMAGE_IDENTIFIER="$(date +%Y%m%d-%H%M%S):$(git rev-parse --short HEAD)" .
```

### Run Milvus locally

```bash
            docker-compose -f ./test_utils/local_test_setup/docker-compose.yml up -d
```

    Database files for the local run will be saved to `./test_utils/milvus_test_setup/test_volumes`. Do not delete this folder if you want to persist data.


"""

html = markdown.markdown("", tab_length=12)
print("|", html, "|")
print("---------------------------------")