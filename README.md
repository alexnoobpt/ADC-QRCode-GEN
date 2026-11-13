# Captchas gen

A CAPTCHAS GEN project.

## Structure

```
QRCODE-GEN/
├── client/
   ├── src/
      ├── __init__.py
│      └── app.py
├── database/
│  
├── tests/
│   ├── __init__.py
│   └── test_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate    
pip install -r requirements.txt
```

## Run

```bash
python -m src.app
```

## Test

```bash
pip install pytest
pytest
```

## Git Workflow

All work goes through the `develop` branch. Do not commit directly to `main` or `develop`.

1. **Create a branch from `develop`**
   ```bash
   git checkout develop
   git pull
   git checkout -b feature/your-feature-name
   ```
2. **Open a Pull Request into `develop`** once your changes are ready.
3. **Merge into `develop`** only after the PR has been reviewed and approved.
4. **Merge `develop` into `main`** as the final step, once everything on `develop` is complete and stable.
