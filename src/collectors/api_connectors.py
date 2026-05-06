from dataclasses import dataclass
from typing import List

@dataclass
class URLCandidate:
    url: str
    source_type: str
    reason: str

def auto_collect_urls() -> List[URLCandidate]:
    return [URLCandidate(url="https://www.sec.gov/edgar/search/", source_type="sec_edgar", reason="SEC EDGAR検索")]
