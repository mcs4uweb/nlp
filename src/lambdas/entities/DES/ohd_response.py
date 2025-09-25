from dataclasses import dataclass
from typing import List, Optional
from datetime import date

from entities.DES.status import Status

@dataclass
class Code:
    code: str
    primary: bool
    system: Optional[str] = None
    display: Optional[str] = None

@dataclass
class Identifier:
    assigningAuthority: Optional[str] = None
    id: Optional[str] = None

@dataclass
class Organization:
    name: Optional[str] = None
    ids: Optional[List[Identifier]] = None

@dataclass
class Address:
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    street: Optional[List[str]] = None
    type: Optional[str] = None

@dataclass
class DateRange:
    start: str
    end: str

@dataclass
class PersonName:
    last: Optional[str] = None
    first: Optional[str] = None
    raw: Optional[str] = None

@dataclass
class Telecom:
    value: Optional[str] = None
    useType: Optional[str] = None
    uriPrefix: Optional[str] = None

@dataclass
class OptIn:
    isOptIn: bool = False

@dataclass
class NextOfKin:
    name: PersonName
    addresses: Optional[List[Address]] = None
    telecoms: Optional[List[Telecom]] = None
    relationship: Optional[List[Code]] = None

@dataclass
class Sponsor:
    name: PersonName
    assignedUnit: Optional[Organization] = None
    rank: Optional[List[Code]] = None
    ssn: Optional[str] = None

@dataclass
class Demographics:
    dataDomain: List[Code]
    facility: Optional[Organization] = None
    recordId: Optional[Identifier] = None    
    repository: Optional[Organization] = None
    addresses: Optional[List[Address]] = None
    age: Optional[int] = None
    assignedUnit: Optional[Organization] = None
    birthDate: Optional[DateRange] = None
    deersEligibility: Optional[List[Code]] = None
    fmp: Optional[str] = None
    maritalStatus: Optional[List[Code]] = None
    name: Optional[PersonName] = None
    nextOfKin: Optional[List[NextOfKin]] = None
    optIn: Optional[OptIn] = None
    patientCategory: Optional[List[Code]] = None
    patientId: Optional[List[Identifier]] = None
    telecoms: Optional[List[Telecom]] = None
    race: Optional[List[List[Code]]] = None
    rank: Optional[List[Code]] = None
    religion: Optional[List[Code]] = None
    sex: Optional[List[Code]] = None
    sponsor: Optional[Sponsor] = None


@dataclass
class DataList:
    demographics: List[Demographics]

@dataclass
class DemographicsRootResponse:
    dataList: DataList
    queryComplete: bool
    statusList: List[Status]