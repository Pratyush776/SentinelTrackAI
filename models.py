from typing import List, Optional
from beanie import Document, Link
from pydantic import BaseModel

class Department(Document):
    name: str 
    risk_level: str
    class Settings:
        name = "departments"

class Attacker(Document):
    ip_address: str
    country: str
    class Settings:
        name = "attackers"

class Alert(Document):
    threat_type: str  
    severity: str
    target_department: Link[Department]
    source_attacker: Link[Attacker]
    class Settings:
        name = "alerts"

class ForensicReport(Document):
    payload_dump: str
    mitre_attack_id: str
    class Settings:
        name = "forensic_reports"

class Incident(Document):
    title: str
    status: str  
    report: Optional[Link[ForensicReport]] = None
    associated_attackers: Optional[List[Link[Attacker]]] = []
    class Settings:
        name = "incidents"