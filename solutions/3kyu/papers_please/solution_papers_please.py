"""https://www.codewars.com/kata/59d582cafbdd0b7ef90000a0"""

import re
from collections import defaultdict
from typing import TypeVar

DESTINATION_COUNTRY = 'Arstotzka'
Doc = TypeVar('Doc', bound='Document')


class Document:
    id: str = None
    nation: str = None
    name: str = None
    exp: str = '9999.12.31'
    dob: str = None
    document_name: str = None

    @classmethod
    def get_document_underscore_name(cls):
        return cls.document_name.replace(' ', '_')


class Passport(Document):
    sex: str = None
    iss: str = None
    document_name = 'passport'


class AccessPermit(Document):
    purpose: str = None
    duration: str = None
    height: str = None
    weight: str = None
    document_name = 'access permit'


class AsylumGrant(Document):
    height: str = None
    weight: str = None
    document_name = 'grant of asylum'


class DiplomaticAuthorization(Document):
    access: str = None
    document_name = 'diplomatic authorization'


class IdCard(Document):
    height: str = None
    weight: str = None
    nation = DESTINATION_COUNTRY
    document_name = 'ID card'


class VaccinationCertificate(Document):
    vaccines: str = None
    document_name = 'certificate of vaccination'


class WorkPass(Document):
    field: str = None
    document_name = 'work pass'


class Immigrant:
    def __init__(self):
        self.documents: list[Document] = []

    def add_document(self, doc_type: type, doc_info: str) -> None:
        doc = doc_type()

        for entry in doc_info.split('\n'):
            key, value = entry.split(': ')
            if key == 'ID#':
                key = 'id'
            setattr(doc, key.lower(), value)

        self.documents.append(doc)

    def find_document(self, doc_type: type[Doc]) -> Doc | None:
        return next((doc for doc in self.documents if isinstance(doc, doc_type)), None)

    def get_nationality(self) -> str | None:
        return next((doc.nation for doc in self.documents if hasattr(doc, 'nation')), None)

    def get_expired_document(self) -> Document | None:
        return next((doc for doc in self.documents if doc.exp < '1982.11.22'), None)

    def get_invalid_document(self) -> Document | None:
        return next((doc for doc in self.documents if
                     isinstance(doc, DiplomaticAuthorization) and DESTINATION_COUNTRY not in doc.access), None)

    def compare_documents(self) -> str | None:
        comparisons = tuple(set() for _ in range(4))
        attributes = 'id', 'name', 'nation', 'dob'
        attribute_strings = 'ID number', 'name', 'nationality', 'date of birth'

        for doc in self.documents:
            for i, attr in enumerate(attributes):
                comparisons[i].add(getattr(doc, attr))

        for i, comp in enumerate(comparisons):
            comp.discard(None)
            if len(comp) > 1:
                return attribute_strings[i]


class Inspector:
    def __init__(self):
        self.allowed_countries = set()
        self.required_documents = defaultdict(set)
        self.criminal = ''

    def receive_bulletin(self, bulletin: str):
        for action, cities in re.findall(r'(Allow|Deny) citizens of (.+)', bulletin):
            city_set = set(cities.split(', '))
            if action == 'Allow':
                self.allowed_countries.update(city_set)
            else:
                self.allowed_countries.difference_update(city_set)

        for nations, no_longer, requirement in re.findall(
                r'(?:Citizens of )?(.+?) (no longer )?require (.+)', bulletin):
            for nation in nations.split(', '):
                req_docs = self.required_documents[nation]
                if no_longer:
                    req_docs.discard(requirement)
                else:
                    req_docs.add(requirement)

        new_criminal_match = re.search(r'Wanted by the State: (.+)', bulletin)

        if new_criminal_match:
            new_criminal = new_criminal_match.group(1)
            names = new_criminal.split()
            self.criminal = f"{names[-1]}, {' '.join(names[:-1])}"

    def inspect(self, documents: dict[str, str]):
        immigrant = Immigrant()
        doc_classes = (
        Passport, AccessPermit, AsylumGrant, DiplomaticAuthorization, IdCard, VaccinationCertificate, WorkPass)

        for doc_type in doc_classes:
            doc_info = documents.get(doc_type.get_document_underscore_name())
            if doc_info:
                immigrant.add_document(doc_type, doc_info)

        if inconsistency := immigrant.compare_documents():
            return f'Detainment: {inconsistency} mismatch.'

        if any(doc.name == self.criminal for doc in immigrant.documents):
            return 'Detainment: Entrant is a wanted criminal.'

        if expired_doc := immigrant.get_expired_document():
            return f'Entry denied: {expired_doc.document_name} expired.'

        nationality = immigrant.get_nationality()

        required_docs = self.required_documents['Entrants'] | self.required_documents[nationality]
        if nationality != DESTINATION_COUNTRY:
            required_docs |= self.required_documents['Foreigners']

        access_permit = immigrant.find_document(AccessPermit)
        if access_permit and access_permit.purpose == 'WORK':
            required_docs |= self.required_documents['Workers']

        if invalid_doc := immigrant.get_invalid_document():
            return f'Entry denied: invalid {invalid_doc.document_name}.'

        has_required_vaccinations = True
        for doc in required_docs:
            if doc.replace(' ', '_') not in documents:
                if doc == 'access permit' and (
                        'diplomatic_authorization' in documents or 'grant_of_asylum' in documents):
                    continue
                if 'vaccination' in doc:
                    disease = doc[:doc.rfind(' vaccination')]
                    vaccination_cert = immigrant.find_document(VaccinationCertificate)
                    if not vaccination_cert or disease not in vaccination_cert.vaccines:
                        has_required_vaccinations = False
                    continue
                return f'Entry denied: missing required {doc}.'

        if not has_required_vaccinations:
            return 'Entry denied: missing required vaccination.'

        if nationality == DESTINATION_COUNTRY:
            return f'Glory to {DESTINATION_COUNTRY}.'

        if nationality not in self.allowed_countries:
            return 'Entry denied: citizen of banned nation.'

        return 'Cause no trouble.'
