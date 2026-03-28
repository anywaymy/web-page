import logging
from pathlib import Path
from fastapi.templating import Jinja2Templates


BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"


templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("web.log", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )