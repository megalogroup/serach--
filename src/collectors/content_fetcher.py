import requests
from bs4 import BeautifulSoup
from readability import Document

def fetch_article(url: str, timeout: int = 20) -> tuple[str, str]:
    res = requests.get(url, timeout=timeout)
    res.raise_for_status()
    doc = Document(res.text)
    soup = BeautifulSoup(doc.summary(), "html.parser")
    text = "\n".join(line.strip() for line in soup.get_text("\n").splitlines() if line.strip())
    return (doc.short_title() or url, text)
