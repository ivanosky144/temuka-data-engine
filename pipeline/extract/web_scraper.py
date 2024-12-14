import requests
from bs4 import BeautifulSoup
import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)