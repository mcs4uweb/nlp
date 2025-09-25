from dataclasses import dataclass
from typing import Optional

@dataclass
class PartnerStatus:
    partnerIdentifier: Optional[str] = None
    partnerName: Optional[str] = None
    partnerType: Optional[str] = None

@dataclass
class Status:
    partner: PartnerStatus
    partnerStatus: Optional[str] = None
    expectedCount: Optional[int] = 0
    receivedCount: Optional[int] = 0