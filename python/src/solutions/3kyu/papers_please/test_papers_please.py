"""https://www.codewars.com/kata/59d582cafbdd0b7ef90000a0"""

from solution_papers_please import *

inspector = Inspector()
bulletin = 'Entrants require passport\nAllow citizens of Arstotzka, Obristan'
inspector.receive_bulletin(bulletin)
josef = {
    'passport': 'ID#: GC07D-FU8AR\nNATION: Arstotzka\nNAME: Costanza, Josef\nDOB: 1933.11.28\nSEX: M\nISS: East Grestin\nEXP: 1983.03.15'}
guyovich = {
    'access_permit': 'NAME: Guyovich, Russian\nNATION: Obristan\nID#: TE8M1-V3N7R\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 159cm\nWEIGHT: 60kg\nEXP: 1983.07.13'}
roman = {
    'passport': 'ID#: WK9XA-LKM0Q\nNATION: United Federation\nNAME: Dolanski, Roman\nDOB: 1933.01.01\nSEX: M\nISS: Shingleton\nEXP: 1983.05.12',
    'grant_of_asylum': 'NAME: Dolanski, Roman\nNATION: United Federation\nID#: Y3MNC-TPWQ2\nDOB: 1933.01.01\nHEIGHT: 176cm\nWEIGHT: 71kg\nEXP: 1983.09.20'}


def test_preliminary_training():
    assert inspector.inspect(josef) == 'Glory to Arstotzka.'
    assert inspector.inspect(guyovich) == 'Entry denied: missing required passport.'
    assert inspector.inspect(roman) == 'Detainment: ID number mismatch.'
