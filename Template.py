import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    r"D:\Medical-Chatbot-Generative-AI\somefolder\__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "Template.py",
    "research/trails.ipynb"
]

for file in list_of_files:
    p = Path(file)
    if not p.is_absolute():
        p = (Path.cwd() / p).resolve()

    folder = p.parent
    name = p.name

    if folder != Path.cwd():
        folder.mkdir(parents=True, exist_ok=True)
        logging.info(f"Ensured folder: {folder} for file: {name}")

    if not p.exists() or p.stat().st_size == 0:
        p.touch(exist_ok=True)
        logging.info(f"Created empty file: {p}")
    else:
        logging.info(f"Already exists: {p}")
