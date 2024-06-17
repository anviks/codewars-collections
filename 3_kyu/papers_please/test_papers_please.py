from papers_please import Inspector


def test():
    inspector = Inspector()

    bulletin = """Entrants require passport
Allow citizens of Arstotzka
Wanted by the State: Mohammed Zhang"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: KDCUJ-N298A\nNATION: Republia\nNAME: Stanislov, Otto\nDOB: 1962.09.25\nSEX: M\nISS: Vedor\nEXP: 1992.07.08'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: H78PR-8M093\nNATION: Antegria\nNAME: Kleiner, Martina\nDOB: 1956.07.28\nSEX: F\nISS: Glorian\nEXP: 1992.08.23'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: R2A0I-T8E6K\nNATION: Arstotzka\nNAME: Lindberg, Natalya\nDOB: 1956.06.29\nSEX: F\nISS: Lesrenadi\nEXP: 1986.01.04'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: NZ0LP-M7FVR\nNATION: Arstotzka\nNAME: Hammerstein, Nadia\nDOB: 1965.05.26\nSEX: F\nISS: Glorian\nEXP: 1989.07.18'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: 5A7U6-SEGDC\nNATION: Impor\nNAME: Jovanovic, Tomas\nDOB: 1951.04.15\nSEX: M\nISS: Shingleton\nEXP: 1990.10.15'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: 82P06-VABS7\nNATION: Impor\nNAME: Karnov, Cameron\nDOB: 1959.08.11\nSEX: F\nISS: Paradizna\nEXP: 1989.03.05'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: LV3SZ-810ST\nNATION: United Federation\nNAME: Sajarvi, Simon\nDOB: 1967.01.27\nSEX: M\nISS: Orvech Vonor\nEXP: 1983.12.16'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: D839H-KUN9Y\nNATION: Kolechia\nNAME: Hammerstein, Gaston\nDOB: 1958.02.08\nSEX: M\nISS: Orvech Vonor\nEXP: 1983.08.23'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: B458G-WY2CS\nNATION: Impor\nNAME: Moldavich, Christina\nDOB: 1968.09.03\nSEX: F\nISS: Great Rapid\nEXP: 1984.08.31'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {}
    assert inspector.inspect(person) == 'Entry denied: missing required passport.'

    person = {
        'passport': 'ID#: SHMK8-9J2N6\nNATION: Impor\nNAME: Diaz, Kristofer\nDOB: 1964.03.22\nSEX: M\nISS: Glorian\nEXP: 1988.06.02'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: YE839-VPS9J\nNATION: Republia\nNAME: Schumer, Patrik\nDOB: 1963.04.15\nSEX: M\nISS: Tsunkeido\nEXP: 1990.12.22'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: RHJ0Q-Z9UHO\nNATION: Kolechia\nNAME: Gregorovich, Ava\nDOB: 1970.01.11\nSEX: F\nISS: Skal\nEXP: 1980.06.29'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: 0MRY1-EG8O3\nNATION: Republia\nNAME: Babayev, Kristina\nDOB: 1968.04.26\nSEX: F\nISS: West Grestin\nEXP: 1983.03.16'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    bulletin = """Allow citizens of Antegria, Impor, Kolechia, Obristan, Republia, United Federation
Wanted by the State: Roman Steinberg"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: E4KTD-49F65\nNATION: Republia\nNAME: Zajak, Eleanor\nDOB: 1958.06.21\nSEX: F\nISS: Vedor\nEXP: 1984.09.06'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 2UL5H-H3GIM\nNATION: Kolechia\nNAME: Hammerstein, Danika\nDOB: 1967.11.03\nSEX: F\nISS: East Grestin\nEXP: 1989.03.23'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: O31VF-LVOQK\nNATION: Kolechia\nNAME: Bullock, Cesar\nDOB: 1969.11.15\nSEX: M\nISS: Lesrenadi\nEXP: 1990.07.17'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: G3I1Y-GQUH4\nNATION: Impor\nNAME: Jokav, Mikhail\nDOB: 1959.09.05\nSEX: M\nISS: Tsunkeido\nEXP: 1984.02.15'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: E86YF-J2HXL\nNATION: Impor\nNAME: Murphy, William\nDOB: 1968.02.29\nSEX: M\nISS: Shingleton\nEXP: 1992.03.24'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: K8STH-VE3QN\nNATION: Kolechia\nNAME: Sorenson, Agnes\nDOB: 1961.09.20\nSEX: F\nISS: West Grestin\nEXP: 1989.04.18'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {}
    assert inspector.inspect(person) == 'Entry denied: missing required passport.'

    person = {
        'passport': 'ID#: XVL7M-OUC9S\nNATION: Republia\nNAME: Pai, Cecelia\nDOB: 1959.02.12\nSEX: F\nISS: Orvech Vonor\nEXP: 1991.05.13'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: A09LJ-RW6AS\nNATION: Antegria\nNAME: Peterson, Vincent\nDOB: 1958.05.14\nSEX: M\nISS: Bostan\nEXP: 1981.06.06'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: P94X5-JG3LF\nNATION: Republia\nNAME: Dahl, Carmen\nDOB: 1957.12.31\nSEX: F\nISS: Mergerous\nEXP: 1992.07.19'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: FQVTS-L7UO9\nNATION: Antegria\nNAME: Maars, Natalya\nDOB: 1963.05.04\nSEX: F\nISS: Mergerous\nEXP: 1984.07.23'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 4DRKA-ATI32\nNATION: United Federation\nNAME: Zitna, Cosmo\nDOB: 1958.06.04\nSEX: M\nISS: Paradizna\nEXP: 1983.10.18'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 78UDK-0PEQ8\nNATION: Antegria\nNAME: Zajak, Nikolas\nDOB: 1967.11.14\nSEX: M\nISS: Vedor\nEXP: 1987.05.09'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Foreigners require access permit
Wanted by the State: Freja Schumer"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: SEU6F-6M1V7\nNATION: Obristan\nNAME: Lindberg, Natalya\nDOB: 1954.07.09\nSEX: F\nISS: Glorian\nEXP: 1981.09.29',
        'grant_of_asylum': 'NAME: Lindberg, Natalya\nNATION: Obristan\nID#: SV8ND-81FUA\nHEIGHT: 185cm\nWEIGHT: 76kg\nEXP: 1991.01.05'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: 0M2OJ-T1MCP\nNATION: Impor\nNAME: Lang, Ava\nDOB: 1956.11.16\nSEX: F\nISS: Yurko City\nEXP: 1984.06.04',
        'access_permit': 'NAME: Lang, Ava\nNATION: Impor\nID#: 0M2OJ-T1MCP\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 180cm\nWEIGHT: 122kg\nEXP: 1983.06.05'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: TARIN-4IO3Q\nNATION: United Federation\nNAME: Muller, Petra\nDOB: 1963.06.13\nSEX: F\nISS: Tsunkeido\nEXP: 1983.07.02',
        'access_permit': 'NAME: Muller, Petra\nNATION: United Federation\nID#: TARIN-4IO3Q\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 173cm\nWEIGHT: 75kg\nEXP: 1993.12.17'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 150PJ-6PJNC\nNATION: United Federation\nNAME: Medici, Olec\nDOB: 1970.03.13\nSEX: M\nISS: Haihan\nEXP: 1980.12.23',
        'grant_of_asylum': 'NAME: Medici, Olec\nNATION: United Federation\nID#: 150PJ-6PJNC\nHEIGHT: 154cm\nWEIGHT: 51kg\nEXP: 1984.11.09'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: D7J3Q-SYIKU\nNATION: Kolechia\nNAME: Smirnov, Katherine\nDOB: 1967.05.17\nSEX: F\nISS: Glorian\nEXP: 1991.01.29',
        'access_permit': 'NAME: Smirnov, Katherine\nNATION: Kolechia\nID#: D7J3Q-SYIKU\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 165cm\nWEIGHT: 90kg\nEXP: 1985.05.14'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: QIOL4-PD0ZA\nNATION: Kolechia\nNAME: Hertzog, Adamik\nDOB: 1966.04.07\nSEX: M\nISS: Yurko City\nEXP: 1992.03.20',
        'access_permit': 'NAME: Hertzog, Adamik\nNATION: Kolechia\nID#: QIOL4-PD0ZA\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 192cm\nWEIGHT: 126kg\nEXP: 1989.04.24'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: VFUI4-CBKFX\nNATION: Impor\nNAME: Frederikson, Michael\nDOB: 1965.05.04\nSEX: M\nISS: Glorian\nEXP: 1985.11.30',
        'access_permit': 'NAME: Frederikson, Michael\nNATION: Impor\nID#: VFUI4-CBKFX\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 191cm\nWEIGHT: 128kg\nEXP: 1993.08.31'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'access_permit': 'NAME: Kierkgaard, Mohammed\nNATION: Republia\nID#: MHK7F-O45AQ\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 199cm\nWEIGHT: 105kg\nEXP: 1985.12.17'}
    assert inspector.inspect(person) == 'Entry denied: missing required passport.'

    person = {
        'passport': 'ID#: U3870-MGJ1B\nNATION: Impor\nNAME: Reichenbach, Vanya\nDOB: 1963.11.05\nSEX: M\nISS: Orvech Vonor\nEXP: 1985.12.02',
        'access_permit': 'NAME: Reichenbach, Vanya\nNATION: Impor\nID#: U3870-MGJ1B\nPURPOSE: WORK\nDURATION: 2 MONTHS\nHEIGHT: 174cm\nWEIGHT: 57kg\nEXP: 1993.08.24'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 5QWFH-OCST9\nNATION: Impor\nNAME: Seczek, Ana\nDOB: 1965.04.26\nSEX: F\nISS: Yurko City\nEXP: 1989.05.12',
        'access_permit': 'NAME: Seczek, Ana\nNATION: Antegria\nID#: 5QWFH-OCST9\nPURPOSE: VISIT\nDURATION: 2 MONTHS\nHEIGHT: 160cm\nWEIGHT: 72kg\nEXP: 1986.06.28'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: OJS4Q-QO4WA\nNATION: Arstotzka\nNAME: Costa, Gloria\nDOB: 1963.09.05\nSEX: F\nISS: Skal\nEXP: 1988.11.28'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: E9RWF-UC0S5\nNATION: Arstotzka\nNAME: Kierkgaard, Kamala\nDOB: 1958.07.27\nSEX: F\nISS: Glorian\nEXP: 1988.06.07'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    bulletin = """Citizens of Arstotzka require ID card
Wanted by the State: Marcel Praskovic"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: GT9CK-E5TNS\nNATION: Obristan\nNAME: Lang, Anastasia\nDOB: 1962.05.30\nSEX: F\nISS: True Glorian\nEXP: 1990.05.11',
        'grant_of_asylum': 'NAME: Lang, Anastasia\nNATION: Obristan\nID#: GT9CK-E5TNS\nHEIGHT: 200cm\nWEIGHT: 64kg\nEXP: 1993.07.12'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 1JHMV-KAZWO\nNATION: Arstotzka\nNAME: Vaughn, Kascha\nDOB: 1954.01.13\nSEX: F\nISS: Shingleton\nEXP: 1993.09.14',
        'ID_card': 'NAME: Vaughn, Kascha\nDOB: 1954.01.13\nHEIGHT: 151cm\nWEIGHT: 84kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: 0BXOW-KPYD3\nNATION: United Federation\nNAME: Vazquez, Aleksander\nDOB: 1961.07.23\nSEX: M\nISS: Outer Grouse\nEXP: 1989.09.07',
        'diplomatic_authorization': 'NAME: Vazquez, Aleksander\nNATION: United Federation\nID#: 0BXOW-KPYD3\nACCESS: Obristan, Antegria, Arstotzka'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: UJFAQ-QX2JU\nNATION: Arstotzka\nNAME: Gregorovich, Paulina\nDOB: 1962.01.19\nSEX: F\nISS: Korista City\nEXP: 1984.04.14',
        'ID_card': 'NAME: Gregorovich, Paulina\nDOB: 1962.01.19\nHEIGHT: 165cm\nWEIGHT: 82kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: 9XZ7A-48SHC\nNATION: Obristan\nNAME: Weiss, Jan\nDOB: 1953.06.26\nSEX: M\nISS: True Glorian\nEXP: 1988.04.26',
        'access_permit': 'NAME: Weiss, Jan\nNATION: Obristan\nID#: 9XZ7A-48SHC\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 166cm\nWEIGHT: 74kg\nEXP: 1987.01.28'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 0IB6W-NE19B\nNATION: United Federation\nNAME: Weisz, Claude\nDOB: 1962.12.09\nSEX: M\nISS: St. Marmero\nEXP: 1993.05.26',
        'grant_of_asylum': 'NAME: Weisz, Claude\nNATION: United Federation\nID#: R07EK-VXUAB\nHEIGHT: 183cm\nWEIGHT: 128kg\nEXP: 1985.01.10'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: 3SG47-AEYQN\nNATION: Kolechia\nNAME: Kovacs, Fyodor\nDOB: 1965.10.09\nSEX: M\nISS: Shingleton\nEXP: 1985.10.12',
        'grant_of_asylum': 'NAME: Kovacs, Fyodor\nNATION: Kolechia\nID#: 3SG47-AEYQN\nHEIGHT: 210cm\nWEIGHT: 104kg\nEXP: 1991.04.06'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: R9T8L-0MY3L\nNATION: United Federation\nNAME: Maars, Calum\nDOB: 1965.11.29\nSEX: M\nISS: East Grestin\nEXP: 1983.05.26',
        'grant_of_asylum': 'NAME: Maars, Calum\nNATION: United Federation\nID#: R9T8L-0MY3L\nHEIGHT: 159cm\nWEIGHT: 45kg\nEXP: 1986.08.11'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 6321B-SGIDJ\nNATION: Impor\nNAME: Bergman, Laura\nDOB: 1950.09.11\nSEX: F\nISS: St. Marmero\nEXP: 1981.09.10',
        'access_permit': 'NAME: Bergman, Laura\nNATION: Impor\nID#: 6321B-SGIDJ\nPURPOSE: VISIT\nDURATION: 1 MONTH\nHEIGHT: 162cm\nWEIGHT: 120kg\nEXP: 1989.05.14'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: XH05I-8RVP9\nNATION: Republia\nNAME: Ortiz, Michaela\nDOB: 1965.01.01\nSEX: F\nISS: Mergerous\nEXP: 1988.05.07',
        'access_permit': 'NAME: Ortiz, Michaela\nNATION: Republia\nID#: XH05I-8RVP9\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 161cm\nWEIGHT: 68kg\nEXP: 1986.11.01'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Allow citizens of Antegria, Impor, Republia, Kolechia, Obristan, United Federation
Wanted by the State: Roberta Klass"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: XWSBI-7DRLU\nNATION: Republia\nNAME: Xavier, Piotr\nDOB: 1959.08.05\nSEX: M\nISS: Skal\nEXP: 1986.09.10'}
    assert inspector.inspect(person) == 'Entry denied: missing required access permit.'

    person = {
        'passport': 'ID#: J267O-7E5AT\nNATION: Obristan\nNAME: Malkova, Edine\nDOB: 1958.11.11\nSEX: F\nISS: Lorndaz\nEXP: 1991.05.31',
        'diplomatic_authorization': 'NAME: Malkova, Edine\nNATION: Obristan\nID#: J267O-7E5AT\nACCESS: Arstotzka, Kolechia, Antegria, United Federation, Impor'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: P8SZN-SNJLT\nNATION: Republia\nNAME: Jokav, Mohammed\nDOB: 1955.06.20\nSEX: M\nISS: Korista City\nEXP: 1982.08.14',
        'access_permit': 'NAME: Jokav, Mohammed\nNATION: Republia\nID#: P8SZN-SNJLT\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 208cm\nWEIGHT: 46kg\nEXP: 1983.08.03'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: 0YCRA-SGDBI\nNATION: Arstotzka\nNAME: Muller, Zachary\nDOB: 1960.05.23\nSEX: M\nISS: Outer Grouse\nEXP: 1983.08.28',
        'ID_card': 'NAME: Muller, Zachary\nDOB: 1960.05.23\nHEIGHT: 195cm\nWEIGHT: 44kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: MYSE1-BU1NF\nNATION: United Federation\nNAME: David, Werner\nDOB: 1953.11.13\nSEX: M\nISS: Lesrenadi\nEXP: 1983.09.25',
        'access_permit': 'NAME: David, Werner\nNATION: United Federation\nID#: Z1JE8-ZOY38\nPURPOSE: WORK\nDURATION: 3 MONTHS\nHEIGHT: 154cm\nWEIGHT: 41kg\nEXP: 1987.06.26'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: P0I8J-1U0CT\nNATION: Antegria\nNAME: Leonov, Lisa\nDOB: 1955.05.03\nSEX: F\nISS: Orvech Vonor\nEXP: 1988.08.02',
        'grant_of_asylum': 'NAME: Leonov, Lisa\nNATION: Antegria\nID#: P0I8J-1U0CT\nHEIGHT: 204cm\nWEIGHT: 130kg\nEXP: 1990.05.24'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: BAFYW-QFCTG\nNATION: Republia\nNAME: Crechiolo, Sarah\nDOB: 1963.09.14\nSEX: F\nISS: True Glorian\nEXP: 1982.12.28',
        'diplomatic_authorization': 'NAME: Crechiolo, Sarah\nNATION: Republia\nID#: BAFYW-QFCTG\nACCESS: Arstotzka, United Federation, Obristan, Impor'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: B8RVK-HOTJ7\nNATION: Kolechia\nNAME: Hammerstein, Yuri\nDOB: 1959.01.31\nSEX: M\nISS: Skal\nEXP: 1984.04.29',
        'access_permit': 'NAME: Hammerstein, Yuri\nNATION: Kolechia\nID#: B8RVK-HOTJ7\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 195cm\nWEIGHT: 93kg\nEXP: 1987.04.10'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: KNW8B-CIUHR\nNATION: Arstotzka\nNAME: Dimanishki, Jennifer\nDOB: 1952.08.01\nSEX: F\nISS: Bostan\nEXP: 1985.03.15',
        'ID_card': 'NAME: Dimanishki, Jennifer\nDOB: 1952.08.01\nHEIGHT: 190cm\nWEIGHT: 85kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: FTQ92-CE2UY\nNATION: Kolechia\nNAME: Novak, Maciej\nDOB: 1964.03.11\nSEX: M\nISS: Bostan\nEXP: 1983.12.12',
        'access_permit': 'NAME: Novak, Maciej\nNATION: Kolechia\nID#: FTQ92-CE2UY\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 159cm\nWEIGHT: 94kg\nEXP: 1990.02.14'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 09VFQ-UZ1XP\nNATION: Obristan\nNAME: Kreczmanski, Kamala\nDOB: 1966.01.22\nSEX: F\nISS: Bostan\nEXP: 1983.01.08',
        'access_permit': 'NAME: Kreczmanski, Kamala\nNATION: Obristan\nID#: 09VFQ-UZ1XP\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 168cm\nWEIGHT: 117kg\nEXP: 1985.02.22'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 21GIN-2Y3TR\nNATION: Impor\nNAME: Henriksson, Liliana\nDOB: 1963.03.27\nSEX: F\nISS: Great Rapid\nEXP: 1980.09.03',
        'access_permit': 'NAME: Henriksson, Liliana\nNATION: United Federation\nID#: 21GIN-2Y3TR\nPURPOSE: WORK\nDURATION: 2 MONTHS\nHEIGHT: 198cm\nWEIGHT: 66kg\nEXP: 1987.04.01'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    bulletin = """Wanted by the State: Andrew Pejic"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: EB5P3-FO29Y\nNATION: Arstotzka\nNAME: Xavier, Galina\nDOB: 1950.01.06\nSEX: F\nISS: Glorian\nEXP: 1984.07.07',
        'ID_card': 'NAME: Xavier, Galina\nDOB: 1993.02.21\nHEIGHT: 186cm\nWEIGHT: 127kg'}
    assert inspector.inspect(person) == 'Detainment: date of birth mismatch.'

    person = {
        'passport': 'ID#: OF3LW-JG9XP\nNATION: Arstotzka\nNAME: Moldavich, Dominik\nDOB: 1953.04.25\nSEX: M\nISS: Outer Grouse\nEXP: 1992.06.06',
        'ID_card': 'NAME: Moldavich, Dominik\nDOB: 1953.04.25\nHEIGHT: 192cm\nWEIGHT: 128kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: EC572-Q5ERC\nNATION: Impor\nNAME: Knapik, Erik\nDOB: 1963.05.17\nSEX: M\nISS: Great Rapid\nEXP: 1980.03.17',
        'access_permit': 'NAME: Knapik, Erik\nNATION: Impor\nID#: EC572-Q5ERC\nPURPOSE: VISIT\nDURATION: 2 MONTHS\nHEIGHT: 183cm\nWEIGHT: 95kg\nEXP: 1990.11.24'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {'ID_card': 'NAME: Nilsson, Agnes\nDOB: 1988.04.21\nHEIGHT: 191cm\nWEIGHT: 50kg'}
    assert inspector.inspect(person) == 'Entry denied: missing required passport.'

    person = {
        'passport': 'ID#: Y04V6-QO71U\nNATION: Antegria\nNAME: David, Johann\nDOB: 1970.07.14\nSEX: M\nISS: True Glorian\nEXP: 1990.05.06',
        'access_permit': 'NAME: David, Johann\nNATION: Antegria\nID#: Y04V6-QO71U\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 202cm\nWEIGHT: 121kg\nEXP: 1986.11.21'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 7FTUB-A7R92\nNATION: Impor\nNAME: Zajak, Guy\nDOB: 1950.01.20\nSEX: M\nISS: Skal\nEXP: 1983.02.22',
        'access_permit': 'NAME: Zajak, Guy\nNATION: Impor\nID#: 7FTUB-A7R92\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 159cm\nWEIGHT: 80kg\nEXP: 1981.08.04'}
    assert inspector.inspect(person) == 'Entry denied: access permit expired.'

    person = {
        'passport': 'ID#: DR5GJ-4PAFW\nNATION: Arstotzka\nNAME: Pejic, Andrew\nDOB: 1964.04.11\nSEX: F\nISS: Enkyo\nEXP: 1986.06.26',
        'ID_card': 'NAME: Pejic, Andrew\nDOB: 1964.04.11\nHEIGHT: 161cm\nWEIGHT: 85kg'}
    assert inspector.inspect(person) == 'Detainment: Entrant is a wanted criminal.'

    person = {
        'passport': 'ID#: IKN41-1QYWS\nNATION: United Federation\nNAME: Anderson, Kamala\nDOB: 1960.08.06\nSEX: F\nISS: Lorndaz\nEXP: 1991.12.25',
        'access_permit': 'NAME: Anderson, Kamala\nNATION: United Federation\nID#: IKN41-1QYWS\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 154cm\nWEIGHT: 123kg\nEXP: 1987.12.01'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: M6O28-G08BF\nNATION: Impor\nNAME: Stolichnaya, Cheyenne\nDOB: 1964.09.24\nSEX: F\nISS: Bostan\nEXP: 1981.07.26',
        'access_permit': 'NAME: Stolichnaya, Cheyenne\nNATION: Impor\nID#: M6O28-G08BF\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 190cm\nWEIGHT: 130kg\nEXP: 1988.11.30'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: HB3UD-796H2\nNATION: Obristan\nNAME: Romanoff, Abdullah\nDOB: 1966.08.15\nSEX: M\nISS: Korista City\nEXP: 1989.01.05',
        'access_permit': 'NAME: Romanoff, Abdullah\nNATION: Obristan\nID#: HB3UD-796H2\nPURPOSE: VISIT\nDURATION: 1 MONTH\nHEIGHT: 153cm\nWEIGHT: 81kg\nEXP: 1988.12.26'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: SV258-629NI\nNATION: Republia\nNAME: Nilsson, Rozsa\nDOB: 1969.11.06\nSEX: F\nISS: Lorndaz\nEXP: 1993.05.21',
        'access_permit': 'NAME: Nilsson, Rozsa\nNATION: Republia\nID#: SV258-629NI\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 185cm\nWEIGHT: 67kg\nEXP: 1988.09.17'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: GKBHU-OEXCU\nNATION: Impor\nNAME: Frank, Natalya\nDOB: 1970.11.21\nSEX: F\nISS: West Grestin\nEXP: 1992.05.17',
        'access_permit': 'NAME: Frank, Natalya\nNATION: Impor\nID#: GKBHU-OEXCU\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 154cm\nWEIGHT: 67kg\nEXP: 1991.07.20'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: MA9QK-W48QD\nNATION: Antegria\nNAME: Evans, Rafal\nDOB: 1952.08.22\nSEX: M\nISS: Paradizna\nEXP: 1991.01.15',
        'access_permit': 'NAME: Evans, Rafal\nNATION: Antegria\nID#: MA9QK-W48QD\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 200cm\nWEIGHT: 58kg\nEXP: 1987.06.18'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Deny citizens of Obristan, Impor, Republia
Foreigners require yellow fever vaccination
Wanted by the State: Fyodor Medici"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: PHMXZ-U0T2Y\nNATION: United Federation\nNAME: Krug, Nikolai\nDOB: 1954.01.09\nSEX: M\nISS: Tsunkeido\nEXP: 1991.06.28',
        'certificate_of_vaccination': 'NAME: Krug, Nikolai\nID#: PHMXZ-U0T2Y\nVACCINES: hepatitis B, yellow fever, tetanus, tuberculosis',
        'access_permit': 'NAME: Krug, Nikolai\nNATION: United Federation\nID#: PHMXZ-U0T2Y\nPURPOSE: WORK\nDURATION: 1 YEAR\nHEIGHT: 199cm\nWEIGHT: 99kg\nEXP: 1989.12.10'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: GWKZQ-O4G60\nNATION: Antegria\nNAME: Savelle, Lena\nDOB: 1959.06.09\nSEX: F\nISS: Lesrenadi\nEXP: 1989.03.22',
        'certificate_of_vaccination': 'NAME: Savelle, Lena\nID#: GWKZQ-O4G60\nVACCINES: cholera, rubella, hepatitis B',
        'diplomatic_authorization': 'NAME: Savelle, Lena\nNATION: Antegria\nID#: GWKZQ-O4G60\nACCESS: Impor, Kolechia'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    person = {
        'passport': 'ID#: ZJB1L-78Q16\nNATION: Obristan\nNAME: Diaz, Anita\nDOB: 1959.08.14\nSEX: F\nISS: Yurko City\nEXP: 1986.12.14',
        'certificate_of_vaccination': 'NAME: Diaz, Anita\nID#: ZJB1L-78Q16\nVACCINES: measles, typhus, yellow fever, cholera',
        'access_permit': 'NAME: Diaz, Anita\nNATION: Obristan\nID#: ZJB1L-78Q16\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 145cm\nWEIGHT: 70kg\nEXP: 1986.04.15'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: 5IJ6G-G9V5K\nNATION: Impor\nNAME: Xavier, Marina\nDOB: 1950.06.08\nSEX: F\nISS: Lesrenadi\nEXP: 1991.04.08',
        'certificate_of_vaccination': 'NAME: Xavier, Marina\nID#: 5IJ6G-G9V5K\nVACCINES: cowpox, yellow fever, HPV, polio',
        'access_permit': 'NAME: Xavier, Marina\nNATION: Impor\nID#: 5IJ6G-G9V5K\nPURPOSE: WORK\nDURATION: 3 MONTHS\nHEIGHT: 168cm\nWEIGHT: 94kg\nEXP: 1983.06.13'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: ABH93-5NJD2\nNATION: Kolechia\nNAME: Kostovetsky, Gabrielle\nDOB: 1953.07.27\nSEX: F\nISS: Paradizna\nEXP: 1988.01.16',
        'certificate_of_vaccination': 'NAME: Kostovetsky, Gabrielle\nID#: ABH93-5NJD2\nVACCINES: polio, tuberculosis, cholera',
        'access_permit': 'NAME: Kostovetsky, Gabrielle\nNATION: United Federation\nID#: ABH93-5NJD2\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 147cm\nWEIGHT: 56kg\nEXP: 1988.08.19'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: VG1KE-NM96D\nNATION: Arstotzka\nNAME: Medici, Fyodor\nDOB: 1964.05.15\nSEX: F\nISS: Bostan\nEXP: 1987.07.01',
        'ID_card': 'NAME: Medici, Fyodor\nDOB: 1964.05.15\nHEIGHT: 167cm\nWEIGHT: 103kg'}
    assert inspector.inspect(person) == 'Detainment: Entrant is a wanted criminal.'

    person = {
        'passport': 'ID#: E1GHT-1JEFA\nNATION: Antegria\nNAME: Moldavich, Hector\nDOB: 1951.03.15\nSEX: M\nISS: St. Marmero\nEXP: 1990.08.21',
        'certificate_of_vaccination': 'NAME: Moldavich, Hector\nID#: E1GHT-1JEFA\nVACCINES: cholera, typhus, tetanus',
        'access_permit': 'NAME: Moldavich, Hector\nNATION: Antegria\nID#: 918HJ-ZG7OC\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 209cm\nWEIGHT: 115kg\nEXP: 1992.05.24'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: 5LMJP-PG0Q6\nNATION: Kolechia\nNAME: Schumer, Sarah\nDOB: 1962.03.30\nSEX: F\nISS: Glorian\nEXP: 1988.12.31',
        'certificate_of_vaccination': 'NAME: Schumer, Sarah\nID#: 5LMJP-PG0Q6\nVACCINES: polio, tetanus, yellow fever, cholera',
        'access_permit': 'NAME: Schumer, Sarah\nNATION: Kolechia\nID#: 5LMJP-PG0Q6\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 193cm\nWEIGHT: 83kg\nEXP: 1985.04.23'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: HF9WG-QER3D\nNATION: Antegria\nNAME: Knapik, Khalid\nDOB: 1968.08.12\nSEX: M\nISS: St. Marmero\nEXP: 1983.08.11',
        'access_permit': 'NAME: Knapik, Khalid\nNATION: Antegria\nID#: HF9WG-QER3D\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 172cm\nWEIGHT: 118kg\nEXP: 1980.09.30'}
    assert inspector.inspect(person) == 'Entry denied: access permit expired.'

    person = {
        'passport': 'ID#: 87TAY-M0HYI\nNATION: United Federation\nNAME: Guillot, Rikardo\nDOB: 1964.07.14\nSEX: M\nISS: Lorndaz\nEXP: 1989.11.23',
        'certificate_of_vaccination': 'NAME: Guillot, Rikardo\nID#: 87TAY-M0HYI\nVACCINES: measles, tuberculosis, rubella',
        'access_permit': 'NAME: Guillot, Rikardo\nNATION: United Federation\nID#: KG079-1JROD\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 169cm\nWEIGHT: 53kg\nEXP: 1992.10.12'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: M54GO-8ND1G\nNATION: Republia\nNAME: Savelle, Gustav\nDOB: 1958.07.03\nSEX: M\nISS: Outer Grouse\nEXP: 1990.03.26',
        'certificate_of_vaccination': 'NAME: Savelle, Gustav\nID#: M54GO-8ND1G\nVACCINES: cholera, tuberculosis, HPV',
        'grant_of_asylum': 'NAME: Savelle, Gustav\nNATION: Republia\nID#: M54GO-8ND1G\nHEIGHT: 187cm\nWEIGHT: 68kg\nEXP: 1980.12.24'}
    assert inspector.inspect(person) == 'Entry denied: grant of asylum expired.'

    bulletin = """Allow citizens of Republia
    Deny citizens of Antegria
    Entrants require tetanus vaccination
    Wanted by the State: Victoria Schroder"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: 71W6T-Z7CWH\nNATION: United Federation\nNAME: Muller, Tatiana\nDOB: 1960.04.07\nSEX: F\nISS: Bostan\nEXP: 1987.03.25',
        'certificate_of_vaccination': 'NAME: Muller, Tatiana\nID#: 71W6T-Z7CWH\nVACCINES: tetanus, cholera, yellow fever, polio',
        'grant_of_asylum': 'NAME: Muller, Tatiana\nNATION: United Federation\nID#: 71W6T-Z7CWH\nHEIGHT: 187cm\nWEIGHT: 82kg\nEXP: 1986.01.15'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: KEPQN-5VIWL\nNATION: Republia\nNAME: Hansson, Felicia\nDOB: 1957.09.07\nSEX: F\nISS: Glorian\nEXP: 1989.09.30',
        'certificate_of_vaccination': 'NAME: Hansson, Felicia\nID#: KEPQN-5VIWL\nVACCINES: tetanus, tuberculosis, yellow fever, measles',
        'access_permit': 'NAME: Hansson, Felicia\nNATION: Republia\nID#: KEPQN-5VIWL\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 167cm\nWEIGHT: 84kg\nEXP: 1991.05.20'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 8F40L-U3VHN\nNATION: Kolechia\nNAME: Tsarnaeva, Erika\nDOB: 1964.09.16\nSEX: F\nISS: True Glorian\nEXP: 1993.02.27',
        'certificate_of_vaccination': 'NAME: Tsarnaeva, Erika\nID#: 8F40L-U3VHN\nVACCINES: yellow fever, hepatitis B, rubella, tetanus',
        'access_permit': 'NAME: Tsarnaeva, Erika\nNATION: Kolechia\nID#: 8F40L-U3VHN\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 197cm\nWEIGHT: 103kg\nEXP: 1991.06.25'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: ZK175-JSO2U\nNATION: Impor\nNAME: Zitna, Damian\nDOB: 1954.05.10\nSEX: M\nISS: Bostan\nEXP: 1991.02.16',
        'certificate_of_vaccination': 'NAME: Zitna, Damian\nID#: ZK175-JSO2U\nVACCINES: rubella, tetanus, yellow fever, HPV',
        'access_permit': 'NAME: Zitna, Damian\nNATION: Impor\nID#: ZK175-JSO2U\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 200cm\nWEIGHT: 63kg\nEXP: 1989.03.16'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: 3OAE2-61ADN\nNATION: Obristan\nNAME: Odom, Samantha\nDOB: 1953.02.14\nSEX: F\nISS: St. Marmero\nEXP: 1991.04.26',
        'certificate_of_vaccination': 'NAME: Odom, Samantha\nID#: 3OAE2-61ADN\nVACCINES: tuberculosis, hepatitis B',
        'grant_of_asylum': 'NAME: Odom, Samantha\nNATION: United Federation\nID#: 3OAE2-61ADN\nHEIGHT: 208cm\nWEIGHT: 42kg\nEXP: 1989.05.29'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: ITS46-IGBJH\nNATION: United Federation\nNAME: Graham, Igor\nDOB: 1959.11.24\nSEX: M\nISS: Tsunkeido\nEXP: 1992.02.23',
        'certificate_of_vaccination': 'NAME: Graham, Igor\nID#: ITS46-IGBJH\nVACCINES: HPV, yellow fever, rubella, tetanus',
        'access_permit': 'NAME: Graham, Igor\nNATION: United Federation\nID#: ITS46-IGBJH\nPURPOSE: VISIT\nDURATION: 2 MONTHS\nHEIGHT: 189cm\nWEIGHT: 66kg\nEXP: 1984.11.29'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: HLOI6-7EGI3\nNATION: Obristan\nNAME: Vincenza, Marco\nDOB: 1963.05.31\nSEX: M\nISS: Shingleton\nEXP: 1990.03.31',
        'certificate_of_vaccination': 'NAME: Vincenza, Marco\nID#: HLOI6-7EGI3\nVACCINES: tuberculosis, tetanus, yellow fever, polio',
        'diplomatic_authorization': 'NAME: Vincenza, Marco\nNATION: Obristan\nID#: HLOI6-7EGI3\nACCESS: Republia, Kolechia, United Federation, Arstotzka'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: 6C8QI-8QXKL\nNATION: Obristan\nNAME: Kirsch, Erik\nDOB: 1955.01.30\nSEX: M\nISS: West Grestin\nEXP: 1986.11.07',
        'certificate_of_vaccination': 'NAME: Kirsch, Erik\nID#: 6C8QI-8QXKL\nVACCINES: tetanus, polio, HPV, yellow fever',
        'access_permit': 'NAME: Kirsch, Erik\nNATION: Obristan\nID#: 6C8QI-8QXKL\nPURPOSE: WORK\nDURATION: 6 MONTHS\nHEIGHT: 170cm\nWEIGHT: 47kg\nEXP: 1984.02.25'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {'certificate_of_vaccination': 'NAME: Vyas, Nicolai\nID#: WM4GE-AMP35\nVACCINES: tuberculosis, cowpox',
              'diplomatic_authorization': 'NAME: Vyas, Nicolai\nNATION: Kolechia\nID#: WM4GE-AMP35\nACCESS: Republia, Antegria, Impor, Obristan'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    person = {
        'passport': 'ID#: N4ZIC-RP8A6\nNATION: United Federation\nNAME: Kravitz, Ekaterina\nDOB: 1959.05.25\nSEX: F\nISS: Skal\nEXP: 1985.04.05',
        'certificate_of_vaccination': 'NAME: Kravitz, Ekaterina\nID#: N4ZIC-RP8A6\nVACCINES: tetanus, yellow fever, typhus, hepatitis B',
        'access_permit': 'NAME: Kravitz, Ekaterina\nNATION: United Federation\nID#: N4ZIC-RP8A6\nPURPOSE: VISIT\nDURATION: 1 MONTH\nHEIGHT: 186cm\nWEIGHT: 58kg\nEXP: 1984.10.18'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: U19T2-9XM6R\nNATION: Obristan\nNAME: Ibrahimovic, Alek\nDOB: 1960.04.20\nSEX: M\nISS: Lorndaz\nEXP: 1988.02.28',
        'certificate_of_vaccination': 'NAME: Ibrahimovic, Alek\nID#: U19T2-9XM6R\nVACCINES: HPV, tetanus, yellow fever, cowpox',
        'access_permit': 'NAME: Ibrahimovic, Alek\nNATION: Obristan\nID#: U19T2-9XM6R\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 199cm\nWEIGHT: 123kg\nEXP: 1986.10.15'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: ROX1E-8ZD7C\nNATION: Impor\nNAME: Muller, Eduardo\nDOB: 1956.06.14\nSEX: M\nISS: Great Rapid\nEXP: 1985.10.24',
        'certificate_of_vaccination': 'NAME: Muller, Eduardo\nID#: ROX1E-8ZD7C\nVACCINES: tetanus, cholera, yellow fever, cowpox',
        'diplomatic_authorization': 'NAME: Muller, Eduardo\nNATION: Impor\nID#: ROX1E-8ZD7C\nACCESS: United Federation, Arstotzka, Republia, Obristan, Kolechia'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: 5RXDW-N5SV9\nNATION: Obristan\nNAME: Muller, Romeo\nDOB: 1968.07.03\nSEX: M\nISS: Great Rapid\nEXP: 1987.02.15',
        'certificate_of_vaccination': 'NAME: Muller, Romeo\nID#: 5RXDW-N5SV9\nVACCINES: yellow fever, tetanus, cowpox, hepatitis B',
        'grant_of_asylum': 'NAME: Muller, Romeo\nNATION: Obristan\nID#: 5RXDW-N5SV9\nHEIGHT: 152cm\nWEIGHT: 94kg\nEXP: 1992.04.30'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    bulletin = """Allow citizens of Impor
Deny citizens of Kolechia, Republia, United Federation
Citizens of Obristan require polio vaccination
Wanted by the State: Lukas Dahl"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: Y10SZ-LFM0K\nNATION: Impor\nNAME: Hammerstein, Mikkel\nDOB: 1957.02.06\nSEX: M\nISS: Vedor\nEXP: 1987.06.10',
        'certificate_of_vaccination': 'NAME: Hammerstein, Mikkel\nID#: Y10SZ-LFM0K\nVACCINES: yellow fever, tuberculosis, cholera, tetanus',
        'access_permit': 'NAME: Hammerstein, Mikkel\nNATION: Impor\nID#: Y10SZ-LFM0K\nPURPOSE: WORK\nDURATION: 2 MONTHS\nHEIGHT: 203cm\nWEIGHT: 83kg\nEXP: 1990.11.11'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 56C0F-9BLYO\nNATION: United Federation\nNAME: Babayev, Nikolas\nDOB: 1963.11.06\nSEX: M\nISS: Vedor\nEXP: 1988.08.08',
        'certificate_of_vaccination': 'NAME: Babayev, Nikolas\nID#: 56C0F-9BLYO\nVACCINES: measles, tetanus, cowpox, yellow fever',
        'access_permit': 'NAME: Babayev, Nikolas\nNATION: United Federation\nID#: 56C0F-9BLYO\nPURPOSE: VISIT\nDURATION: 1 MONTH\nHEIGHT: 166cm\nWEIGHT: 121kg\nEXP: 1983.07.23'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: UACV1-KPUW5\nNATION: Obristan\nNAME: Diaz, Petr\nDOB: 1953.01.20\nSEX: M\nISS: Tsunkeido\nEXP: 1985.12.02',
        'certificate_of_vaccination': 'NAME: Diaz, Petr\nID#: UACV1-KPUW5\nVACCINES: HPV',
        'access_permit': 'NAME: Diaz, Petr\nNATION: Antegria\nID#: UACV1-KPUW5\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 184cm\nWEIGHT: 126kg\nEXP: 1983.12.12'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: 8LN4S-CORSQ\nNATION: Obristan\nNAME: Zeitsoff, Cosmo\nDOB: 1954.04.11\nSEX: M\nISS: West Grestin\nEXP: 1986.03.21',
        'certificate_of_vaccination': 'NAME: Zeitsoff, Cosmo\nID#: 8LN4S-CORSQ\nVACCINES: polio, yellow fever, tetanus, HPV',
        'access_permit': 'NAME: Zeitsoff, Cosmo\nNATION: Obristan\nID#: 8LN4S-CORSQ\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 182cm\nWEIGHT: 42kg\nEXP: 1983.12.18'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: BKYOP-FMG3R\nNATION: Republia\nNAME: Wolfe, Hugo\nDOB: 1963.01.26\nSEX: M\nISS: West Grestin\nEXP: 1989.11.09',
        'certificate_of_vaccination': 'NAME: Wolfe, Hugo\nID#: BKYOP-FMG3R\nVACCINES: hepatitis B, yellow fever, tetanus, HPV',
        'grant_of_asylum': 'NAME: Wolfe, Hugo\nNATION: Republia\nID#: BKYOP-FMG3R\nHEIGHT: 177cm\nWEIGHT: 114kg\nEXP: 1989.07.07'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: QRT53-97BDI\nNATION: Obristan\nNAME: Hassad, Gunther\nDOB: 1963.02.08\nSEX: M\nISS: Lorndaz\nEXP: 1991.06.17',
        'certificate_of_vaccination': 'NAME: Hassad, Gunther\nID#: QRT53-97BDI\nVACCINES: typhus',
        'diplomatic_authorization': 'NAME: Hassad, Gunther\nNATION: Obristan\nID#: QRT53-97BDI\nACCESS: Antegria'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    person = {
        'passport': 'ID#: 6UBS8-0BP24\nNATION: Republia\nNAME: Vyas, Heidi\nDOB: 1967.06.20\nSEX: F\nISS: Lorndaz\nEXP: 1986.05.31',
        'certificate_of_vaccination': 'NAME: Vyas, Heidi\nID#: 6UBS8-0BP24\nVACCINES: yellow fever, cowpox, tetanus, typhus',
        'access_permit': 'NAME: Vyas, Heidi\nNATION: Republia\nID#: 6UBS8-0BP24\nPURPOSE: WORK\nDURATION: 2 MONTHS\nHEIGHT: 163cm\nWEIGHT: 121kg\nEXP: 1991.12.17'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: CYFG1-D7JKY\nNATION: Arstotzka\nNAME: Thunstrom, Joachim\nDOB: 1954.12.13\nSEX: M\nISS: Tsunkeido\nEXP: 1987.12.11',
        'certificate_of_vaccination': 'NAME: Thunstrom, Joachim\nID#: CYFG1-D7JKY\nVACCINES: HPV, measles, cholera, tetanus',
        'ID_card': 'NAME: Thunstrom, Joachim\nDOB: 1954.12.13\nHEIGHT: 177cm\nWEIGHT: 126kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: TNJ8K-Q1OIB\nNATION: Obristan\nNAME: Schulz, Josefina\nDOB: 1950.01.18\nSEX: F\nISS: Bostan\nEXP: 1984.04.20',
        'certificate_of_vaccination': 'NAME: Schulz, Josefina\nID#: TNJ8K-Q1OIB\nVACCINES: yellow fever, HPV, tetanus, polio',
        'grant_of_asylum': 'NAME: Schulz, Josefina\nNATION: Obristan\nID#: TNJ8K-Q1OIB\nHEIGHT: 207cm\nWEIGHT: 46kg\nEXP: 1993.04.25'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: B19PR-0XYKU\nNATION: United Federation\nNAME: Karlsson, Zera\nDOB: 1961.12.24\nSEX: F\nISS: Shingleton\nEXP: 1987.04.23',
        'certificate_of_vaccination': 'NAME: Karlsson, Zera\nID#: B19PR-0XYKU\nVACCINES: rubella, measles'}
    assert inspector.inspect(person) == 'Entry denied: missing required access permit.'

    person = {
        'passport': 'ID#: N4UQK-51FEV\nNATION: Obristan\nNAME: Gregorovich, Ingrid\nDOB: 1958.09.30\nSEX: F\nISS: Glorian\nEXP: 1993.09.20',
        'certificate_of_vaccination': 'NAME: Gregorovich, Ingrid\nID#: N4UQK-51FEV\nVACCINES: typhus, tetanus, yellow fever, polio',
        'access_permit': 'NAME: Gregorovich, Ingrid\nNATION: Obristan\nID#: N4UQK-51FEV\nPURPOSE: VISIT\nDURATION: 3 MONTHS\nHEIGHT: 185cm\nWEIGHT: 93kg\nEXP: 1993.11.07'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: PYV7U-J2YOX\nNATION: United Federation\nNAME: Hansson, Jorge\nDOB: 1953.01.22\nSEX: M\nISS: Mergerous\nEXP: 1991.10.19',
        'certificate_of_vaccination': 'NAME: Hansson, Jorge\nID#: PYV7U-J2YOX\nVACCINES: HPV, hepatitis B',
        'access_permit': 'NAME: Hansson, Jorge\nNATION: United Federation\nID#: WQE5Y-CKJ5R\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 210cm\nWEIGHT: 102kg\nEXP: 1986.03.04'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: QVCAN-8H1FR\nNATION: United Federation\nNAME: Rosenfeld, Vanessa\nDOB: 1962.07.30\nSEX: F\nISS: Yurko City\nEXP: 1980.12.12',
        'certificate_of_vaccination': 'NAME: Rosenfeld, Vanessa\nID#: QVCAN-8H1FR\nVACCINES: cholera, rubella',
        'access_permit': 'NAME: Rosenfeld, Vanessa\nNATION: United Federation\nID#: UHRTV-RJ8DM\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 209cm\nWEIGHT: 90kg\nEXP: 1992.01.23'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: FEHND-M7EQZ\nNATION: United Federation\nNAME: Knapik, Elena\nDOB: 1951.08.07\nSEX: F\nISS: True Glorian\nEXP: 1989.06.09',
        'certificate_of_vaccination': 'NAME: Knapik, Elena\nID#: FEHND-M7EQZ\nVACCINES: yellow fever, tetanus, measles, cholera',
        'access_permit': 'NAME: Knapik, Elena\nNATION: United Federation\nID#: FEHND-M7EQZ\nPURPOSE: VISIT\nDURATION: 3 MONTHS\nHEIGHT: 174cm\nWEIGHT: 67kg\nEXP: 1984.02.07'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    bulletin = """Deny citizens of Impor
Workers require work pass
Wanted by the State: Rachel Romanoff"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: IMRZJ-YKX7W\nNATION: Republia\nNAME: Sorenson, Maria\nDOB: 1963.04.08\nSEX: F\nISS: Great Rapid\nEXP: 1993.08.24',
        'certificate_of_vaccination': 'NAME: Sorenson, Maria\nID#: IMRZJ-YKX7W\nVACCINES: polio, rubella, tetanus, yellow fever',
        'access_permit': 'NAME: Sorenson, Maria\nNATION: Republia\nID#: IMRZJ-YKX7W\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 187cm\nWEIGHT: 130kg\nEXP: 1985.10.13'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: ROBTD-FTGI3\nNATION: Republia\nNAME: Ramos, Johann\nDOB: 1959.12.13\nSEX: M\nISS: Vedor\nEXP: 1990.05.13',
        'certificate_of_vaccination': 'NAME: Ramos, Johann\nID#: ROBTD-FTGI3\nVACCINES: polio, cowpox, tetanus, yellow fever',
        'grant_of_asylum': 'NAME: Ramos, Johann\nNATION: Republia\nID#: ROBTD-FTGI3\nHEIGHT: 207cm\nWEIGHT: 111kg\nEXP: 1989.01.10'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: S4G6H-TN257\nNATION: United Federation\nNAME: Vaughn, Gabrielle\nDOB: 1965.08.03\nSEX: F\nISS: Outer Grouse\nEXP: 1991.09.01',
        'certificate_of_vaccination': 'NAME: Vaughn, Gabrielle\nID#: S4G6H-TN257\nVACCINES: rubella, polio',
        'access_permit': 'NAME: Vaughn, Gabrielle\nNATION: United Federation\nID#: P893Y-W5AVB\nPURPOSE: WORK\nDURATION: 1 YEAR\nHEIGHT: 207cm\nWEIGHT: 80kg\nEXP: 1983.06.27',
        'work_pass': 'NAME: Tjell, Ivanka\nFIELD: Research\nEXP: 1982.07.18'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: 5WR76-Y09OW\nNATION: Impor\nNAME: Czekowicz, Alberta\nDOB: 1962.11.14\nSEX: F\nISS: Paradizna\nEXP: 1989.04.02',
        'certificate_of_vaccination': 'NAME: Czekowicz, Alberta\nID#: 5WR76-Y09OW\nVACCINES: typhus, yellow fever, tetanus, tuberculosis',
        'access_permit': 'NAME: Czekowicz, Alberta\nNATION: Impor\nID#: 5WR76-Y09OW\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 190cm\nWEIGHT: 108kg\nEXP: 1993.10.21'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: EBKZJ-05OEG\nNATION: Republia\nNAME: Thunstrom, Ada\nDOB: 1957.10.07\nSEX: F\nISS: East Grestin\nEXP: 1992.09.02',
        'certificate_of_vaccination': 'NAME: Thunstrom, Ada\nID#: EBKZJ-05OEG\nVACCINES: polio, yellow fever, tetanus, cholera',
        'access_permit': 'NAME: Thunstrom, Ada\nNATION: Republia\nID#: EBKZJ-05OEG\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 205cm\nWEIGHT: 117kg\nEXP: 1989.09.19'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: DGKZ6-L1HJY\nNATION: Kolechia\nNAME: Romanoff, Rachel\nDOB: 1955.03.06\nSEX: F\nISS: Shingleton\nEXP: 1983.03.30',
        'diplomatic_authorization': 'NAME: Romanoff, Rachel\nNATION: Kolechia\nID#: DGKZ6-L1HJY\nACCESS: Impor, Antegria, United Federation'}
    assert inspector.inspect(person) == 'Detainment: Entrant is a wanted criminal.'

    person = {
        'passport': 'ID#: TZRFY-N0BXO\nNATION: Obristan\nNAME: Savelle, Giovanni\nDOB: 1961.11.26\nSEX: M\nISS: East Grestin\nEXP: 1989.09.11',
        'certificate_of_vaccination': 'NAME: Savelle, Giovanni\nID#: TZRFY-N0BXO\nVACCINES: yellow fever, polio, hepatitis B, tetanus',
        'access_permit': 'NAME: Savelle, Giovanni\nNATION: Obristan\nID#: TZRFY-N0BXO\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 183cm\nWEIGHT: 115kg\nEXP: 1986.12.18'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: T1KYQ-DF7B4\nNATION: United Federation\nNAME: Dvorkin, Daniela\nDOB: 1951.09.04\nSEX: F\nISS: St. Marmero\nEXP: 1991.09.08',
        'certificate_of_vaccination': 'NAME: Dvorkin, Daniela\nID#: T1KYQ-DF7B4\nVACCINES: yellow fever, cowpox, tetanus, rubella',
        'access_permit': 'NAME: Dvorkin, Daniela\nNATION: United Federation\nID#: T1KYQ-DF7B4\nPURPOSE: WORK\nDURATION: 1 MONTH\nHEIGHT: 164cm\nWEIGHT: 74kg\nEXP: 1986.05.09',
        'work_pass': 'NAME: Dvorkin, Daniela\nFIELD: Fine arts\nEXP: 1987.03.01'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: PWIN0-YELWG\nNATION: Obristan\nNAME: Hammerstein, Carmen\nDOB: 1961.06.27\nSEX: F\nISS: Paradizna\nEXP: 1981.06.16',
        'certificate_of_vaccination': 'NAME: Hammerstein, Carmen\nID#: PWIN0-YELWG\nVACCINES: yellow fever, tetanus, polio, cowpox',
        'access_permit': 'NAME: Hammerstein, Carmen\nNATION: Obristan\nID#: PWIN0-YELWG\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 153cm\nWEIGHT: 81kg\nEXP: 1990.09.10'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: OGXSR-7902U\nNATION: Kolechia\nNAME: Borg, Cheyenne\nDOB: 1966.11.16\nSEX: F\nISS: Paradizna\nEXP: 1985.05.19',
        'certificate_of_vaccination': 'NAME: Borg, Cheyenne\nID#: OGXSR-7902U\nVACCINES: measles, HPV',
        'grant_of_asylum': 'NAME: Borg, Cheyenne\nNATION: Kolechia\nID#: C3WOA-UT2F5\nHEIGHT: 176cm\nWEIGHT: 82kg\nEXP: 1993.07.12'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: JXRZ9-HRJ5N\nNATION: Obristan\nNAME: Costa, Julia\nDOB: 1969.03.15\nSEX: F\nISS: Vedor\nEXP: 1992.03.23',
        'certificate_of_vaccination': 'NAME: Costa, Julia\nID#: JXRZ9-HRJ5N\nVACCINES: yellow fever, polio, tetanus, cowpox',
        'access_permit': 'NAME: Costa, Julia\nNATION: Obristan\nID#: JXRZ9-HRJ5N\nPURPOSE: VISIT\nDURATION: 1 MONTH\nHEIGHT: 166cm\nWEIGHT: 129kg\nEXP: 1984.01.07'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    bulletin = """Citizens of Republia, Kolechia, Obristan, Antegria require rubella vaccination
Wanted by the State: Felicia Schulz"""
    inspector.receive_bulletin(bulletin)

    person = {
        'certificate_of_vaccination': 'NAME: Zajak, Juliette\nID#: 7M0SD-NXU8B\nVACCINES: rubella, tetanus, polio, yellow fever',
        'diplomatic_authorization': 'NAME: Zajak, Juliette\nNATION: Obristan\nID#: 7M0SD-NXU8B\nACCESS: Impor, Antegria, United Federation'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    person = {
        'passport': 'ID#: KDC5M-MYQDH\nNATION: Impor\nNAME: Henriksson, Gabriela\nDOB: 1958.05.20\nSEX: F\nISS: True Glorian\nEXP: 1987.10.22',
        'certificate_of_vaccination': 'NAME: Henriksson, Gabriela\nID#: KDC5M-MYQDH\nVACCINES: yellow fever, tetanus, tuberculosis, rubella',
        'access_permit': 'NAME: Henriksson, Gabriela\nNATION: Impor\nID#: KDC5M-MYQDH\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 188cm\nWEIGHT: 56kg\nEXP: 1990.12.05'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: OQ8XU-EUPLB\nNATION: Antegria\nNAME: Smirnov, Joachim\nDOB: 1964.03.22\nSEX: M\nISS: Great Rapid\nEXP: 1992.10.24',
        'certificate_of_vaccination': 'NAME: Smirnov, Joachim\nID#: OQ8XU-EUPLB\nVACCINES: rubella, yellow fever, tetanus, cowpox',
        'access_permit': 'NAME: Smirnov, Joachim\nNATION: Antegria\nID#: OQ8XU-EUPLB\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 179cm\nWEIGHT: 92kg\nEXP: 1984.01.25'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: XRBQI-WZRTK\nNATION: United Federation\nNAME: Sousa, Ivana\nDOB: 1956.01.18\nSEX: F\nISS: Outer Grouse\nEXP: 1993.07.20',
        'certificate_of_vaccination': 'NAME: Sousa, Ivana\nID#: XRBQI-WZRTK\nVACCINES: tetanus, rubella, yellow fever, tuberculosis',
        'access_permit': 'NAME: Sousa, Ivana\nNATION: United Federation\nID#: XRBQI-WZRTK\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 173cm\nWEIGHT: 50kg\nEXP: 1989.09.28'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: BMDGI-YSKIE\nNATION: Arstotzka\nNAME: Bosch, Ada\nDOB: 1960.06.24\nSEX: F\nISS: Enkyo\nEXP: 1984.11.18',
        'certificate_of_vaccination': 'NAME: Bosch, Ada\nID#: BMDGI-YSKIE\nVACCINES: tetanus, tuberculosis, rubella, HPV',
        'ID_card': 'NAME: Bosch, Ada\nDOB: 1960.06.24\nHEIGHT: 198cm\nWEIGHT: 103kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: ZE641-J682I\nNATION: Antegria\nNAME: Ortiz, Evgeny\nDOB: 1963.04.10\nSEX: M\nISS: Enkyo\nEXP: 1988.06.27',
        'certificate_of_vaccination': 'NAME: Ortiz, Evgeny\nID#: ZE641-J682I\nVACCINES: yellow fever, tuberculosis, tetanus, rubella',
        'access_permit': 'NAME: Ortiz, Evgeny\nNATION: Antegria\nID#: ZE641-J682I\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 193cm\nWEIGHT: 43kg\nEXP: 1991.06.13'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: VJIW4-OLE6X\nNATION: Impor\nNAME: Kerr, Romeo\nDOB: 1966.05.03\nSEX: M\nISS: Skal\nEXP: 1984.09.16',
        'certificate_of_vaccination': 'NAME: Kerr, Romeo\nID#: VJIW4-OLE6X\nVACCINES: tetanus, HPV, cowpox, yellow fever',
        'diplomatic_authorization': 'NAME: Kerr, Romeo\nNATION: Impor\nID#: VJIW4-OLE6X\nACCESS: Republia, Arstotzka'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: DFW0V-IO341\nNATION: United Federation\nNAME: Burke, Freja\nDOB: 1954.02.20\nSEX: F\nISS: St. Marmero\nEXP: 1983.11.26',
        'certificate_of_vaccination': 'NAME: Burke, Freja\nID#: DFW0V-IO341\nVACCINES: tetanus, yellow fever, tuberculosis, polio',
        'diplomatic_authorization': 'NAME: Burke, Freja\nNATION: United Federation\nID#: DFW0V-IO341\nACCESS: Kolechia, Arstotzka, Impor'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: FCM2A-DE7CX\nNATION: Republia\nNAME: Tolaj, David\nDOB: 1958.07.01\nSEX: M\nISS: True Glorian\nEXP: 1987.08.26',
        'certificate_of_vaccination': 'NAME: Tolaj, David\nID#: FCM2A-DE7CX\nVACCINES: rubella, yellow fever, HPV, tetanus',
        'access_permit': 'NAME: Tolaj, David\nNATION: Republia\nID#: FCM2A-DE7CX\nPURPOSE: VISIT\nDURATION: 3 MONTHS\nHEIGHT: 169cm\nWEIGHT: 54kg\nEXP: 1991.10.07'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: I1UY7-H4TKY\nNATION: Republia\nNAME: Steinberg, Eva\nDOB: 1950.07.02\nSEX: F\nISS: Mergerous\nEXP: 1991.10.16',
        'certificate_of_vaccination': 'NAME: Steinberg, Eva\nID#: I1UY7-H4TKY\nVACCINES: HPV',
        'access_permit': 'NAME: Steinberg, Eva\nNATION: Republia\nID#: I1UY7-H4TKY\nPURPOSE: WORK\nDURATION: 2 MONTHS\nHEIGHT: 148cm\nWEIGHT: 51kg\nEXP: 1982.02.24'}
    assert inspector.inspect(person) == 'Entry denied: access permit expired.'

    person = {
        'passport': 'ID#: 2X7IB-0LDAP\nNATION: Arstotzka\nNAME: Schulz, Felicia\nDOB: 1955.02.26\nSEX: M\nISS: Great Rapid\nEXP: 1993.03.18',
        'ID_card': 'NAME: Schulz, Felicia\nDOB: 1991.08.30\nHEIGHT: 170cm\nWEIGHT: 129kg'}
    assert inspector.inspect(person) == 'Detainment: date of birth mismatch.'

    person = {
        'passport': 'ID#: 60NXJ-HRDOG\nNATION: Impor\nNAME: Zajak, Erik\nDOB: 1952.10.09\nSEX: M\nISS: Lesrenadi\nEXP: 1993.10.02',
        'certificate_of_vaccination': 'NAME: Zajak, Erik\nID#: 60NXJ-HRDOG\nVACCINES: typhus, yellow fever, HPV, tetanus',
        'access_permit': 'NAME: Zajak, Erik\nNATION: Impor\nID#: 60NXJ-HRDOG\nPURPOSE: WORK\nDURATION: 2 MONTHS\nHEIGHT: 171cm\nWEIGHT: 67kg\nEXP: 1984.05.31',
        'work_pass': 'NAME: Zajak, Erik\nFIELD: Engineering\nEXP: 1993.07.07'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: VX67Y-CEU81\nNATION: Arstotzka\nNAME: Kaczynska, Simon\nDOB: 1952.10.19\nSEX: M\nISS: Haihan\nEXP: 1989.02.08',
        'certificate_of_vaccination': 'NAME: Kaczynska, Simon\nID#: VX67Y-CEU81\nVACCINES: cholera, typhus, tetanus, hepatitis B',
        'ID_card': 'NAME: Kaczynska, Simon\nDOB: 1952.10.19\nHEIGHT: 181cm\nWEIGHT: 55kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: Q67YD-Z2J5L\nNATION: Republia\nNAME: Smirnov, Yelena\nDOB: 1953.09.15\nSEX: F\nISS: Lorndaz\nEXP: 1987.03.21',
        'certificate_of_vaccination': 'NAME: Smirnov, Yelena\nID#: Q67YD-Z2J5L\nVACCINES: yellow fever, rubella, hepatitis B, tetanus',
        'access_permit': 'NAME: Smirnov, Yelena\nNATION: Republia\nID#: Q67YD-Z2J5L\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 160cm\nWEIGHT: 62kg\nEXP: 1993.02.04'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    bulletin = """Allow citizens of United Federation, Kolechia, Obristan, Republia
Wanted by the State: Sergey Diaz"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: 4OLWI-FDN7U\nNATION: Impor\nNAME: Diaz, Sergey\nDOB: 1956.12.09\nSEX: M\nISS: Tsunkeido\nEXP: 1991.02.22',
        'certificate_of_vaccination': 'NAME: Diaz, Sergey\nID#: 4OLWI-FDN7U\nVACCINES: measles, hepatitis B',
        'access_permit': 'NAME: Diaz, Sergey\nNATION: Impor\nID#: 7BMHJ-Y4BE5\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 177cm\nWEIGHT: 130kg\nEXP: 1989.06.16'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: DNOMI-WU9J1\nNATION: Kolechia\nNAME: Rosebrova, Julio\nDOB: 1957.08.13\nSEX: M\nISS: Vedor\nEXP: 1991.03.23',
        'certificate_of_vaccination': 'NAME: Rosebrova, Julio\nID#: DNOMI-WU9J1\nVACCINES: typhus',
        'diplomatic_authorization': 'NAME: Rosebrova, Julio\nNATION: Kolechia\nID#: DNOMI-WU9J1\nACCESS: Impor'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    person = {
        'passport': 'ID#: 0FI5R-2QVGH\nNATION: Obristan\nNAME: Weisz, Lisa\nDOB: 1958.10.26\nSEX: F\nISS: St. Marmero\nEXP: 1983.12.09',
        'certificate_of_vaccination': 'NAME: Weisz, Lisa\nID#: 0FI5R-2QVGH\nVACCINES: tetanus, rubella, yellow fever, polio',
        'access_permit': 'NAME: Weisz, Lisa\nNATION: Antegria\nID#: 0FI5R-2QVGH\nPURPOSE: WORK\nDURATION: 6 MONTHS\nHEIGHT: 158cm\nWEIGHT: 129kg\nEXP: 1985.11.06',
        'work_pass': 'NAME: Weisz, Lisa\nFIELD: Agriculture\nEXP: 1981.03.13'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: WGBDV-9PSD5\nNATION: Obristan\nNAME: Tolaj, Carmen\nDOB: 1957.01.09\nSEX: F\nISS: Korista City\nEXP: 1986.06.17',
        'certificate_of_vaccination': 'NAME: Tolaj, Carmen\nID#: WGBDV-9PSD5\nVACCINES: tetanus, polio, yellow fever, rubella',
        'grant_of_asylum': 'NAME: Tolaj, Carmen\nNATION: Obristan\nID#: WGBDV-9PSD5\nHEIGHT: 162cm\nWEIGHT: 91kg\nEXP: 1985.11.01'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 2IW5K-IQSCW\nNATION: Obristan\nNAME: Mikkelson, Ava\nDOB: 1956.04.24\nSEX: F\nISS: Bostan\nEXP: 1984.01.06',
        'certificate_of_vaccination': 'NAME: Mikkelson, Ava\nID#: 2IW5K-IQSCW\nVACCINES: yellow fever, tetanus, polio, rubella',
        'access_permit': 'NAME: Mikkelson, Ava\nNATION: Obristan\nID#: 2IW5K-IQSCW\nPURPOSE: VISIT\nDURATION: 1 MONTH\nHEIGHT: 155cm\nWEIGHT: 41kg\nEXP: 1990.03.09'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: T617X-7AIXK\nNATION: Republia\nNAME: Kowalska, Paulina\nDOB: 1958.08.05\nSEX: F\nISS: Mergerous\nEXP: 1993.09.22',
        'grant_of_asylum': 'NAME: Kowalska, Paulina\nNATION: Republia\nID#: T617X-7AIXK\nHEIGHT: 191cm\nWEIGHT: 44kg\nEXP: 1980.05.07'}
    assert inspector.inspect(person) == 'Entry denied: grant of asylum expired.'

    person = {
        'passport': 'ID#: 8WAJQ-5GRSE\nNATION: Kolechia\nNAME: Diaz, Sergey\nDOB: 1961.03.23\nSEX: F\nISS: Mergerous\nEXP: 1987.02.22',
        'certificate_of_vaccination': 'NAME: Diaz, Sergey\nID#: 8WAJQ-5GRSE\nVACCINES: yellow fever, polio, tetanus, rubella',
        'diplomatic_authorization': 'NAME: Diaz, Sergey\nNATION: Kolechia\nID#: 8WAJQ-5GRSE\nACCESS: Arstotzka, United Federation, Republia, Antegria'}
    assert inspector.inspect(person) == 'Detainment: Entrant is a wanted criminal.'

    person = {
        'passport': 'ID#: 24FEK-G96ID\nNATION: Impor\nNAME: Lukowski, Anita\nDOB: 1969.06.18\nSEX: F\nISS: East Grestin\nEXP: 1983.10.03',
        'certificate_of_vaccination': 'NAME: Lukowski, Anita\nID#: 24FEK-G96ID\nVACCINES: tetanus, cholera, yellow fever, rubella',
        'diplomatic_authorization': 'NAME: Lukowski, Anita\nNATION: Impor\nID#: 24FEK-G96ID\nACCESS: Republia, Arstotzka, Obristan'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: BEH0O-C4BRH\nNATION: Impor\nNAME: Rosebrova, Eleanor\nDOB: 1969.10.24\nSEX: F\nISS: Orvech Vonor\nEXP: 1983.07.31',
        'certificate_of_vaccination': 'NAME: Rosebrova, Eleanor\nID#: BEH0O-C4BRH\nVACCINES: HPV, cholera, yellow fever, tetanus',
        'access_permit': 'NAME: Rosebrova, Eleanor\nNATION: Impor\nID#: BEH0O-C4BRH\nPURPOSE: VISIT\nDURATION: 2 MONTHS\nHEIGHT: 173cm\nWEIGHT: 86kg\nEXP: 1984.05.31'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: ZW9A5-83MDU\nNATION: Arstotzka\nNAME: Murphy, Igor\nDOB: 1963.09.30\nSEX: M\nISS: Tsunkeido\nEXP: 1982.09.27',
        'certificate_of_vaccination': 'NAME: Murphy, Igor\nID#: ZW9A5-83MDU\nVACCINES: polio, rubella, tuberculosis',
        'ID_card': 'NAME: Murphy, Igor\nDOB: 1963.09.30\nHEIGHT: 162cm\nWEIGHT: 103kg'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: ICJYS-QK4H8\nNATION: Kolechia\nNAME: Savelle, Abdullah\nDOB: 1962.06.11\nSEX: M\nISS: Glorian\nEXP: 1983.05.02',
        'certificate_of_vaccination': 'NAME: Savelle, Abdullah\nID#: ICJYS-QK4H8\nVACCINES: tuberculosis',
        'access_permit': 'NAME: Savelle, Abdullah\nNATION: Obristan\nID#: ICJYS-QK4H8\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 149cm\nWEIGHT: 51kg\nEXP: 1993.02.19'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: VAB59-B1ZSG\nNATION: Kolechia\nNAME: Jensen, Alberta\nDOB: 1954.12.08\nSEX: F\nISS: Lesrenadi\nEXP: 1992.07.15',
        'certificate_of_vaccination': 'NAME: Jensen, Alberta\nID#: VAB59-B1ZSG\nVACCINES: HPV',
        'access_permit': 'NAME: Jensen, Alberta\nNATION: Republia\nID#: VAB59-B1ZSG\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 147cm\nWEIGHT: 96kg\nEXP: 1989.08.07'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: NI541-MU6AB\nNATION: Impor\nNAME: Newman, Abdullah\nDOB: 1954.08.13\nSEX: M\nISS: Lesrenadi\nEXP: 1984.10.02',
        'certificate_of_vaccination': 'NAME: Newman, Abdullah\nID#: NI541-MU6AB\nVACCINES: HPV, tetanus, yellow fever, typhus',
        'diplomatic_authorization': 'NAME: Newman, Abdullah\nNATION: Impor\nID#: NI541-MU6AB\nACCESS: United Federation, Obristan, Kolechia, Arstotzka'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: KUFNG-T6KYF\nNATION: Obristan\nNAME: Costanzo, Brenna\nDOB: 1961.10.26\nSEX: F\nISS: Paradizna\nEXP: 1987.01.02',
        'certificate_of_vaccination': 'NAME: Costanzo, Brenna\nID#: KUFNG-T6KYF\nVACCINES: polio, rubella, tetanus, yellow fever',
        'diplomatic_authorization': 'NAME: Costanzo, Brenna\nNATION: Obristan\nID#: KUFNG-T6KYF\nACCESS: Arstotzka, Impor, Republia'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Allow citizens of Antegria
Foreigners no longer require yellow fever vaccination
Wanted by the State: Renee Zajak"""
    inspector.receive_bulletin(bulletin)

    person = {'certificate_of_vaccination': 'NAME: Jordan, Emma\nID#: 7O3H4-IYOZK\nVACCINES: typhus',
              'access_permit': 'NAME: Jordan, Emma\nNATION: Kolechia\nID#: 7O3H4-IYOZK\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 174cm\nWEIGHT: 88kg\nEXP: 1985.06.21'}
    assert inspector.inspect(person) == 'Entry denied: missing required passport.'

    person = {
        'passport': 'ID#: 98OJI-OBQ4T\nNATION: Kolechia\nNAME: Jager, Peter\nDOB: 1955.09.03\nSEX: M\nISS: Enkyo\nEXP: 1985.08.30',
        'certificate_of_vaccination': 'NAME: Jager, Peter\nID#: 98OJI-OBQ4T\nVACCINES: typhus, rubella, tetanus, HPV',
        'access_permit': 'NAME: Jager, Peter\nNATION: Kolechia\nID#: 98OJI-OBQ4T\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 188cm\nWEIGHT: 71kg\nEXP: 1983.02.26'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: BL7IY-SG83W\nNATION: Obristan\nNAME: Sorenson, Calum\nDOB: 1954.01.28\nSEX: M\nISS: Skal\nEXP: 1984.08.12',
        'certificate_of_vaccination': 'NAME: Sorenson, Calum\nID#: BL7IY-SG83W\nVACCINES: rubella, polio, tetanus, cowpox',
        'access_permit': 'NAME: Sorenson, Calum\nNATION: Obristan\nID#: BL7IY-SG83W\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 193cm\nWEIGHT: 93kg\nEXP: 1987.07.12'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: L5HF1-MALTQ\nNATION: Arstotzka\nNAME: Zhang, Katarina\nDOB: 1952.07.17\nSEX: F\nISS: Glorian\nEXP: 1990.01.17',
        'certificate_of_vaccination': 'NAME: Zhang, Katarina\nID#: L5HF1-MALTQ\nVACCINES: hepatitis B, typhus, tetanus, tuberculosis',
        'ID_card': 'NAME: Zhang, Katarina\nDOB: 1952.07.17\nHEIGHT: 172cm\nWEIGHT: 79kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: S23BG-FMPZY\nNATION: Arstotzka\nNAME: Nityev, Malva\nDOB: 1954.06.13\nSEX: F\nISS: Orvech Vonor\nEXP: 1990.04.21',
        'certificate_of_vaccination': 'NAME: Nityev, Malva\nID#: S23BG-FMPZY\nVACCINES: tetanus, cowpox, tuberculosis, measles',
        'ID_card': 'NAME: Nityev, Malva\nDOB: 1954.06.13\nHEIGHT: 197cm\nWEIGHT: 50kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: 1UI8J-ZW7X3\nNATION: Impor\nNAME: Quinn, Jonathan\nDOB: 1952.09.28\nSEX: M\nISS: West Grestin\nEXP: 1985.08.11',
        'certificate_of_vaccination': 'NAME: Quinn, Jonathan\nID#: 1UI8J-ZW7X3\nVACCINES: tetanus, cholera, cowpox, HPV',
        'access_permit': 'NAME: Quinn, Jonathan\nNATION: Impor\nID#: 1UI8J-ZW7X3\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 148cm\nWEIGHT: 109kg\nEXP: 1988.07.05'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: 1IVNZ-DX5B4\nNATION: Antegria\nNAME: Krug, Sarah\nDOB: 1962.07.18\nSEX: F\nISS: Haihan\nEXP: 1990.12.24',
        'certificate_of_vaccination': 'NAME: Krug, Sarah\nID#: 1IVNZ-DX5B4\nVACCINES: cholera, hepatitis B, tetanus, rubella',
        'diplomatic_authorization': 'NAME: Krug, Sarah\nNATION: Antegria\nID#: 1IVNZ-DX5B4\nACCESS: Obristan, Arstotzka, Republia, Impor'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 0JK4F-BK8HT\nNATION: Arstotzka\nNAME: Praskovic, Rafal\nDOB: 1964.07.17\nSEX: M\nISS: Outer Grouse\nEXP: 1985.08.13',
        'certificate_of_vaccination': 'NAME: Praskovic, Rafal\nID#: 0JK4F-BK8HT\nVACCINES: measles, tetanus, cowpox, yellow fever',
        'ID_card': 'NAME: Praskovic, Rafal\nDOB: 1964.07.17\nHEIGHT: 175cm\nWEIGHT: 59kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: YGM0U-5L8ST\nNATION: United Federation\nNAME: Bullock, Bruno\nDOB: 1952.05.23\nSEX: M\nISS: West Grestin\nEXP: 1992.02.24',
        'certificate_of_vaccination': 'NAME: Bullock, Bruno\nID#: YGM0U-5L8ST\nVACCINES: rubella, measles, typhus',
        'diplomatic_authorization': 'NAME: Bullock, Bruno\nNATION: United Federation\nID#: YGM0U-5L8ST\nACCESS: Impor, Antegria, Obristan, Republia'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    person = {
        'passport': 'ID#: 3D2VU-EHYM1\nNATION: Obristan\nNAME: Strauss, Roberta\nDOB: 1958.05.01\nSEX: F\nISS: Korista City\nEXP: 1982.02.08',
        'certificate_of_vaccination': 'NAME: Strauss, Roberta\nID#: 3D2VU-EHYM1\nVACCINES: HPV',
        'access_permit': 'NAME: Strauss, Roberta\nNATION: Obristan\nID#: 3D2VU-EHYM1\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 194cm\nWEIGHT: 86kg\nEXP: 1982.07.22'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: VJP3I-W4ICT\nNATION: Arstotzka\nNAME: Atreides, Rasmus\nDOB: 1969.12.20\nSEX: M\nISS: West Grestin\nEXP: 1984.09.28',
        'certificate_of_vaccination': 'NAME: Atreides, Rasmus\nID#: VJP3I-W4ICT\nVACCINES: yellow fever, hepatitis B, tetanus, measles',
        'ID_card': 'NAME: Atreides, Rasmus\nDOB: 1969.12.20\nHEIGHT: 165cm\nWEIGHT: 92kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: HSUY1-LD9W0\nNATION: Impor\nNAME: Gregorovich, Emil\nDOB: 1950.11.17\nSEX: M\nISS: Enkyo\nEXP: 1982.11.04',
        'certificate_of_vaccination': 'NAME: Gregorovich, Emil\nID#: HSUY1-LD9W0\nVACCINES: tuberculosis, cowpox, hepatitis B, tetanus',
        'grant_of_asylum': 'NAME: Gregorovich, Emil\nNATION: Impor\nID#: HSUY1-LD9W0\nHEIGHT: 208cm\nWEIGHT: 104kg\nEXP: 1985.02.04'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: H3Z61-4FL9J\nNATION: Arstotzka\nNAME: Zajak, Nikola\nDOB: 1964.08.17\nSEX: F\nISS: Korista City\nEXP: 1990.11.21',
        'certificate_of_vaccination': 'NAME: Zajak, Nikola\nID#: H3Z61-4FL9J\nVACCINES: tetanus, HPV, hepatitis B, typhus',
        'ID_card': 'NAME: Zajak, Nikola\nDOB: 1964.08.17\nHEIGHT: 185cm\nWEIGHT: 110kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: 87K92-TVUIJ\nNATION: Kolechia\nNAME: Hansson, Michaela\nDOB: 1965.11.04\nSEX: F\nISS: Orvech Vonor\nEXP: 1990.06.09',
        'certificate_of_vaccination': 'NAME: Hansson, Michaela\nID#: 87K92-TVUIJ\nVACCINES: measles, tetanus, rubella, yellow fever',
        'access_permit': 'NAME: Hansson, Michaela\nNATION: Kolechia\nID#: 87K92-TVUIJ\nPURPOSE: VISIT\nDURATION: 3 MONTHS\nHEIGHT: 176cm\nWEIGHT: 97kg\nEXP: 1990.12.16'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Allow citizens of Impor
Deny citizens of Republia, Kolechia, Antegria
Citizens of Kolechia, Antegria, Impor require cowpox vaccination
Entrants no longer require tetanus vaccination
Wanted by the State: Beatrix Petrova"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: DQOJX-XJCZ7\nNATION: Republia\nNAME: Xavier, Maciej\nDOB: 1961.12.26\nSEX: M\nISS: Mergerous\nEXP: 1980.07.14',
        'certificate_of_vaccination': 'NAME: Xavier, Maciej\nID#: DQOJX-XJCZ7\nVACCINES: typhus, tetanus, rubella, measles',
        'grant_of_asylum': 'NAME: Xavier, Maciej\nNATION: Republia\nID#: DQOJX-XJCZ7\nHEIGHT: 170cm\nWEIGHT: 127kg\nEXP: 1984.06.29'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: 75U1O-FCPWK\nNATION: United Federation\nNAME: Jung, Zera\nDOB: 1957.08.01\nSEX: F\nISS: Shingleton\nEXP: 1985.01.02'}
    assert inspector.inspect(person) == 'Entry denied: missing required access permit.'

    person = {
        'passport': 'ID#: BPDYE-61LRW\nNATION: Antegria\nNAME: Spektor, Claude\nDOB: 1970.12.29\nSEX: M\nISS: Mergerous\nEXP: 1989.09.01',
        'certificate_of_vaccination': 'NAME: Spektor, Claude\nID#: BPDYE-61LRW\nVACCINES: yellow fever, hepatitis B'}
    assert inspector.inspect(person) == 'Entry denied: missing required access permit.'

    person = {
        'passport': 'ID#: KAHSQ-VMYPF\nNATION: Arstotzka\nNAME: Zhang, Julia\nDOB: 1968.12.05\nSEX: F\nISS: Haihan\nEXP: 1991.02.24',
        'ID_card': 'NAME: Zhang, Julia\nDOB: 1968.12.05\nHEIGHT: 158cm\nWEIGHT: 80kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: YE8F1-Y0RP7\nNATION: Arstotzka\nNAME: Smirnov, Jorge\nDOB: 1968.01.30\nSEX: M\nISS: Enkyo\nEXP: 1985.01.27',
        'ID_card': 'NAME: Smirnov, Jorge\nDOB: 1968.01.30\nHEIGHT: 186cm\nWEIGHT: 123kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: 75LHX-9F2QD\nNATION: Republia\nNAME: Muller, Lars\nDOB: 1957.12.30\nSEX: M\nISS: St. Marmero\nEXP: 1982.09.07',
        'diplomatic_authorization': 'NAME: Muller, Lars\nNATION: Republia\nID#: 75LHX-9F2QD\nACCESS: Antegria, Kolechia'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: 6Z75O-C1JM4\nNATION: Obristan\nNAME: Frank, Vincent\nDOB: 1957.01.29\nSEX: M\nISS: Paradizna\nEXP: 1984.07.22',
        'certificate_of_vaccination': 'NAME: Frank, Vincent\nID#: 6Z75O-C1JM4\nVACCINES: cowpox, rubella, polio, tuberculosis',
        'grant_of_asylum': 'NAME: Frank, Vincent\nNATION: Obristan\nID#: 6Z75O-C1JM4\nHEIGHT: 151cm\nWEIGHT: 59kg\nEXP: 1989.02.16'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: OE0R4-O7DK8\nNATION: Antegria\nNAME: Romanoff, Josephine\nDOB: 1956.03.02\nSEX: F\nISS: Tsunkeido\nEXP: 1981.02.04',
        'certificate_of_vaccination': 'NAME: Romanoff, Josephine\nID#: OE0R4-O7DK8\nVACCINES: cholera, measles, cowpox, rubella',
        'diplomatic_authorization': 'NAME: Romanoff, Josephine\nNATION: Antegria\nID#: OE0R4-O7DK8\nACCESS: Impor, Obristan, Arstotzka, Republia'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: 5ZDX1-7PF52\nNATION: Arstotzka\nNAME: Aji, Sasha\nDOB: 1953.04.07\nSEX: M\nISS: Shingleton\nEXP: 1993.11.01',
        'ID_card': 'NAME: Aji, Sasha\nDOB: 1953.04.07\nHEIGHT: 199cm\nWEIGHT: 96kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: 0E7LW-3SRPV\nNATION: Republia\nNAME: Rasmussen, Yvonna\nDOB: 1954.12.18\nSEX: F\nISS: St. Marmero\nEXP: 1982.01.28',
        'certificate_of_vaccination': 'NAME: Rasmussen, Yvonna\nID#: 0E7LW-3SRPV\nVACCINES: rubella, cowpox, measles, HPV',
        'diplomatic_authorization': 'NAME: Rasmussen, Yvonna\nNATION: Republia\nID#: 0E7LW-3SRPV\nACCESS: Antegria, Obristan, Kolechia, Impor, Arstotzka'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: 92TWE-ZT5O8\nNATION: Impor\nNAME: Kerr, Nikolas\nDOB: 1967.03.15\nSEX: M\nISS: Enkyo\nEXP: 1988.12.15',
        'certificate_of_vaccination': 'NAME: Kerr, Nikolas\nID#: 92TWE-ZT5O8\nVACCINES: cholera, typhus, cowpox, polio',
        'diplomatic_authorization': 'NAME: Kerr, Nikolas\nNATION: Impor\nID#: 92TWE-ZT5O8\nACCESS: Arstotzka, Kolechia, Obristan, United Federation'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: TRMP4-OG17Y\nNATION: Arstotzka\nNAME: Spektor, Natalya\nDOB: 1960.01.29\nSEX: F\nISS: Mergerous\nEXP: 1990.11.24',
        'ID_card': 'NAME: Spektor, Natalya\nDOB: 1960.01.29\nHEIGHT: 152cm\nWEIGHT: 79kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: RJ92W-GFN47\nNATION: Obristan\nNAME: Mateo, Giovanni\nDOB: 1953.04.20\nSEX: M\nISS: Vedor\nEXP: 1983.08.19',
        'certificate_of_vaccination': 'NAME: Mateo, Giovanni\nID#: RJ92W-GFN47\nVACCINES: yellow fever, rubella, typhus, polio',
        'grant_of_asylum': 'NAME: Mateo, Giovanni\nNATION: Obristan\nID#: RJ92W-GFN47\nHEIGHT: 192cm\nWEIGHT: 80kg\nEXP: 1988.02.11'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Allow citizens of Republia
Entrants require tuberculosis vaccination
Wanted by the State: Ivanka Steiner"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: 3ARJS-GEXB8\nNATION: Republia\nNAME: Crechiolo, Carmen\nDOB: 1950.02.10\nSEX: F\nISS: Korista City\nEXP: 1990.07.03',
        'certificate_of_vaccination': 'NAME: Crechiolo, Carmen\nID#: 3ARJS-GEXB8\nVACCINES: HPV, cowpox',
        'access_permit': 'NAME: Crechiolo, Carmen\nNATION: Republia\nID#: XE6DU-KHEIN\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 192cm\nWEIGHT: 94kg\nEXP: 1990.06.22'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: 4HBK9-2C0KB\nNATION: Arstotzka\nNAME: Steinberg, Simon\nDOB: 1962.11.23\nSEX: M\nISS: Enkyo\nEXP: 1988.09.08',
        'certificate_of_vaccination': 'NAME: Steinberg, Simon\nID#: 4HBK9-2C0KB\nVACCINES: hepatitis B, tuberculosis, typhus, tetanus',
        'ID_card': 'NAME: Steinberg, Simon\nDOB: 1962.11.23\nHEIGHT: 163cm\nWEIGHT: 118kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: R3S8G-IAEJ6\nNATION: Kolechia\nNAME: Levine, Renee\nDOB: 1959.07.12\nSEX: F\nISS: Skal\nEXP: 1993.04.01',
        'certificate_of_vaccination': 'NAME: Levine, Renee\nID#: R3S8G-IAEJ6\nVACCINES: typhus, tuberculosis, cowpox, rubella',
        'grant_of_asylum': 'NAME: Levine, Renee\nNATION: Kolechia\nID#: R3S8G-IAEJ6\nHEIGHT: 174cm\nWEIGHT: 83kg\nEXP: 1984.12.17'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: L4I9T-TRUC7\nNATION: United Federation\nNAME: Carlstrom, Mohammed\nDOB: 1951.01.24\nSEX: M\nISS: Tsunkeido\nEXP: 1993.08.09',
        'certificate_of_vaccination': 'NAME: Carlstrom, Mohammed\nID#: L4I9T-TRUC7\nVACCINES: typhus, rubella, hepatitis B, tuberculosis',
        'access_permit': 'NAME: Carlstrom, Mohammed\nNATION: United Federation\nID#: L4I9T-TRUC7\nPURPOSE: VISIT\nDURATION: 2 MONTHS\nHEIGHT: 162cm\nWEIGHT: 123kg\nEXP: 1985.10.31'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: IUP0N-YM3QE\nNATION: Impor\nNAME: Novak, Jonathan\nDOB: 1969.03.08\nSEX: M\nISS: East Grestin\nEXP: 1981.11.12',
        'certificate_of_vaccination': 'NAME: Novak, Jonathan\nID#: IUP0N-YM3QE\nVACCINES: measles, cowpox, tuberculosis, tetanus',
        'grant_of_asylum': 'NAME: Novak, Jonathan\nNATION: Impor\nID#: IUP0N-YM3QE\nHEIGHT: 173cm\nWEIGHT: 74kg\nEXP: 1988.12.09'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: I5YEM-ZOXC2\nNATION: Arstotzka\nNAME: Reed, Artour\nDOB: 1961.01.07\nSEX: M\nISS: Yurko City\nEXP: 1985.11.06',
        'certificate_of_vaccination': 'NAME: Reed, Artour\nID#: I5YEM-ZOXC2\nVACCINES: tuberculosis, cholera, cowpox, polio',
        'ID_card': 'NAME: Reed, Artour\nDOB: 1961.01.07\nHEIGHT: 158cm\nWEIGHT: 115kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: QKZL3-VS2QJ\nNATION: Antegria\nNAME: David, Alfred\nDOB: 1967.01.02\nSEX: M\nISS: Skal\nEXP: 1981.09.24',
        'certificate_of_vaccination': 'NAME: David, Alfred\nID#: QKZL3-VS2QJ\nVACCINES: cholera, cowpox, rubella, tuberculosis',
        'access_permit': 'NAME: David, Alfred\nNATION: Antegria\nID#: QKZL3-VS2QJ\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 170cm\nWEIGHT: 112kg\nEXP: 1986.06.29'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: OJHIB-8O0R5\nNATION: Impor\nNAME: Newman, Abdullah\nDOB: 1969.04.21\nSEX: M\nISS: Orvech Vonor\nEXP: 1992.04.07',
        'certificate_of_vaccination': 'NAME: Newman, Abdullah\nID#: OJHIB-8O0R5\nVACCINES: tetanus, tuberculosis, cowpox, measles',
        'diplomatic_authorization': 'NAME: Newman, Abdullah\nNATION: Impor\nID#: OJHIB-8O0R5\nACCESS: Kolechia, United Federation, Arstotzka, Obristan, Republia'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 35PJR-M35AI\nNATION: Kolechia\nNAME: Romanowski, Boris\nDOB: 1958.12.30\nSEX: M\nISS: Haihan\nEXP: 1982.07.28',
        'certificate_of_vaccination': 'NAME: Romanowski, Boris\nID#: 35PJR-M35AI\nVACCINES: hepatitis B, rubella, cowpox, tuberculosis',
        'access_permit': 'NAME: Romanowski, Boris\nNATION: Kolechia\nID#: 35PJR-M35AI\nPURPOSE: VISIT\nDURATION: 3 MONTHS\nHEIGHT: 178cm\nWEIGHT: 63kg\nEXP: 1985.05.03'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: 58ZJ9-Q41DE\nNATION: Antegria\nNAME: Czekowicz, Artour\nDOB: 1962.06.19\nSEX: M\nISS: Haihan\nEXP: 1987.02.27',
        'certificate_of_vaccination': 'NAME: Czekowicz, Artour\nID#: 58ZJ9-Q41DE\nVACCINES: tetanus',
        'access_permit': 'NAME: Czekowicz, Artour\nNATION: Antegria\nID#: 8FBQ0-KYA7M\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 183cm\nWEIGHT: 98kg\nEXP: 1983.09.03'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    bulletin = """Allow citizens of Kolechia, Antegria
Deny citizens of Republia, Obristan, Impor
Citizens of Obristan no longer require polio vaccination
Wanted by the State: Valentina Kovacs"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: ENTB7-HOZYJ\nNATION: Obristan\nNAME: Blanco, Gaston\nDOB: 1968.03.07\nSEX: M\nISS: East Grestin\nEXP: 1990.12.30',
        'certificate_of_vaccination': 'NAME: Blanco, Gaston\nID#: ENTB7-HOZYJ\nVACCINES: tuberculosis, tetanus, cowpox, rubella',
        'access_permit': 'NAME: Blanco, Gaston\nNATION: Obristan\nID#: ENTB7-HOZYJ\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 169cm\nWEIGHT: 65kg\nEXP: 1983.04.13'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: Q5OE7-YZOLM\nNATION: Obristan\nNAME: Aji, Freja\nDOB: 1958.10.25\nSEX: F\nISS: Paradizna\nEXP: 1985.10.19',
        'certificate_of_vaccination': 'NAME: Aji, Freja\nID#: Q5OE7-YZOLM\nVACCINES: rubella, tuberculosis, typhus, cowpox',
        'access_permit': 'NAME: Aji, Freja\nNATION: Obristan\nID#: Q5OE7-YZOLM\nPURPOSE: WORK\nDURATION: 1 YEAR\nHEIGHT: 192cm\nWEIGHT: 103kg\nEXP: 1990.06.09',
        'work_pass': 'NAME: Aji, Freja\nFIELD: Manufacturing\nEXP: 1988.10.03'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: MSBN1-PHF87\nNATION: United Federation\nNAME: Fonseca, Anastasia\nDOB: 1955.01.26\nSEX: F\nISS: St. Marmero\nEXP: 1992.06.23',
        'certificate_of_vaccination': 'NAME: Fonseca, Anastasia\nID#: MSBN1-PHF87\nVACCINES: tuberculosis, yellow fever, hepatitis B, tetanus',
        'diplomatic_authorization': 'NAME: Fonseca, Anastasia\nNATION: United Federation\nID#: MSBN1-PHF87\nACCESS: Impor, Kolechia, Republia, Arstotzka'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: O9H1P-MGJTD\nNATION: Impor\nNAME: Knapik, Bruno\nDOB: 1960.12.09\nSEX: M\nISS: Bostan\nEXP: 1987.04.20',
        'certificate_of_vaccination': 'NAME: Knapik, Bruno\nID#: O9H1P-MGJTD\nVACCINES: tetanus, cowpox, typhus, tuberculosis',
        'grant_of_asylum': 'NAME: Knapik, Bruno\nNATION: Impor\nID#: O9H1P-MGJTD\nHEIGHT: 150cm\nWEIGHT: 60kg\nEXP: 1984.07.03'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: 7SNCM-745G8\nNATION: Arstotzka\nNAME: Smirnov, Fyodor\nDOB: 1957.10.06\nSEX: M\nISS: Lesrenadi\nEXP: 1985.02.09',
        'certificate_of_vaccination': 'NAME: Smirnov, Fyodor\nID#: 7SNCM-745G8\nVACCINES: tuberculosis, measles, cholera, tetanus',
        'ID_card': 'NAME: Smirnov, Fyodor\nDOB: 1957.10.06\nHEIGHT: 180cm\nWEIGHT: 98kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: E52W4-K587U\nNATION: Arstotzka\nNAME: Conrad, Hugo\nDOB: 1959.05.09\nSEX: M\nISS: Bostan\nEXP: 1989.05.03',
        'certificate_of_vaccination': 'NAME: Conrad, Hugo\nID#: E52W4-K587U\nVACCINES: tuberculosis, measles, rubella, cholera',
        'ID_card': 'NAME: Conrad, Hugo\nDOB: 1959.05.09\nHEIGHT: 200cm\nWEIGHT: 100kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {'certificate_of_vaccination': 'NAME: Ortiz, David\nID#: WM8A7-B4QIN\nVACCINES: polio, measles',
              'diplomatic_authorization': 'NAME: Ortiz, David\nNATION: Obristan\nID#: WM8A7-B4QIN\nACCESS: Impor, Antegria'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    person = {
        'passport': 'ID#: ADK52-9Z8I4\nNATION: Obristan\nNAME: Dimitrov, Natasha\nDOB: 1956.08.21\nSEX: F\nISS: Orvech Vonor\nEXP: 1991.11.03',
        'certificate_of_vaccination': 'NAME: Dimitrov, Natasha\nID#: ADK52-9Z8I4\nVACCINES: cowpox, yellow fever, tuberculosis, rubella',
        'diplomatic_authorization': 'NAME: Dimitrov, Natasha\nNATION: Obristan\nID#: ADK52-9Z8I4\nACCESS: Arstotzka, Antegria, Impor'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: K9ZUT-AQMD6\nNATION: Arstotzka\nNAME: Kostovetsky, Martin\nDOB: 1952.06.07\nSEX: M\nISS: Tsunkeido\nEXP: 1987.09.09',
        'certificate_of_vaccination': 'NAME: Kostovetsky, Martin\nID#: K9ZUT-AQMD6\nVACCINES: typhus, rubella, cholera',
        'ID_card': 'NAME: Vazquez, Bernard\nDOB: 1952.06.07\nHEIGHT: 188cm\nWEIGHT: 54kg'}
    assert inspector.inspect(person) == 'Detainment: name mismatch.'

    person = {
        'passport': 'ID#: AZPGM-19YO3\nNATION: Impor\nNAME: Vazquez, Fyodor\nDOB: 1951.09.03\nSEX: M\nISS: Great Rapid\nEXP: 1985.10.22',
        'certificate_of_vaccination': 'NAME: Vazquez, Fyodor\nID#: AZPGM-19YO3\nVACCINES: polio, typhus'}
    assert inspector.inspect(person) == 'Entry denied: missing required access permit.'

    person = {
        'passport': 'ID#: CJG3L-WJVCH\nNATION: Impor\nNAME: Gregorovich, Adriana\nDOB: 1957.08.12\nSEX: F\nISS: Mergerous\nEXP: 1990.08.08',
        'certificate_of_vaccination': 'NAME: Gregorovich, Adriana\nID#: CJG3L-WJVCH\nVACCINES: hepatitis B, tetanus',
        'access_permit': 'NAME: Gregorovich, Adriana\nNATION: Republia\nID#: CJG3L-WJVCH\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 165cm\nWEIGHT: 68kg\nEXP: 1992.04.02'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: V1T0L-F0YHQ\nNATION: Republia\nNAME: Kovacs, Valentina\nDOB: 1954.05.08\nSEX: M\nISS: Bostan\nEXP: 1991.12.25',
        'certificate_of_vaccination': 'NAME: Kovacs, Valentina\nID#: V1T0L-F0YHQ\nVACCINES: rubella, yellow fever, tuberculosis, typhus',
        'access_permit': 'NAME: Kovacs, Valentina\nNATION: Republia\nID#: V1T0L-F0YHQ\nPURPOSE: WORK\nDURATION: 1 YEAR\nHEIGHT: 164cm\nWEIGHT: 112kg\nEXP: 1983.12.30'}
    assert inspector.inspect(person) == 'Detainment: Entrant is a wanted criminal.'

    person = {
        'passport': 'ID#: 3MSX8-ZSXEG\nNATION: Antegria\nNAME: Borg, Felicia\nDOB: 1968.08.20\nSEX: F\nISS: Great Rapid\nEXP: 1986.08.13',
        'certificate_of_vaccination': 'NAME: Borg, Felicia\nID#: 3MSX8-ZSXEG\nVACCINES: typhus',
        'grant_of_asylum': 'NAME: Borg, Felicia\nNATION: Antegria\nID#: F9HIU-CBXAS\nHEIGHT: 169cm\nWEIGHT: 87kg\nEXP: 1989.01.11'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    bulletin = """Foreigners require cholera vaccination
Wanted by the State: Katarina Bergman"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: P8ZF9-73WX0\nNATION: Arstotzka\nNAME: Vaughn, Kamala\nDOB: 1965.07.26\nSEX: F\nISS: West Grestin\nEXP: 1993.12.09',
        'certificate_of_vaccination': 'NAME: Vaughn, Kamala\nID#: P8ZF9-73WX0\nVACCINES: tuberculosis, hepatitis B, tetanus, cholera',
        'ID_card': 'NAME: Vaughn, Kamala\nDOB: 1965.07.26\nHEIGHT: 196cm\nWEIGHT: 108kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: 27DLS-05IYC\nNATION: Obristan\nNAME: Muller, Agnes\nDOB: 1959.01.20\nSEX: F\nISS: Lesrenadi\nEXP: 1992.01.01',
        'certificate_of_vaccination': 'NAME: Muller, Agnes\nID#: 27DLS-05IYC\nVACCINES: cholera, HPV, tuberculosis, rubella',
        'access_permit': 'NAME: Muller, Agnes\nNATION: Obristan\nID#: 27DLS-05IYC\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 205cm\nWEIGHT: 71kg\nEXP: 1991.08.07'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: U1N4E-N98OC\nNATION: Arstotzka\nNAME: Hammerstein, Petra\nDOB: 1970.01.26\nSEX: F\nISS: Bostan\nEXP: 1990.08.15',
        'certificate_of_vaccination': 'NAME: Hammerstein, Petra\nID#: U1N4E-N98OC\nVACCINES: yellow fever, polio, measles',
        'ID_card': 'NAME: Owsianka, Sven\nDOB: 1970.01.26\nHEIGHT: 157cm\nWEIGHT: 47kg'}
    assert inspector.inspect(person) == 'Detainment: name mismatch.'

    person = {
        'passport': 'ID#: QKUGD-Z4JRP\nNATION: Impor\nNAME: Borshiki, Karin\nDOB: 1961.01.20\nSEX: F\nISS: True Glorian\nEXP: 1990.10.25',
        'certificate_of_vaccination': 'NAME: Borshiki, Karin\nID#: QKUGD-Z4JRP\nVACCINES: yellow fever',
        'grant_of_asylum': 'NAME: Borshiki, Karin\nNATION: Impor\nID#: 8AM6Z-L572Q\nHEIGHT: 200cm\nWEIGHT: 110kg\nEXP: 1989.04.13'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: D0W4O-AKQMU\nNATION: Impor\nNAME: Zhang, Dimitry\nDOB: 1957.10.23\nSEX: M\nISS: Lesrenadi\nEXP: 1993.07.12',
        'certificate_of_vaccination': 'NAME: Zhang, Dimitry\nID#: D0W4O-AKQMU\nVACCINES: tetanus',
        'access_permit': 'NAME: Zhang, Dimitry\nNATION: Impor\nID#: D0W4O-AKQMU\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 190cm\nWEIGHT: 103kg\nEXP: 1980.05.26'}
    assert inspector.inspect(person) == 'Entry denied: access permit expired.'

    person = {
        'passport': 'ID#: TY60S-E26W8\nNATION: Antegria\nNAME: Murphy, Erika\nDOB: 1970.04.28\nSEX: F\nISS: Paradizna\nEXP: 1985.03.06',
        'certificate_of_vaccination': 'NAME: Murphy, Erika\nID#: TY60S-E26W8\nVACCINES: tuberculosis, cholera, cowpox, rubella',
        'diplomatic_authorization': 'NAME: Murphy, Erika\nNATION: Antegria\nID#: TY60S-E26W8\nACCESS: Impor, Obristan, Arstotzka, Republia, Kolechia'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: H6IRZ-T5G2B\nNATION: Kolechia\nNAME: Babayev, Sharona\nDOB: 1967.07.06\nSEX: F\nISS: Yurko City\nEXP: 1990.09.16',
        'certificate_of_vaccination': 'NAME: Babayev, Sharona\nID#: H6IRZ-T5G2B\nVACCINES: cowpox, rubella, tuberculosis, cholera',
        'access_permit': 'NAME: Babayev, Sharona\nNATION: Kolechia\nID#: H6IRZ-T5G2B\nPURPOSE: WORK\nDURATION: 1 MONTH\nHEIGHT: 171cm\nWEIGHT: 73kg\nEXP: 1980.09.16'}
    assert inspector.inspect(person) == 'Entry denied: access permit expired.'

    person = {
        'passport': 'ID#: AC4WP-G8ABQ\nNATION: United Federation\nNAME: Kirsch, Lukas\nDOB: 1961.05.05\nSEX: M\nISS: Bostan\nEXP: 1984.06.12',
        'certificate_of_vaccination': 'NAME: Kirsch, Lukas\nID#: AC4WP-G8ABQ\nVACCINES: cowpox, tuberculosis, HPV, cholera',
        'diplomatic_authorization': 'NAME: Kirsch, Lukas\nNATION: United Federation\nID#: AC4WP-G8ABQ\nACCESS: Antegria, Obristan, Arstotzka'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: V6YLO-WH3OB\nNATION: Arstotzka\nNAME: Romanoff, Nikola\nDOB: 1968.11.05\nSEX: F\nISS: Outer Grouse\nEXP: 1983.06.05',
        'ID_card': 'NAME: Romanowski, Laura\nDOB: 1968.11.05\nHEIGHT: 164cm\nWEIGHT: 128kg'}
    assert inspector.inspect(person) == 'Detainment: name mismatch.'

    person = {
        'passport': 'ID#: ZV3WY-94OMU\nNATION: United Federation\nNAME: Borg, Calum\nDOB: 1955.09.24\nSEX: M\nISS: Haihan\nEXP: 1984.11.06',
        'certificate_of_vaccination': 'NAME: Borg, Calum\nID#: ZV3WY-94OMU\nVACCINES: hepatitis B, rubella',
        'diplomatic_authorization': 'NAME: Chernovski, Robert\nNATION: United Federation\nID#: ZV3WY-94OMU\nACCESS: Republia, Obristan, Kolechia, Impor'}
    assert inspector.inspect(person) == 'Detainment: name mismatch.'

    person = {
        'passport': 'ID#: PYXE0-4VIDE\nNATION: Obristan\nNAME: Newman, Nikola\nDOB: 1958.01.15\nSEX: F\nISS: Lesrenadi\nEXP: 1987.06.15',
        'certificate_of_vaccination': 'NAME: Newman, Nikola\nID#: PYXE0-4VIDE\nVACCINES: polio',
        'grant_of_asylum': 'NAME: Newman, Nikola\nNATION: Obristan\nID#: MXH3T-TC0YA\nHEIGHT: 147cm\nWEIGHT: 48kg\nEXP: 1993.10.04'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: WIO5B-Z01KG\nNATION: Republia\nNAME: Grech, Tatiana\nDOB: 1967.12.22\nSEX: F\nISS: Orvech Vonor\nEXP: 1986.04.15',
        'certificate_of_vaccination': 'NAME: Grech, Tatiana\nID#: WIO5B-Z01KG\nVACCINES: HPV, rubella, cholera, tuberculosis',
        'diplomatic_authorization': 'NAME: Grech, Tatiana\nNATION: Republia\nID#: WIO5B-Z01KG\nACCESS: Impor, Arstotzka'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: FDPG8-PYQ0D\nNATION: Arstotzka\nNAME: Reyes, Peter\nDOB: 1958.06.17\nSEX: M\nISS: Mergerous\nEXP: 1984.07.11',
        'certificate_of_vaccination': 'NAME: Reyes, Peter\nID#: FDPG8-PYQ0D\nVACCINES: polio, yellow fever, cowpox',
        'ID_card': 'NAME: Reyes, Peter\nDOB: 1958.06.17\nHEIGHT: 174cm\nWEIGHT: 65kg'}
    assert inspector.inspect(person) == 'Entry denied: missing required vaccination.'

    person = {
        'passport': 'ID#: 4K1ET-Q73BN\nNATION: Impor\nNAME: Frank, Erika\nDOB: 1964.12.16\nSEX: F\nISS: Shingleton\nEXP: 1985.12.03',
        'certificate_of_vaccination': 'NAME: Frank, Erika\nID#: 4K1ET-Q73BN\nVACCINES: cholera, tetanus, tuberculosis, cowpox',
        'diplomatic_authorization': 'NAME: Frank, Erika\nNATION: Impor\nID#: 4K1ET-Q73BN\nACCESS: Obristan, Arstotzka'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    bulletin = """Deny citizens of Antegria, United Federation
Foreigners require typhus vaccination
Citizens of Kolechia, Antegria, Impor no longer require cowpox vaccination
Entrants no longer require tuberculosis vaccination
Wanted by the State: Felicia Odom"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: N4UCS-96BZ8\nNATION: Obristan\nNAME: Wolfe, Adam\nDOB: 1963.10.18\nSEX: M\nISS: True Glorian\nEXP: 1987.04.19',
        'certificate_of_vaccination': 'NAME: Wolfe, Adam\nID#: N4UCS-96BZ8\nVACCINES: polio, rubella, cholera, typhus',
        'access_permit': 'NAME: Wolfe, Adam\nNATION: Obristan\nID#: N4UCS-96BZ8\nPURPOSE: VISIT\nDURATION: 2 MONTHS\nHEIGHT: 210cm\nWEIGHT: 129kg\nEXP: 1988.09.03'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: 9N451-2SE38\nNATION: Arstotzka\nNAME: Lewandowski, Gustav\nDOB: 1956.02.20\nSEX: M\nISS: West Grestin\nEXP: 1982.04.25',
        'ID_card': 'NAME: Lewandowski, Gustav\nDOB: 1956.02.20\nHEIGHT: 194cm\nWEIGHT: 42kg'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: LHYN0-Q05J8\nNATION: Kolechia\nNAME: Crechiolo, Edine\nDOB: 1967.04.18\nSEX: F\nISS: Skal\nEXP: 1985.08.23',
        'certificate_of_vaccination': 'NAME: Crechiolo, Edine\nID#: LHYN0-Q05J8\nVACCINES: cholera, HPV, typhus, rubella',
        'diplomatic_authorization': 'NAME: Crechiolo, Edine\nNATION: Kolechia\nID#: LHYN0-Q05J8\nACCESS: Republia, Arstotzka'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 82EV4-2R1CH\nNATION: Republia\nNAME: Costanzo, Isabella\nDOB: 1951.11.15\nSEX: F\nISS: Outer Grouse\nEXP: 1984.01.19',
        'certificate_of_vaccination': 'NAME: Costanzo, Isabella\nID#: 82EV4-2R1CH\nVACCINES: rubella, HPV, typhus, cholera',
        'access_permit': 'NAME: Costanzo, Isabella\nNATION: Republia\nID#: 82EV4-2R1CH\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 200cm\nWEIGHT: 74kg\nEXP: 1983.12.29'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: RP69S-QHDBL\nNATION: United Federation\nNAME: Kerr, Alfred\nDOB: 1952.07.16\nSEX: M\nISS: Great Rapid\nEXP: 1985.08.17',
        'certificate_of_vaccination': 'NAME: Kerr, Alfred\nID#: RP69S-QHDBL\nVACCINES: measles, tuberculosis',
        'diplomatic_authorization': 'NAME: Kerr, Alfred\nNATION: United Federation\nID#: RP69S-QHDBL\nACCESS: Impor, Antegria, Republia'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    person = {
        'passport': 'ID#: R7Z28-VPEL1\nNATION: Antegria\nNAME: Hansson, Anton\nDOB: 1958.08.05\nSEX: M\nISS: West Grestin\nEXP: 1988.09.19',
        'certificate_of_vaccination': 'NAME: Hansson, Anton\nID#: R7Z28-VPEL1\nVACCINES: rubella, HPV, cholera, typhus',
        'grant_of_asylum': 'NAME: Hansson, Anton\nNATION: Antegria\nID#: R7Z28-VPEL1\nHEIGHT: 183cm\nWEIGHT: 53kg\nEXP: 1992.04.08'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: KR9SA-UNA8T\nNATION: Kolechia\nNAME: Thunstrom, Victoria\nDOB: 1964.01.18\nSEX: F\nISS: Vedor\nEXP: 1982.11.15',
        'certificate_of_vaccination': 'NAME: Thunstrom, Victoria\nID#: KR9SA-UNA8T\nVACCINES: hepatitis B, typhus, cholera, rubella',
        'diplomatic_authorization': 'NAME: Thunstrom, Victoria\nNATION: Kolechia\nID#: KR9SA-UNA8T\nACCESS: Obristan, Republia, Arstotzka, Impor, Antegria'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: ORMXS-KRAD9\nNATION: Impor\nNAME: Yankov, Peter\nDOB: 1966.03.15\nSEX: M\nISS: Outer Grouse\nEXP: 1984.05.21',
        'certificate_of_vaccination': 'NAME: Yankov, Peter\nID#: ORMXS-KRAD9\nVACCINES: tetanus, rubella, cholera, typhus',
        'grant_of_asylum': 'NAME: Yankov, Peter\nNATION: Impor\nID#: ORMXS-KRAD9\nHEIGHT: 201cm\nWEIGHT: 51kg\nEXP: 1987.02.08'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: ID53G-RUTIZ\nNATION: United Federation\nNAME: Sajarvi, Gabriela\nDOB: 1957.07.04\nSEX: F\nISS: Orvech Vonor\nEXP: 1987.08.08',
        'certificate_of_vaccination': 'NAME: Sajarvi, Gabriela\nID#: ID53G-RUTIZ\nVACCINES: yellow fever, polio',
        'grant_of_asylum': 'NAME: Sajarvi, Gabriela\nNATION: Kolechia\nID#: ID53G-RUTIZ\nHEIGHT: 189cm\nWEIGHT: 59kg\nEXP: 1987.05.10'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: YE1AZ-3Z0H4\nNATION: Kolechia\nNAME: Jensen, Natasha\nDOB: 1969.10.29\nSEX: F\nISS: Korista City\nEXP: 1993.04.19',
        'certificate_of_vaccination': 'NAME: Jensen, Natasha\nID#: YE1AZ-3Z0H4\nVACCINES: rubella, cowpox, cholera, typhus',
        'diplomatic_authorization': 'NAME: Jensen, Natasha\nNATION: Kolechia\nID#: YE1AZ-3Z0H4\nACCESS: Impor, Arstotzka'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Allow citizens of United Federation, Republia, Obristan, Antegria
Deny citizens of Kolechia
Citizens of Republia, Kolechia, Obristan, Antegria no longer require rubella vaccination
Wanted by the State: Elena Romanowski"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: U1W4V-QR94O\nNATION: Obristan\nNAME: Muller, Eva\nDOB: 1968.06.27\nSEX: F\nISS: Tsunkeido\nEXP: 1987.07.03',
        'certificate_of_vaccination': 'NAME: Muller, Eva\nID#: U1W4V-QR94O\nVACCINES: typhus, tetanus, cholera, yellow fever',
        'grant_of_asylum': 'NAME: Muller, Eva\nNATION: Obristan\nID#: U1W4V-QR94O\nHEIGHT: 168cm\nWEIGHT: 48kg\nEXP: 1989.07.02'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: B9TSR-B962R\nNATION: Kolechia\nNAME: Levine, Julia\nDOB: 1950.08.11\nSEX: F\nISS: Tsunkeido\nEXP: 1989.04.08',
        'certificate_of_vaccination': 'NAME: Levine, Julia\nID#: B9TSR-B962R\nVACCINES: cholera, rubella, polio, typhus',
        'access_permit': 'NAME: Levine, Julia\nNATION: Kolechia\nID#: B9TSR-B962R\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 152cm\nWEIGHT: 55kg\nEXP: 1992.04.04'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: EF8DC-LJCV3\nNATION: Antegria\nNAME: Wagner, Christoph\nDOB: 1958.01.10\nSEX: M\nISS: Glorian\nEXP: 1988.09.15',
        'certificate_of_vaccination': 'NAME: Wagner, Christoph\nID#: EF8DC-LJCV3\nVACCINES: typhus, cholera, HPV, cowpox',
        'access_permit': 'NAME: Wagner, Christoph\nNATION: Antegria\nID#: EF8DC-LJCV3\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 188cm\nWEIGHT: 46kg\nEXP: 1984.05.14'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: TJNPY-0AHMG\nNATION: Republia\nNAME: Smirnov, Samantha\nDOB: 1951.12.05\nSEX: F\nISS: Enkyo\nEXP: 1983.03.16',
        'certificate_of_vaccination': 'NAME: Smirnov, Samantha\nID#: TJNPY-0AHMG\nVACCINES: rubella, hepatitis B',
        'work_pass': 'NAME: Petrova, Pavel\nFIELD: Food service\nEXP: 1981.05.21'}
    assert inspector.inspect(person) == 'Detainment: name mismatch.'

    person = {
        'passport': 'ID#: XLMJW-3HOWF\nNATION: Kolechia\nNAME: Seczek, Samuel\nDOB: 1953.05.01\nSEX: M\nISS: Lorndaz\nEXP: 1984.03.16',
        'certificate_of_vaccination': 'NAME: Seczek, Samuel\nID#: XLMJW-3HOWF\nVACCINES: typhus, HPV, yellow fever, cholera',
        'diplomatic_authorization': 'NAME: Seczek, Samuel\nNATION: Kolechia\nID#: XLMJW-3HOWF\nACCESS: Republia, Antegria, Impor, United Federation, Arstotzka'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: 5A1YT-3TPOU\nNATION: United Federation\nNAME: Shaw, Zachary\nDOB: 1964.10.05\nSEX: M\nISS: Tsunkeido\nEXP: 1986.06.12',
        'certificate_of_vaccination': 'NAME: Shaw, Zachary\nID#: 5A1YT-3TPOU\nVACCINES: measles, typhus, cholera, rubella',
        'grant_of_asylum': 'NAME: Shaw, Zachary\nNATION: United Federation\nID#: 5A1YT-3TPOU\nHEIGHT: 189cm\nWEIGHT: 91kg\nEXP: 1983.08.08'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 8CBPR-7WZR1\nNATION: Kolechia\nNAME: Murphy, Gustav\nDOB: 1952.09.07\nSEX: M\nISS: Skal\nEXP: 1980.04.10',
        'certificate_of_vaccination': 'NAME: Murphy, Gustav\nID#: 8CBPR-7WZR1\nVACCINES: cholera, HPV, typhus, rubella',
        'access_permit': 'NAME: Murphy, Gustav\nNATION: Kolechia\nID#: 8CBPR-7WZR1\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 171cm\nWEIGHT: 126kg\nEXP: 1984.02.16'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: RKGPD-IZDOW\nNATION: Antegria\nNAME: Li, Piotr\nDOB: 1953.12.18\nSEX: M\nISS: St. Marmero\nEXP: 1991.10.18',
        'certificate_of_vaccination': 'NAME: Li, Piotr\nID#: RKGPD-IZDOW\nVACCINES: typhus, yellow fever, cholera, measles',
        'diplomatic_authorization': 'NAME: Li, Piotr\nNATION: Antegria\nID#: RKGPD-IZDOW\nACCESS: Obristan, Arstotzka'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: V4173-4H15B\nNATION: Kolechia\nNAME: Jokav, Sven\nDOB: 1958.07.02\nSEX: M\nISS: Bostan\nEXP: 1990.10.01',
        'certificate_of_vaccination': 'NAME: Jokav, Sven\nID#: V4173-4H15B\nVACCINES: measles, HPV'}
    assert inspector.inspect(person) == 'Entry denied: missing required access permit.'

    person = {
        'passport': 'ID#: NPHBM-LJ2QP\nNATION: Obristan\nNAME: Radic, Katarina\nDOB: 1961.06.07\nSEX: F\nISS: Korista City\nEXP: 1992.10.07',
        'access_permit': 'NAME: Radic, Katarina\nNATION: Antegria\nID#: NPHBM-LJ2QP\nPURPOSE: VISIT\nDURATION: 2 MONTHS\nHEIGHT: 207cm\nWEIGHT: 45kg\nEXP: 1988.03.26'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: 4K7XA-69PLZ\nNATION: Impor\nNAME: Frank, Jonathan\nDOB: 1953.03.12\nSEX: M\nISS: Vedor\nEXP: 1987.05.13',
        'certificate_of_vaccination': 'NAME: Frank, Jonathan\nID#: 4K7XA-69PLZ\nVACCINES: hepatitis B, rubella',
        'diplomatic_authorization': 'NAME: Frank, Jonathan\nNATION: Impor\nID#: 4K7XA-69PLZ\nACCESS: United Federation'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    person = {
        'passport': 'ID#: Y5TVL-XC9SF\nNATION: Republia\nNAME: Dimanishki, Cosmo\nDOB: 1962.07.25\nSEX: M\nISS: Vedor\nEXP: 1988.05.29',
        'certificate_of_vaccination': 'NAME: Dimanishki, Cosmo\nID#: Y5TVL-XC9SF\nVACCINES: typhus, HPV, cholera, polio',
        'diplomatic_authorization': 'NAME: Dimanishki, Cosmo\nNATION: Republia\nID#: Y5TVL-XC9SF\nACCESS: Kolechia, Arstotzka, Obristan'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Foreigners no longer require cholera vaccination
Wanted by the State: Evgeny Ibrahimovic"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: YX3F7-LDTJ9\nNATION: Arstotzka\nNAME: Owsianka, Nicole\nDOB: 1959.12.01\nSEX: F\nISS: Yurko City\nEXP: 1990.07.16',
        'ID_card': 'NAME: Owsianka, Nicole\nDOB: 1959.12.01\nHEIGHT: 166cm\nWEIGHT: 80kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: M40ZV-NGJ5W\nNATION: Republia\nNAME: Ibrahimovic, Evgeny\nDOB: 1954.12.15\nSEX: F\nISS: Outer Grouse\nEXP: 1980.02.10',
        'certificate_of_vaccination': 'NAME: Ibrahimovic, Evgeny\nID#: M40ZV-NGJ5W\nVACCINES: yellow fever, typhus, tuberculosis, hepatitis B',
        'access_permit': 'NAME: Ibrahimovic, Evgeny\nNATION: Republia\nID#: M40ZV-NGJ5W\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 188cm\nWEIGHT: 85kg\nEXP: 1989.04.30'}
    assert inspector.inspect(person) == 'Detainment: Entrant is a wanted criminal.'

    person = {
        'passport': 'ID#: W8GTU-TPMD9\nNATION: Republia\nNAME: Schulz, Josefina\nDOB: 1964.03.23\nSEX: F\nISS: West Grestin\nEXP: 1988.05.24',
        'certificate_of_vaccination': 'NAME: Schulz, Josefina\nID#: W8GTU-TPMD9\nVACCINES: cowpox, tetanus, measles, typhus',
        'access_permit': 'NAME: Schulz, Josefina\nNATION: Republia\nID#: W8GTU-TPMD9\nPURPOSE: VISIT\nDURATION: 3 MONTHS\nHEIGHT: 196cm\nWEIGHT: 41kg\nEXP: 1983.04.25'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: MD7JO-ZWM0V\nNATION: Obristan\nNAME: Kowalska, Danil\nDOB: 1966.01.28\nSEX: M\nISS: Mergerous\nEXP: 1986.07.28',
        'certificate_of_vaccination': 'NAME: Kowalska, Danil\nID#: MD7JO-ZWM0V\nVACCINES: cowpox, tetanus, cholera',
        'diplomatic_authorization': 'NAME: Kowalska, Danil\nNATION: Obristan\nID#: MD7JO-ZWM0V\nACCESS: Antegria, Republia, Impor'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    person = {
        'passport': 'ID#: Q6R5O-AKRIV\nNATION: Antegria\nNAME: Vaughn, Cecelia\nDOB: 1955.05.22\nSEX: F\nISS: Haihan\nEXP: 1989.06.16',
        'certificate_of_vaccination': 'NAME: Vaughn, Cecelia\nID#: Q6R5O-AKRIV\nVACCINES: tetanus, hepatitis B, measles, typhus',
        'access_permit': 'NAME: Vaughn, Cecelia\nNATION: Antegria\nID#: Q6R5O-AKRIV\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 209cm\nWEIGHT: 61kg\nEXP: 1982.12.27'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 80QPR-E895C\nNATION: Impor\nNAME: Hammacher, Cosmo\nDOB: 1969.11.24\nSEX: M\nISS: East Grestin\nEXP: 1986.05.12',
        'certificate_of_vaccination': 'NAME: Hammacher, Cosmo\nID#: 80QPR-E895C\nVACCINES: tuberculosis, hepatitis B, HPV',
        'access_permit': 'NAME: Hammacher, Cosmo\nNATION: Impor\nID#: 80QPR-E895C\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 204cm\nWEIGHT: 77kg\nEXP: 1980.10.15'}
    assert inspector.inspect(person) == 'Entry denied: access permit expired.'

    person = {
        'passport': 'ID#: 9GXRF-SRUYO\nNATION: Kolechia\nNAME: Guillot, Natasha\nDOB: 1969.01.09\nSEX: F\nISS: Paradizna\nEXP: 1984.04.25',
        'certificate_of_vaccination': 'NAME: Guillot, Natasha\nID#: 9GXRF-SRUYO\nVACCINES: tuberculosis, cowpox, rubella, typhus',
        'diplomatic_authorization': 'NAME: Guillot, Natasha\nNATION: Kolechia\nID#: 9GXRF-SRUYO\nACCESS: Arstotzka, Impor, Antegria, United Federation, Obristan'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: G1ORF-3X9WC\nNATION: Arstotzka\nNAME: Ortiz, Niel\nDOB: 1968.12.29\nSEX: M\nISS: Lorndaz\nEXP: 1989.02.25',
        'ID_card': 'NAME: Ortiz, Niel\nDOB: 1968.12.29\nHEIGHT: 208cm\nWEIGHT: 96kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: PM7D2-B8DCJ\nNATION: Kolechia\nNAME: Dimitrov, Aleksi\nDOB: 1956.07.11\nSEX: M\nISS: Outer Grouse\nEXP: 1981.03.09',
        'certificate_of_vaccination': 'NAME: Dimitrov, Aleksi\nID#: PM7D2-B8DCJ\nVACCINES: yellow fever, polio, rubella, typhus',
        'access_permit': 'NAME: Dimitrov, Aleksi\nNATION: Kolechia\nID#: PM7D2-B8DCJ\nPURPOSE: VISIT\nDURATION: 1 MONTH\nHEIGHT: 186cm\nWEIGHT: 110kg\nEXP: 1988.09.17'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: 2RMZ7-M9KX6\nNATION: Republia\nNAME: Andrevska, Wilma\nDOB: 1956.11.13\nSEX: F\nISS: Vedor\nEXP: 1991.06.28',
        'certificate_of_vaccination': 'NAME: Andrevska, Wilma\nID#: 2RMZ7-M9KX6\nVACCINES: tuberculosis, cholera, typhus, hepatitis B',
        'access_permit': 'NAME: Andrevska, Wilma\nNATION: Republia\nID#: 2RMZ7-M9KX6\nPURPOSE: WORK\nDURATION: 2 MONTHS\nHEIGHT: 160cm\nWEIGHT: 60kg\nEXP: 1992.09.10'}
    assert inspector.inspect(person) == 'Entry denied: missing required work pass.'

    bulletin = """Allow citizens of Kolechia
Wanted by the State: Sara Czekowicz"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: AGNYU-YHPKV\nNATION: Obristan\nNAME: Olah, Lukas\nDOB: 1960.04.07\nSEX: M\nISS: Bostan\nEXP: 1984.07.15',
        'certificate_of_vaccination': 'NAME: Olah, Lukas\nID#: AGNYU-YHPKV\nVACCINES: hepatitis B, cowpox, HPV, typhus',
        'grant_of_asylum': 'NAME: Olah, Lukas\nNATION: Obristan\nID#: AGNYU-YHPKV\nHEIGHT: 167cm\nWEIGHT: 53kg\nEXP: 1988.02.05'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 4E07L-YT240\nNATION: Obristan\nNAME: Olah, Renee\nDOB: 1969.05.24\nSEX: F\nISS: Bostan\nEXP: 1984.04.23',
        'certificate_of_vaccination': 'NAME: Olah, Renee\nID#: 4E07L-YT240\nVACCINES: cowpox, tuberculosis, polio, typhus',
        'diplomatic_authorization': 'NAME: Olah, Renee\nNATION: Obristan\nID#: 4E07L-YT240\nACCESS: Kolechia, Arstotzka, Republia, United Federation'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: D7UBO-69WKB\nNATION: Kolechia\nNAME: Odom, Juliette\nDOB: 1961.03.02\nSEX: F\nISS: St. Marmero\nEXP: 1982.06.01',
        'certificate_of_vaccination': 'NAME: Odom, Juliette\nID#: D7UBO-69WKB\nVACCINES: typhus, polio, tuberculosis, rubella',
        'grant_of_asylum': 'NAME: Odom, Juliette\nNATION: Kolechia\nID#: D7UBO-69WKB\nHEIGHT: 166cm\nWEIGHT: 51kg\nEXP: 1985.03.31'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: GW5A6-AIFR1\nNATION: United Federation\nNAME: Evans, Lisa\nDOB: 1962.02.14\nSEX: F\nISS: Enkyo\nEXP: 1981.01.28',
        'certificate_of_vaccination': 'NAME: Evans, Lisa\nID#: GW5A6-AIFR1\nVACCINES: measles, cholera, typhus, yellow fever',
        'access_permit': 'NAME: Evans, Lisa\nNATION: United Federation\nID#: GW5A6-AIFR1\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 176cm\nWEIGHT: 83kg\nEXP: 1983.10.25'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: V72HB-MSVAD\nNATION: Obristan\nNAME: Peterson, Malva\nDOB: 1967.01.18\nSEX: F\nISS: Tsunkeido\nEXP: 1984.01.10',
        'certificate_of_vaccination': 'NAME: Peterson, Malva\nID#: V72HB-MSVAD\nVACCINES: rubella, hepatitis B, measles',
        'access_permit': 'NAME: Peterson, Malva\nNATION: Obristan\nID#: V72HB-MSVAD\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 178cm\nWEIGHT: 45kg\nEXP: 1981.11.27'}
    assert inspector.inspect(person) == 'Entry denied: access permit expired.'

    person = {
        'passport': 'ID#: AUDTJ-JGIFY\nNATION: Antegria\nNAME: Blanco, Sara\nDOB: 1957.01.05\nSEX: F\nISS: Great Rapid\nEXP: 1988.01.14',
        'certificate_of_vaccination': 'NAME: Blanco, Sara\nID#: AUDTJ-JGIFY\nVACCINES: measles, typhus, polio, cowpox',
        'access_permit': 'NAME: Blanco, Sara\nNATION: Antegria\nID#: AUDTJ-JGIFY\nPURPOSE: WORK\nDURATION: 2 MONTHS\nHEIGHT: 199cm\nWEIGHT: 87kg\nEXP: 1992.10.28'}
    assert inspector.inspect(person) == 'Entry denied: missing required work pass.'

    person = {
        'passport': 'ID#: ULFZR-A4EO2\nNATION: Arstotzka\nNAME: Costa, Cameron\nDOB: 1959.04.23\nSEX: F\nISS: Skal\nEXP: 1993.05.30',
        'ID_card': 'NAME: Costa, Cameron\nDOB: 1959.04.23\nHEIGHT: 207cm\nWEIGHT: 82kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: TBLP7-G1ASE\nNATION: Antegria\nNAME: Macek, Guy\nDOB: 1968.10.02\nSEX: M\nISS: Yurko City\nEXP: 1983.02.19',
        'certificate_of_vaccination': 'NAME: Macek, Guy\nID#: TBLP7-G1ASE\nVACCINES: tetanus, rubella, yellow fever',
        'access_permit': 'NAME: Macek, Guy\nNATION: Antegria\nID#: TBLP7-G1ASE\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 166cm\nWEIGHT: 83kg\nEXP: 1981.06.24'}
    assert inspector.inspect(person) == 'Entry denied: access permit expired.'

    person = {
        'passport': 'ID#: WH3VY-B8XH0\nNATION: Impor\nNAME: Klaus, Malva\nDOB: 1953.03.16\nSEX: F\nISS: Bostan\nEXP: 1981.08.19',
        'certificate_of_vaccination': 'NAME: Klaus, Malva\nID#: WH3VY-B8XH0\nVACCINES: tuberculosis, measles, hepatitis B, typhus',
        'access_permit': 'NAME: Klaus, Malva\nNATION: Impor\nID#: WH3VY-B8XH0\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 149cm\nWEIGHT: 123kg\nEXP: 1987.08.21'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: 6INEB-JCSKU\nNATION: Obristan\nNAME: Lindberg, Damian\nDOB: 1958.04.29\nSEX: M\nISS: Haihan\nEXP: 1993.12.21',
        'certificate_of_vaccination': 'NAME: Lindberg, Damian\nID#: 6INEB-JCSKU\nVACCINES: cowpox, typhus, tetanus, cholera',
        'access_permit': 'NAME: Lindberg, Damian\nNATION: Obristan\nID#: 6INEB-JCSKU\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 198cm\nWEIGHT: 109kg\nEXP: 1983.12.10'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Allow citizens of Impor
Wanted by the State: Tomas Kleiner"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: GU0CQ-GHXNY\nNATION: Antegria\nNAME: Kerr, Evgeny\nDOB: 1959.02.04\nSEX: M\nISS: Great Rapid\nEXP: 1987.07.21',
        'certificate_of_vaccination': 'NAME: Kerr, Evgeny\nID#: GU0CQ-GHXNY\nVACCINES: measles, hepatitis B, polio'}
    assert inspector.inspect(person) == 'Entry denied: missing required access permit.'

    person = {
        'passport': 'ID#: 79Q06-5PU92\nNATION: Antegria\nNAME: Dahl, Ingrid\nDOB: 1952.06.04\nSEX: F\nISS: Glorian\nEXP: 1987.06.01',
        'certificate_of_vaccination': 'NAME: Dahl, Ingrid\nID#: 79Q06-5PU92\nVACCINES: cholera, cowpox, rubella',
        'access_permit': 'NAME: Dahl, Ingrid\nNATION: Antegria\nID#: 6J7DX-MABJ9\nPURPOSE: WORK\nDURATION: 3 MONTHS\nHEIGHT: 185cm\nWEIGHT: 112kg\nEXP: 1988.03.01',
        'work_pass': 'NAME: Conrad, Vilhelm\nFIELD: Sports\nEXP: 1980.08.05'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: 5YERM-UESP1\nNATION: Kolechia\nNAME: Dimitrov, Mathias\nDOB: 1966.12.24\nSEX: M\nISS: St. Marmero\nEXP: 1988.11.21',
        'certificate_of_vaccination': 'NAME: Dimitrov, Mathias\nID#: 5YERM-UESP1\nVACCINES: typhus, cowpox, yellow fever, polio',
        'grant_of_asylum': 'NAME: Dimitrov, Mathias\nNATION: Kolechia\nID#: 5YERM-UESP1\nHEIGHT: 149cm\nWEIGHT: 72kg\nEXP: 1988.07.09'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: COXHG-8W4O6\nNATION: Kolechia\nNAME: Frank, Nikolas\nDOB: 1957.07.17\nSEX: M\nISS: Lesrenadi\nEXP: 1990.12.25',
        'certificate_of_vaccination': 'NAME: Frank, Nikolas\nID#: COXHG-8W4O6\nVACCINES: cholera, cowpox, polio, typhus',
        'diplomatic_authorization': 'NAME: Frank, Nikolas\nNATION: Kolechia\nID#: COXHG-8W4O6\nACCESS: Arstotzka, Antegria, Republia'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: YL36T-JKIS2\nNATION: Impor\nNAME: Zitna, Mathias\nDOB: 1955.09.25\nSEX: M\nISS: Vedor\nEXP: 1982.01.01',
        'certificate_of_vaccination': 'NAME: Zitna, Mathias\nID#: YL36T-JKIS2\nVACCINES: tuberculosis, typhus, cowpox, measles',
        'access_permit': 'NAME: Zitna, Mathias\nNATION: Impor\nID#: YL36T-JKIS2\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 145cm\nWEIGHT: 98kg\nEXP: 1988.07.27'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: XMA8U-12AFP\nNATION: Impor\nNAME: Anderson, Danika\nDOB: 1968.10.05\nSEX: F\nISS: East Grestin\nEXP: 1987.02.20',
        'certificate_of_vaccination': 'NAME: Anderson, Danika\nID#: XMA8U-12AFP\nVACCINES: typhus, tetanus, hepatitis B, rubella',
        'diplomatic_authorization': 'NAME: Anderson, Danika\nNATION: Impor\nID#: XMA8U-12AFP\nACCESS: Arstotzka, Kolechia'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: VWD3R-G30S1\nNATION: Kolechia\nNAME: Jovanovic, Lukas\nDOB: 1955.11.02\nSEX: M\nISS: Tsunkeido\nEXP: 1993.07.30',
        'certificate_of_vaccination': 'NAME: Jovanovic, Lukas\nID#: VWD3R-G30S1\nVACCINES: rubella, cowpox, typhus, cholera',
        'access_permit': 'NAME: Jovanovic, Lukas\nNATION: Kolechia\nID#: VWD3R-G30S1\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 154cm\nWEIGHT: 78kg\nEXP: 1992.05.10'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: W2XQE-L0DN9\nNATION: Obristan\nNAME: Atreides, Daniela\nDOB: 1951.06.03\nSEX: F\nISS: Enkyo\nEXP: 1992.06.20',
        'certificate_of_vaccination': 'NAME: Atreides, Daniela\nID#: W2XQE-L0DN9\nVACCINES: typhus, tuberculosis, hepatitis B, cowpox',
        'access_permit': 'NAME: Atreides, Daniela\nNATION: Obristan\nID#: W2XQE-L0DN9\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 170cm\nWEIGHT: 107kg\nEXP: 1988.06.16'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: UMCQW-LBTNS\nNATION: Republia\nNAME: Feyd, Misha\nDOB: 1958.05.14\nSEX: F\nISS: True Glorian\nEXP: 1981.01.07',
        'certificate_of_vaccination': 'NAME: Feyd, Misha\nID#: UMCQW-LBTNS\nVACCINES: measles, yellow fever, typhus, HPV',
        'diplomatic_authorization': 'NAME: Feyd, Misha\nNATION: Republia\nID#: UMCQW-LBTNS\nACCESS: Arstotzka, Impor, Obristan'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: UGY6Q-5J10U\nNATION: Arstotzka\nNAME: Kremenliev, James\nDOB: 1970.01.21\nSEX: M\nISS: Mergerous\nEXP: 1985.02.11',
        'ID_card': 'NAME: Kremenliev, James\nDOB: 1970.01.21\nHEIGHT: 189cm\nWEIGHT: 121kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: 0JSBD-ALXRW\nNATION: Obristan\nNAME: Moldavich, Yosef\nDOB: 1951.03.13\nSEX: M\nISS: Bostan\nEXP: 1989.01.06',
        'diplomatic_authorization': 'NAME: Moldavich, Yosef\nNATION: Obristan\nID#: 0JSBD-ALXRW\nACCESS: United Federation, Impor, Kolechia, Republia'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    person = {
        'passport': 'ID#: COI6U-EQM84\nNATION: Republia\nNAME: Tolaj, Martin\nDOB: 1957.02.08\nSEX: M\nISS: Orvech Vonor\nEXP: 1985.01.22',
        'certificate_of_vaccination': 'NAME: Tolaj, Martin\nID#: COI6U-EQM84\nVACCINES: hepatitis B, typhus, polio, HPV',
        'access_permit': 'NAME: Tolaj, Martin\nNATION: Republia\nID#: COI6U-EQM84\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 208cm\nWEIGHT: 115kg\nEXP: 1988.01.04'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Citizens of Kolechia, United Federation, Obristan, Antegria require HPV vaccination
Wanted by the State: Simon Graham"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: YT1MN-MU42R\nNATION: Obristan\nNAME: Seczek, Petr\nDOB: 1952.07.28\nSEX: M\nISS: Yurko City\nEXP: 1989.04.16',
        'certificate_of_vaccination': 'NAME: Seczek, Petr\nID#: YT1MN-MU42R\nVACCINES: cowpox, tetanus, typhus, HPV',
        'access_permit': 'NAME: Seczek, Petr\nNATION: Obristan\nID#: YT1MN-MU42R\nPURPOSE: WORK\nDURATION: 1 YEAR\nHEIGHT: 164cm\nWEIGHT: 58kg\nEXP: 1983.10.12'}
    assert inspector.inspect(person) == 'Entry denied: missing required work pass.'

    person = {
        'passport': 'ID#: HC2V1-GVH6J\nNATION: United Federation\nNAME: Frederikson, Paulina\nDOB: 1955.10.29\nSEX: F\nISS: Korista City\nEXP: 1987.10.14',
        'certificate_of_vaccination': 'NAME: Frederikson, Paulina\nID#: HC2V1-GVH6J\nVACCINES: typhus, HPV, yellow fever, tuberculosis',
        'diplomatic_authorization': 'NAME: Frederikson, Paulina\nNATION: United Federation\nID#: HC2V1-GVH6J\nACCESS: Arstotzka, Impor'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: WQT4C-8NJYM\nNATION: Antegria\nNAME: Bennet, Ivana\nDOB: 1953.03.04\nSEX: F\nISS: Bostan\nEXP: 1983.11.25',
        'certificate_of_vaccination': 'NAME: Bennet, Ivana\nID#: WQT4C-8NJYM\nVACCINES: polio, hepatitis B',
        'access_permit': 'NAME: Bennet, Ivana\nNATION: Antegria\nID#: WQT4C-8NJYM\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 146cm\nWEIGHT: 91kg\nEXP: 1980.07.31'}
    assert inspector.inspect(person) == 'Entry denied: access permit expired.'

    person = {
        'passport': 'ID#: 18OM6-8DKLR\nNATION: United Federation\nNAME: Graham, Gabrielle\nDOB: 1961.07.08\nSEX: F\nISS: Haihan\nEXP: 1992.02.12',
        'certificate_of_vaccination': 'NAME: Graham, Gabrielle\nID#: 18OM6-8DKLR\nVACCINES: HPV, yellow fever, typhus, cholera',
        'access_permit': 'NAME: Graham, Gabrielle\nNATION: United Federation\nID#: 18OM6-8DKLR\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 164cm\nWEIGHT: 130kg\nEXP: 1988.06.09'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: LRB6C-39XKM\nNATION: Impor\nNAME: Wagner, Leonid\nDOB: 1965.10.11\nSEX: M\nISS: Vedor\nEXP: 1984.06.13',
        'certificate_of_vaccination': 'NAME: Wagner, Leonid\nID#: LRB6C-39XKM\nVACCINES: cowpox, typhus, tuberculosis, cholera',
        'diplomatic_authorization': 'NAME: Wagner, Leonid\nNATION: Impor\nID#: LRB6C-39XKM\nACCESS: Republia, Arstotzka, Antegria, Obristan'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 2DVFJ-XPLAN\nNATION: Impor\nNAME: Smirnov, Isaak\nDOB: 1964.05.15\nSEX: M\nISS: St. Marmero\nEXP: 1987.07.09',
        'certificate_of_vaccination': 'NAME: Smirnov, Isaak\nID#: 2DVFJ-XPLAN\nVACCINES: yellow fever, typhus, polio, HPV',
        'diplomatic_authorization': 'NAME: Smirnov, Isaak\nNATION: Impor\nID#: 2DVFJ-XPLAN\nACCESS: Obristan, Arstotzka, Republia'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: ZVXKF-4JROZ\nNATION: United Federation\nNAME: Fisk, Renee\nDOB: 1968.08.26\nSEX: F\nISS: Bostan\nEXP: 1985.10.31',
        'certificate_of_vaccination': 'NAME: Fisk, Renee\nID#: ZVXKF-4JROZ\nVACCINES: measles, cholera, HPV, typhus',
        'access_permit': 'NAME: Fisk, Renee\nNATION: United Federation\nID#: ZVXKF-4JROZ\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 195cm\nWEIGHT: 84kg\nEXP: 1991.03.03'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 71I68-DZH6B\nNATION: Impor\nNAME: Bullock, Maciej\nDOB: 1963.10.19\nSEX: M\nISS: Vedor\nEXP: 1988.07.25',
        'certificate_of_vaccination': 'NAME: Bullock, Maciej\nID#: 71I68-DZH6B\nVACCINES: rubella, tuberculosis, cowpox, typhus',
        'diplomatic_authorization': 'NAME: Bullock, Maciej\nNATION: Impor\nID#: 71I68-DZH6B\nACCESS: Arstotzka, Kolechia'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: DX8L9-BHIG3\nNATION: Antegria\nNAME: Mikkelson, Liliana\nDOB: 1964.11.23\nSEX: F\nISS: Haihan\nEXP: 1992.06.26',
        'certificate_of_vaccination': 'NAME: Mikkelson, Liliana\nID#: DX8L9-BHIG3\nVACCINES: HPV, tetanus, typhus, hepatitis B',
        'access_permit': 'NAME: Mikkelson, Liliana\nNATION: Antegria\nID#: DX8L9-BHIG3\nPURPOSE: VISIT\nDURATION: 1 MONTH\nHEIGHT: 195cm\nWEIGHT: 53kg\nEXP: 1984.01.15'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: IE79G-LYSOR\nNATION: Antegria\nNAME: Atreides, Aron\nDOB: 1966.10.23\nSEX: M\nISS: Orvech Vonor\nEXP: 1988.03.02',
        'certificate_of_vaccination': 'NAME: Atreides, Aron\nID#: IE79G-LYSOR\nVACCINES: typhus, HPV, tetanus, yellow fever',
        'access_permit': 'NAME: Atreides, Aron\nNATION: Antegria\nID#: IE79G-LYSOR\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 166cm\nWEIGHT: 76kg\nEXP: 1992.11.09'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: J49FD-B598K\nNATION: Republia\nNAME: Borshiki, Mohammed\nDOB: 1956.11.21\nSEX: M\nISS: Great Rapid\nEXP: 1993.04.04',
        'certificate_of_vaccination': 'NAME: Borshiki, Mohammed\nID#: J49FD-B598K\nVACCINES: typhus, tuberculosis, rubella, polio',
        'access_permit': 'NAME: Borshiki, Mohammed\nNATION: Republia\nID#: J49FD-B598K\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 156cm\nWEIGHT: 70kg\nEXP: 1987.12.01'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: Q3WHA-D4MER\nNATION: Republia\nNAME: Yankov, Sergey\nDOB: 1967.10.31\nSEX: M\nISS: Mergerous\nEXP: 1983.02.18',
        'certificate_of_vaccination': 'NAME: Yankov, Sergey\nID#: Q3WHA-D4MER\nVACCINES: tuberculosis, yellow fever, rubella',
        'access_permit': 'NAME: Yankov, Sergey\nNATION: Kolechia\nID#: Q3WHA-D4MER\nPURPOSE: WORK\nDURATION: 3 MONTHS\nHEIGHT: 203cm\nWEIGHT: 101kg\nEXP: 1990.02.20',
        'work_pass': 'NAME: Yankov, Sergey\nFIELD: Drafting\nEXP: 1982.11.14'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    bulletin = """Wanted by the State: Gregor Young"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: ZWRB4-DJLU0\nNATION: Arstotzka\nNAME: Shaw, Hayden\nDOB: 1961.08.17\nSEX: M\nISS: Paradizna\nEXP: 1982.03.06',
        'ID_card': 'NAME: Shaw, Hayden\nDOB: 1961.08.17\nHEIGHT: 161cm\nWEIGHT: 104kg'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: WJRTY-OX42D\nNATION: Kolechia\nNAME: Feyd, Alexa\nDOB: 1954.02.04\nSEX: F\nISS: Outer Grouse\nEXP: 1983.07.27',
        'grant_of_asylum': 'NAME: Feyd, Alexa\nNATION: Antegria\nID#: WJRTY-OX42D\nHEIGHT: 150cm\nWEIGHT: 44kg\nEXP: 1987.02.20'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: 3SUOJ-MK9S0\nNATION: Obristan\nNAME: Lima, Anton\nDOB: 1970.06.25\nSEX: M\nISS: Bostan\nEXP: 1990.11.28',
        'certificate_of_vaccination': 'NAME: Lima, Anton\nID#: 3SUOJ-MK9S0\nVACCINES: yellow fever, typhus, HPV, hepatitis B',
        'diplomatic_authorization': 'NAME: Lima, Anton\nNATION: Obristan\nID#: 3SUOJ-MK9S0\nACCESS: Arstotzka, United Federation, Impor, Kolechia'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 0OE15-QE28L\nNATION: Republia\nNAME: Ortiz, Khalid\nDOB: 1961.09.15\nSEX: M\nISS: Orvech Vonor\nEXP: 1991.04.05',
        'certificate_of_vaccination': 'NAME: Ortiz, Khalid\nID#: 0OE15-QE28L\nVACCINES: hepatitis B, rubella, polio',
        'access_permit': 'NAME: Ortiz, Khalid\nNATION: Kolechia\nID#: 0OE15-QE28L\nPURPOSE: WORK\nDURATION: 1 MONTH\nHEIGHT: 147cm\nWEIGHT: 60kg\nEXP: 1990.08.18'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: 13BFE-1QV8U\nNATION: Republia\nNAME: Shaw, Boris\nDOB: 1960.07.06\nSEX: M\nISS: Shingleton\nEXP: 1983.11.13',
        'certificate_of_vaccination': 'NAME: Shaw, Boris\nID#: 13BFE-1QV8U\nVACCINES: typhus, polio, yellow fever, HPV',
        'access_permit': 'NAME: Shaw, Boris\nNATION: Republia\nID#: 13BFE-1QV8U\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 166cm\nWEIGHT: 126kg\nEXP: 1991.02.17'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: E5HYA-2X0ZU\nNATION: Republia\nNAME: Kovacs, Ibrahim\nDOB: 1960.02.03\nSEX: M\nISS: East Grestin\nEXP: 1992.07.26',
        'certificate_of_vaccination': 'NAME: Kovacs, Ibrahim\nID#: E5HYA-2X0ZU\nVACCINES: typhus, cholera, cowpox, hepatitis B',
        'access_permit': 'NAME: Kovacs, Ibrahim\nNATION: Republia\nID#: E5HYA-2X0ZU\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 169cm\nWEIGHT: 88kg\nEXP: 1989.11.22'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: JDX7Q-6DUSP\nNATION: Obristan\nNAME: Vaughn, Alexa\nDOB: 1954.08.21\nSEX: F\nISS: Tsunkeido\nEXP: 1988.12.13',
        'certificate_of_vaccination': 'NAME: Vaughn, Alexa\nID#: JDX7Q-6DUSP\nVACCINES: cholera, hepatitis B',
        'access_permit': 'NAME: Vaughn, Alexa\nNATION: Kolechia\nID#: JDX7Q-6DUSP\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 179cm\nWEIGHT: 46kg\nEXP: 1986.02.06'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: MPF3A-74BWV\nNATION: Antegria\nNAME: Mateo, Naomi\nDOB: 1962.02.16\nSEX: F\nISS: Great Rapid\nEXP: 1990.06.14',
        'certificate_of_vaccination': 'NAME: Mateo, Naomi\nID#: AXU7F-XS13P\nVACCINES: tuberculosis, hepatitis B',
        'access_permit': 'NAME: Mateo, Naomi\nNATION: Antegria\nID#: MPF3A-74BWV\nPURPOSE: VISIT\nDURATION: 2 MONTHS\nHEIGHT: 205cm\nWEIGHT: 128kg\nEXP: 1981.08.10'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: LGMFJ-ZM7G2\nNATION: Republia\nNAME: Olah, Hubert\nDOB: 1957.09.11\nSEX: M\nISS: Skal\nEXP: 1988.04.29',
        'certificate_of_vaccination': 'NAME: Olah, Hubert\nID#: LGMFJ-ZM7G2\nVACCINES: typhus, measles, cowpox, polio',
        'grant_of_asylum': 'NAME: Olah, Hubert\nNATION: Republia\nID#: LGMFJ-ZM7G2\nHEIGHT: 149cm\nWEIGHT: 87kg\nEXP: 1989.02.06'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: LJ70Z-NE8T3\nNATION: Obristan\nNAME: Rasmussen, Eva\nDOB: 1963.12.31\nSEX: F\nISS: East Grestin\nEXP: 1985.04.25',
        'certificate_of_vaccination': 'NAME: Rasmussen, Eva\nID#: LJ70Z-NE8T3\nVACCINES: cholera, typhus, HPV, tetanus',
        'access_permit': 'NAME: Rasmussen, Eva\nNATION: Obristan\nID#: LJ70Z-NE8T3\nPURPOSE: WORK\nDURATION: 1 YEAR\nHEIGHT: 159cm\nWEIGHT: 129kg\nEXP: 1990.01.14',
        'work_pass': 'NAME: Rasmussen, Eva\nFIELD: Manufacturing\nEXP: 1985.12.04'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Deny citizens of Republia
Foreigners require yellow fever vaccination
Foreigners no longer require typhus vaccination
Wanted by the State: Alberta Murphy"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: X73GD-VIYG8\nNATION: Antegria\nNAME: Bosch, Antonia\nDOB: 1953.08.22\nSEX: F\nISS: Lorndaz\nEXP: 1980.11.30',
        'certificate_of_vaccination': 'NAME: Bosch, Antonia\nID#: X73GD-VIYG8\nVACCINES: HPV, tetanus, tuberculosis, yellow fever',
        'access_permit': 'NAME: Bosch, Antonia\nNATION: Antegria\nID#: X73GD-VIYG8\nPURPOSE: WORK\nDURATION: 1 YEAR\nHEIGHT: 156cm\nWEIGHT: 93kg\nEXP: 1987.07.02',
        'work_pass': 'NAME: Bosch, Antonia\nFIELD: Architecture\nEXP: 1986.07.03'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: TBJIW-XRBQD\nNATION: United Federation\nNAME: Lundberg, Ibrahim\nDOB: 1970.04.18\nSEX: M\nISS: Bostan\nEXP: 1980.11.30',
        'certificate_of_vaccination': 'NAME: Lundberg, Ibrahim\nID#: TBJIW-XRBQD\nVACCINES: yellow fever, HPV, cholera, tetanus',
        'diplomatic_authorization': 'NAME: Lundberg, Ibrahim\nNATION: United Federation\nID#: TBJIW-XRBQD\nACCESS: Arstotzka, Obristan, Impor'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: LGP98-19A8F\nNATION: Impor\nNAME: Levine, Petra\nDOB: 1953.02.24\nSEX: F\nISS: Haihan\nEXP: 1981.05.30',
        'certificate_of_vaccination': 'NAME: Levine, Petra\nID#: LGP98-19A8F\nVACCINES: yellow fever, typhus, measles, rubella',
        'access_permit': 'NAME: Levine, Petra\nNATION: Impor\nID#: LGP98-19A8F\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 197cm\nWEIGHT: 65kg\nEXP: 1985.03.23'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: EA7ZK-3IKP2\nNATION: Impor\nNAME: Fischer, Sharona\nDOB: 1967.08.04\nSEX: F\nISS: Shingleton\nEXP: 1983.12.16',
        'certificate_of_vaccination': 'NAME: Fischer, Sharona\nID#: EA7ZK-3IKP2\nVACCINES: HPV, typhus, yellow fever, tuberculosis',
        'grant_of_asylum': 'NAME: Fischer, Sharona\nNATION: Impor\nID#: EA7ZK-3IKP2\nHEIGHT: 200cm\nWEIGHT: 72kg\nEXP: 1987.06.27'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: EBN67-F9K5R\nNATION: Kolechia\nNAME: Dimitrov, Claude\nDOB: 1953.07.06\nSEX: M\nISS: Lesrenadi\nEXP: 1987.03.10',
        'certificate_of_vaccination': 'NAME: Dimitrov, Claude\nID#: EBN67-F9K5R\nVACCINES: HPV, hepatitis B, yellow fever, rubella',
        'access_permit': 'NAME: Dimitrov, Claude\nNATION: Kolechia\nID#: EBN67-F9K5R\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 201cm\nWEIGHT: 125kg\nEXP: 1987.07.11'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: JD4W3-TZ6RU\nNATION: Kolechia\nNAME: Sorenson, Kristen\nDOB: 1966.05.12\nSEX: F\nISS: Lesrenadi\nEXP: 1993.03.28',
        'certificate_of_vaccination': 'NAME: Sorenson, Kristen\nID#: JD4W3-TZ6RU\nVACCINES: cowpox, HPV, typhus, yellow fever',
        'access_permit': 'NAME: Sorenson, Kristen\nNATION: Kolechia\nID#: JD4W3-TZ6RU\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 179cm\nWEIGHT: 48kg\nEXP: 1989.08.08'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 5UZ30-V6Q2G\nNATION: Arstotzka\nNAME: Murphy, Alberta\nDOB: 1953.07.12\nSEX: M\nISS: Bostan\nEXP: 1986.07.13',
        'ID_card': 'NAME: Murphy, Alberta\nDOB: 1953.07.12\nHEIGHT: 159cm\nWEIGHT: 41kg'}
    assert inspector.inspect(person) == 'Detainment: Entrant is a wanted criminal.'

    person = {
        'passport': 'ID#: 9GUW1-YJFUG\nNATION: Obristan\nNAME: Romanoff, Nicolai\nDOB: 1964.12.21\nSEX: M\nISS: East Grestin\nEXP: 1983.10.06',
        'certificate_of_vaccination': 'NAME: Romanoff, Nicolai\nID#: 9GUW1-YJFUG\nVACCINES: tuberculosis, typhus',
        'grant_of_asylum': 'NAME: Romanoff, Nicolai\nNATION: United Federation\nID#: 9GUW1-YJFUG\nHEIGHT: 184cm\nWEIGHT: 51kg\nEXP: 1983.04.14'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'certificate_of_vaccination': 'NAME: Bergman, Rafal\nID#: 45Y2M-FAGRW\nVACCINES: rubella, hepatitis B, cowpox',
        'access_permit': 'NAME: Bergman, Rafal\nNATION: Impor\nID#: 45Y2M-FAGRW\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 209cm\nWEIGHT: 46kg\nEXP: 1982.06.16'}
    assert inspector.inspect(person) == 'Entry denied: access permit expired.'

    person = {
        'passport': 'ID#: ANQ9X-XGZC8\nNATION: Antegria\nNAME: Zitna, Pavel\nDOB: 1963.10.23\nSEX: M\nISS: Yurko City\nEXP: 1985.09.02',
        'certificate_of_vaccination': 'NAME: Zitna, Pavel\nID#: ANQ9X-XGZC8\nVACCINES: measles, cholera, yellow fever, HPV',
        'access_permit': 'NAME: Zitna, Pavel\nNATION: Antegria\nID#: ANQ9X-XGZC8\nPURPOSE: WORK\nDURATION: 1 YEAR\nHEIGHT: 190cm\nWEIGHT: 90kg\nEXP: 1989.09.16'}
    assert inspector.inspect(person) == 'Entry denied: missing required work pass.'

    person = {'certificate_of_vaccination': 'NAME: Schroder, Katrina\nID#: AG853-LWYFH\nVACCINES: rubella, polio',
              'access_permit': 'NAME: Schroder, Katrina\nNATION: Kolechia\nID#: N5MEW-0UWPX\nPURPOSE: WORK\nDURATION: 2 MONTHS\nHEIGHT: 168cm\nWEIGHT: 81kg\nEXP: 1987.02.22',
              'work_pass': 'NAME: Schroder, Katrina\nFIELD: Research\nEXP: 1982.10.28'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: 4LF5B-B9WUO\nNATION: Impor\nNAME: Michaelson, Petr\nDOB: 1950.12.04\nSEX: M\nISS: West Grestin\nEXP: 1993.03.05',
        'certificate_of_vaccination': 'NAME: Michaelson, Petr\nID#: 4LF5B-B9WUO\nVACCINES: rubella, yellow fever, tetanus, measles',
        'diplomatic_authorization': 'NAME: Michaelson, Petr\nNATION: Impor\nID#: 4LF5B-B9WUO\nACCESS: Kolechia, Arstotzka, Obristan'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: HS94B-O8BKN\nNATION: Antegria\nNAME: Lovska, Georgia\nDOB: 1966.09.10\nSEX: F\nISS: Great Rapid\nEXP: 1991.11.28',
        'certificate_of_vaccination': 'NAME: Lovska, Georgia\nID#: HS94B-O8BKN\nVACCINES: measles, hepatitis B',
        'access_permit': 'NAME: Lovska, Georgia\nNATION: Antegria\nID#: 24ZHU-UJR1V\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 169cm\nWEIGHT: 90kg\nEXP: 1992.02.23'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: 2NQTV-04Z8C\nNATION: Republia\nNAME: David, Sarah\nDOB: 1961.11.22\nSEX: F\nISS: Bostan\nEXP: 1986.12.30',
        'certificate_of_vaccination': 'NAME: David, Sarah\nID#: 2NQTV-04Z8C\nVACCINES: tetanus, HPV, cholera',
        'diplomatic_authorization': 'NAME: David, Sarah\nNATION: Republia\nID#: 2NQTV-04Z8C\nACCESS: United Federation, Kolechia, Obristan'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    bulletin = """Entrants require polio vaccination
Wanted by the State: Ava Kerr"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: FXO62-SJWXK\nNATION: Antegria\nNAME: Bennet, Stanislav\nDOB: 1957.08.16\nSEX: M\nISS: St. Marmero\nEXP: 1993.06.05',
        'certificate_of_vaccination': 'NAME: Bennet, Stanislav\nID#: FXO62-SJWXK\nVACCINES: tetanus',
        'access_permit': 'NAME: Bennet, Stanislav\nNATION: Republia\nID#: FXO62-SJWXK\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 203cm\nWEIGHT: 129kg\nEXP: 1986.05.29'}
    assert inspector.inspect(person) == 'Detainment: nationality mismatch.'

    person = {
        'passport': 'ID#: 609LC-MDKQC\nNATION: Republia\nNAME: Odom, Natalya\nDOB: 1965.04.21\nSEX: F\nISS: Great Rapid\nEXP: 1992.05.29',
        'certificate_of_vaccination': 'NAME: Odom, Natalya\nID#: 609LC-MDKQC\nVACCINES: rubella, polio, cholera, yellow fever',
        'diplomatic_authorization': 'NAME: Odom, Natalya\nNATION: Republia\nID#: 609LC-MDKQC\nACCESS: Obristan, Arstotzka, Impor'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: 4Z78O-58CNM\nNATION: Republia\nNAME: Aji, Wilma\nDOB: 1952.07.19\nSEX: F\nISS: True Glorian\nEXP: 1981.09.08',
        'certificate_of_vaccination': 'NAME: Aji, Wilma\nID#: 4Z78O-58CNM\nVACCINES: yellow fever, polio, measles, cholera',
        'diplomatic_authorization': 'NAME: Aji, Wilma\nNATION: Republia\nID#: 4Z78O-58CNM\nACCESS: Obristan, Impor, Antegria, Arstotzka, United Federation'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: 0L7A8-CQR4X\nNATION: Republia\nNAME: Hertzog, Anna\nDOB: 1959.12.29\nSEX: F\nISS: Korista City\nEXP: 1986.07.18',
        'certificate_of_vaccination': 'NAME: Hertzog, Anna\nID#: 0L7A8-CQR4X\nVACCINES: tuberculosis, polio, cowpox, yellow fever',
        'diplomatic_authorization': 'NAME: Hertzog, Anna\nNATION: Republia\nID#: 0L7A8-CQR4X\nACCESS: Impor, United Federation, Arstotzka'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: X2FAR-MOVAU\nNATION: Impor\nNAME: Zajak, Kascha\nDOB: 1952.04.25\nSEX: F\nISS: Haihan\nEXP: 1992.09.06',
        'certificate_of_vaccination': 'NAME: Zajak, Kascha\nID#: X2FAR-MOVAU\nVACCINES: cowpox, polio, HPV, yellow fever',
        'access_permit': 'NAME: Zajak, Kascha\nNATION: Impor\nID#: X2FAR-MOVAU\nPURPOSE: VISIT\nDURATION: 1 MONTH\nHEIGHT: 173cm\nWEIGHT: 47kg\nEXP: 1985.05.05'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 95167-KAVO9\nNATION: Impor\nNAME: Sousa, Joachim\nDOB: 1961.09.21\nSEX: M\nISS: Yurko City\nEXP: 1985.10.24',
        'certificate_of_vaccination': 'NAME: Sousa, Joachim\nID#: 95167-KAVO9\nVACCINES: tuberculosis, hepatitis B',
        'grant_of_asylum': 'NAME: Sousa, Joachim\nNATION: Impor\nID#: 8UCOM-6TI2C\nHEIGHT: 203cm\nWEIGHT: 92kg\nEXP: 1991.02.01'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: FG87Z-NQKHA\nNATION: Obristan\nNAME: Rasmussen, Omid\nDOB: 1957.05.01\nSEX: M\nISS: Enkyo\nEXP: 1987.02.04',
        'certificate_of_vaccination': 'NAME: Rasmussen, Omid\nID#: FG87Z-NQKHA\nVACCINES: polio, tuberculosis, HPV, yellow fever',
        'access_permit': 'NAME: Rasmussen, Omid\nNATION: Obristan\nID#: FG87Z-NQKHA\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 202cm\nWEIGHT: 78kg\nEXP: 1987.02.08'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: DRHS5-VRDPM\nNATION: Obristan\nNAME: Owsianka, Cesar\nDOB: 1967.05.12\nSEX: M\nISS: Tsunkeido\nEXP: 1989.12.22',
        'certificate_of_vaccination': 'NAME: Owsianka, Cesar\nID#: DRHS5-VRDPM\nVACCINES: polio, tetanus, yellow fever, HPV',
        'diplomatic_authorization': 'NAME: Owsianka, Cesar\nNATION: Obristan\nID#: DRHS5-VRDPM\nACCESS: United Federation, Impor, Kolechia, Antegria, Arstotzka'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: U23C5-A7DK9\nNATION: Arstotzka\nNAME: Schroder, Olga\nDOB: 1969.05.14\nSEX: F\nISS: Great Rapid\nEXP: 1993.01.13',
        'certificate_of_vaccination': 'NAME: Schroder, Olga\nID#: U23C5-A7DK9\nVACCINES: cholera, tetanus, hepatitis B',
        'ID_card': 'NAME: Schroder, Olga\nDOB: 1983.10.07\nHEIGHT: 163cm\nWEIGHT: 87kg'}
    assert inspector.inspect(person) == 'Detainment: date of birth mismatch.'

    person = {
        'passport': 'ID#: 6L3YT-LJ3RK\nNATION: Obristan\nNAME: Kowalska, Ivan\nDOB: 1962.02.03\nSEX: M\nISS: Skal\nEXP: 1988.08.03',
        'certificate_of_vaccination': 'NAME: Kowalska, Ivan\nID#: 6L3YT-LJ3RK\nVACCINES: cowpox, HPV, polio, yellow fever',
        'access_permit': 'NAME: Kowalska, Ivan\nNATION: Obristan\nID#: 6L3YT-LJ3RK\nPURPOSE: WORK\nDURATION: 6 MONTHS\nHEIGHT: 201cm\nWEIGHT: 81kg\nEXP: 1986.01.04',
        'work_pass': 'NAME: Kowalska, Ivan\nFIELD: Fishing\nEXP: 1993.01.08'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Wanted by the State: Nicole Chernovski"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: UI5PL-3UMAO\nNATION: Obristan\nNAME: Tjell, Damian\nDOB: 1962.12.09\nSEX: M\nISS: Vedor\nEXP: 1992.05.16',
        'certificate_of_vaccination': 'NAME: Tjell, Damian\nID#: UI5PL-3UMAO\nVACCINES: yellow fever, HPV, cholera, polio',
        'access_permit': 'NAME: Tjell, Damian\nNATION: Obristan\nID#: UI5PL-3UMAO\nPURPOSE: WORK\nDURATION: 1 MONTH\nHEIGHT: 189cm\nWEIGHT: 51kg\nEXP: 1993.09.03'}
    assert inspector.inspect(person) == 'Entry denied: missing required work pass.'

    person = {
        'passport': 'ID#: GE5BR-47YA2\nNATION: Arstotzka\nNAME: Hansson, Samantha\nDOB: 1959.02.09\nSEX: F\nISS: Shingleton\nEXP: 1984.01.22',
        'certificate_of_vaccination': 'NAME: Hansson, Samantha\nID#: GE5BR-47YA2\nVACCINES: tuberculosis, HPV, polio, hepatitis B',
        'ID_card': 'NAME: Hansson, Samantha\nDOB: 1959.02.09\nHEIGHT: 174cm\nWEIGHT: 77kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: EA9H8-7JAGX\nNATION: United Federation\nNAME: Vyas, Yulia\nDOB: 1966.10.09\nSEX: F\nISS: Paradizna\nEXP: 1988.08.17',
        'certificate_of_vaccination': 'NAME: Vyas, Yulia\nID#: EA9H8-7JAGX\nVACCINES: polio, yellow fever, HPV, hepatitis B',
        'diplomatic_authorization': 'NAME: Vyas, Yulia\nNATION: United Federation\nID#: EA9H8-7JAGX\nACCESS: Arstotzka, Antegria, Republia'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: EUO2L-NDG90\nNATION: United Federation\nNAME: Watson, Mikaela\nDOB: 1959.03.19\nSEX: F\nISS: Skal\nEXP: 1989.03.30',
        'certificate_of_vaccination': 'NAME: Watson, Mikaela\nID#: EUO2L-NDG90\nVACCINES: HPV, typhus, polio, yellow fever',
        'access_permit': 'NAME: Watson, Mikaela\nNATION: United Federation\nID#: EUO2L-NDG90\nPURPOSE: WORK\nDURATION: 2 MONTHS\nHEIGHT: 162cm\nWEIGHT: 46kg\nEXP: 1989.02.12'}
    assert inspector.inspect(person) == 'Entry denied: missing required work pass.'

    person = {
        'passport': 'ID#: ENLPI-NRWOX\nNATION: Impor\nNAME: Wolfe, Alexis\nDOB: 1954.03.08\nSEX: F\nISS: Enkyo\nEXP: 1986.01.15',
        'certificate_of_vaccination': 'NAME: Wolfe, Alexis\nID#: ENLPI-NRWOX\nVACCINES: tuberculosis, yellow fever, polio, hepatitis B',
        'access_permit': 'NAME: Wolfe, Alexis\nNATION: Impor\nID#: ENLPI-NRWOX\nPURPOSE: WORK\nDURATION: 6 MONTHS\nHEIGHT: 189cm\nWEIGHT: 84kg\nEXP: 1984.12.27'}
    assert inspector.inspect(person) == 'Entry denied: missing required work pass.'

    person = {
        'passport': 'ID#: XYHFR-LE6PG\nNATION: Obristan\nNAME: Roberts, Luis\nDOB: 1951.11.23\nSEX: M\nISS: Korista City\nEXP: 1983.09.04',
        'certificate_of_vaccination': 'NAME: Roberts, Luis\nID#: XYHFR-LE6PG\nVACCINES: polio, yellow fever, HPV, typhus',
        'access_permit': 'NAME: Roberts, Luis\nNATION: Obristan\nID#: XYHFR-LE6PG\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 149cm\nWEIGHT: 63kg\nEXP: 1983.08.21'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 1DKF0-F865I\nNATION: Republia\nNAME: Latva, Nikola\nDOB: 1959.03.01\nSEX: F\nISS: Mergerous\nEXP: 1988.03.30',
        'certificate_of_vaccination': 'NAME: Latva, Nikola\nID#: 1DKF0-F865I\nVACCINES: typhus, polio, yellow fever, cholera',
        'grant_of_asylum': 'NAME: Latva, Nikola\nNATION: Republia\nID#: 1DKF0-F865I\nHEIGHT: 146cm\nWEIGHT: 62kg\nEXP: 1983.08.03'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: Y9D2M-YD2CI\nNATION: Impor\nNAME: Kirsch, Cassandra\nDOB: 1969.01.30\nSEX: F\nISS: East Grestin\nEXP: 1989.04.27',
        'certificate_of_vaccination': 'NAME: Kirsch, Cassandra\nID#: Y9D2M-YD2CI\nVACCINES: measles, yellow fever, cowpox, polio',
        'access_permit': 'NAME: Kirsch, Cassandra\nNATION: Impor\nID#: Y9D2M-YD2CI\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 147cm\nWEIGHT: 60kg\nEXP: 1986.10.29'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: C60YK-J82B6\nNATION: Antegria\nNAME: Klass, Sophia\nDOB: 1961.12.24\nSEX: F\nISS: Glorian\nEXP: 1989.06.10',
        'certificate_of_vaccination': 'NAME: Klass, Sophia\nID#: C60YK-J82B6\nVACCINES: HPV, yellow fever, tuberculosis, polio',
        'access_permit': 'NAME: Klass, Sophia\nNATION: Antegria\nID#: C60YK-J82B6\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 165cm\nWEIGHT: 97kg\nEXP: 1986.07.30'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: S0Z6R-74DEH\nNATION: Republia\nNAME: Chernovski, Nicole\nDOB: 1958.12.20\nSEX: F\nISS: Great Rapid\nEXP: 1985.02.28',
        'diplomatic_authorization': 'NAME: Chernovski, Nicole\nNATION: Republia\nID#: S0Z6R-74DEH\nACCESS: United Federation, Kolechia, Antegria, Impor'}
    assert inspector.inspect(person) == 'Detainment: Entrant is a wanted criminal.'

    person = {
        'passport': 'ID#: T54P3-PMAYU\nNATION: Antegria\nNAME: Schumer, Felipe\nDOB: 1958.04.25\nSEX: M\nISS: Shingleton\nEXP: 1990.12.19',
        'certificate_of_vaccination': 'NAME: Schumer, Felipe\nID#: T54P3-PMAYU\nVACCINES: yellow fever, HPV, cowpox, polio',
        'access_permit': 'NAME: Schumer, Felipe\nNATION: Antegria\nID#: T54P3-PMAYU\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 195cm\nWEIGHT: 129kg\nEXP: 1991.07.14'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: C5HF3-8AF6I\nNATION: Republia\nNAME: Lewandowski, Ivanka\nDOB: 1969.04.22\nSEX: F\nISS: East Grestin\nEXP: 1983.07.23',
        'certificate_of_vaccination': 'NAME: Lewandowski, Ivanka\nID#: C5HF3-8AF6I\nVACCINES: cowpox, hepatitis B, polio, yellow fever',
        'access_permit': 'NAME: Lewandowski, Ivanka\nNATION: Republia\nID#: C5HF3-8AF6I\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 154cm\nWEIGHT: 104kg\nEXP: 1990.05.14'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: CRI25-USDEO\nNATION: Antegria\nNAME: Jager, Ivanka\nDOB: 1951.08.13\nSEX: F\nISS: Shingleton\nEXP: 1980.02.17',
        'certificate_of_vaccination': 'NAME: Jager, Ivanka\nID#: CRI25-USDEO\nVACCINES: cowpox, yellow fever, HPV, polio',
        'access_permit': 'NAME: Jager, Ivanka\nNATION: Antegria\nID#: CRI25-USDEO\nPURPOSE: WORK\nDURATION: 6 MONTHS\nHEIGHT: 147cm\nWEIGHT: 99kg\nEXP: 1993.06.01'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    bulletin = """Allow citizens of Republia
Citizens of Antegria, Obristan require measles vaccination
Citizens of Kolechia, United Federation, Obristan, Antegria no longer require HPV vaccination
Wanted by the State: Dimitry Bullock"""
    inspector.receive_bulletin(bulletin)

    person = {'certificate_of_vaccination': 'NAME: Xavier, Brenna\nID#: 9AWP3-EXZVP\nVACCINES: cowpox, rubella',
              'access_permit': 'NAME: Xavier, Brenna\nNATION: Antegria\nID#: 9AWP3-EXZVP\nPURPOSE: WORK\nDURATION: 3 MONTHS\nHEIGHT: 202cm\nWEIGHT: 79kg\nEXP: 1985.09.25',
              'work_pass': 'NAME: Xavier, Brenna\nFIELD: Food service\nEXP: 1982.06.01'}
    assert inspector.inspect(person) == 'Entry denied: work pass expired.'

    person = {
        'passport': 'ID#: J6DRM-D14MV\nNATION: United Federation\nNAME: Levine, Paulina\nDOB: 1957.03.28\nSEX: F\nISS: Outer Grouse\nEXP: 1986.02.26',
        'certificate_of_vaccination': 'NAME: Levine, Paulina\nID#: J6DRM-D14MV\nVACCINES: yellow fever, polio, tuberculosis, measles',
        'access_permit': 'NAME: Levine, Paulina\nNATION: United Federation\nID#: J6DRM-D14MV\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 152cm\nWEIGHT: 105kg\nEXP: 1985.10.11'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: QOPUI-FQSPH\nNATION: United Federation\nNAME: Klaus, James\nDOB: 1961.04.20\nSEX: M\nISS: Outer Grouse\nEXP: 1992.08.23',
        'certificate_of_vaccination': 'NAME: Klaus, James\nID#: QOPUI-FQSPH\nVACCINES: tetanus, rubella',
        'diplomatic_authorization': 'NAME: Klaus, James\nNATION: United Federation\nID#: QOPUI-FQSPH\nACCESS: Republia, Kolechia, Impor, Obristan'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    person = {
        'passport': 'ID#: INZTW-JWQME\nNATION: Obristan\nNAME: Carlstrom, Vilhelm\nDOB: 1969.11.24\nSEX: M\nISS: West Grestin\nEXP: 1992.10.10',
        'certificate_of_vaccination': 'NAME: Carlstrom, Vilhelm\nID#: INZTW-JWQME\nVACCINES: polio, measles, yellow fever, rubella',
        'access_permit': 'NAME: Carlstrom, Vilhelm\nNATION: Obristan\nID#: INZTW-JWQME\nPURPOSE: WORK\nDURATION: 3 MONTHS\nHEIGHT: 204cm\nWEIGHT: 97kg\nEXP: 1985.04.16',
        'work_pass': 'NAME: Carlstrom, Vilhelm\nFIELD: Agriculture\nEXP: 1983.11.20'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: PXK5J-GV54R\nNATION: Republia\nNAME: Schroder, Hugo\nDOB: 1954.12.21\nSEX: M\nISS: Bostan\nEXP: 1986.09.16',
        'certificate_of_vaccination': 'NAME: Schroder, Hugo\nID#: PXK5J-GV54R\nVACCINES: HPV, cholera',
        'grant_of_asylum': 'NAME: Schroder, Hugo\nNATION: Republia\nID#: X2L6A-Z4B8X\nHEIGHT: 210cm\nWEIGHT: 46kg\nEXP: 1987.05.05'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: DNA8Y-A0C8O\nNATION: Antegria\nNAME: Medici, Pablo\nDOB: 1967.01.06\nSEX: M\nISS: East Grestin\nEXP: 1990.11.26',
        'certificate_of_vaccination': 'NAME: Medici, Pablo\nID#: DNA8Y-A0C8O\nVACCINES: measles, yellow fever, rubella, polio',
        'access_permit': 'NAME: Medici, Pablo\nNATION: Antegria\nID#: DNA8Y-A0C8O\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 155cm\nWEIGHT: 92kg\nEXP: 1985.06.15'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: XGJSH-DP51X\nNATION: Republia\nNAME: Stoyakovich, Cecelia\nDOB: 1961.02.25\nSEX: F\nISS: Vedor\nEXP: 1985.12.17',
        'certificate_of_vaccination': 'NAME: Stoyakovich, Cecelia\nID#: XGJSH-DP51X\nVACCINES: tuberculosis, cowpox, polio, yellow fever',
        'access_permit': 'NAME: Stoyakovich, Cecelia\nNATION: Republia\nID#: XGJSH-DP51X\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 200cm\nWEIGHT: 73kg\nEXP: 1989.08.22'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 94FAV-95D8T\nNATION: Impor\nNAME: Lang, Cameron\nDOB: 1955.06.04\nSEX: F\nISS: Yurko City\nEXP: 1983.06.10',
        'certificate_of_vaccination': 'NAME: Lang, Cameron\nID#: 94FAV-95D8T\nVACCINES: yellow fever, typhus, polio, HPV',
        'diplomatic_authorization': 'NAME: Lang, Cameron\nNATION: Impor\nID#: 94FAV-95D8T\nACCESS: Antegria, Arstotzka, Obristan, Kolechia, Republia'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: KUZC5-PS7NM\nNATION: Arstotzka\nNAME: Bullock, Dimitry\nDOB: 1967.05.17\nSEX: M\nISS: Yurko City\nEXP: 1991.05.20',
        'certificate_of_vaccination': 'NAME: Bullock, Dimitry\nID#: KUZC5-PS7NM\nVACCINES: polio, rubella, tetanus, hepatitis B',
        'ID_card': 'NAME: Bullock, Dimitry\nDOB: 1967.05.17\nHEIGHT: 158cm\nWEIGHT: 81kg'}
    assert inspector.inspect(person) == 'Detainment: Entrant is a wanted criminal.'

    person = {
        'passport': 'ID#: 57VP0-BIN9K\nNATION: Obristan\nNAME: Steinberg, Jessica\nDOB: 1968.07.10\nSEX: F\nISS: West Grestin\nEXP: 1984.09.28',
        'certificate_of_vaccination': 'NAME: Steinberg, Jessica\nID#: 57VP0-BIN9K\nVACCINES: hepatitis B, yellow fever, polio, measles',
        'diplomatic_authorization': 'NAME: Steinberg, Jessica\nNATION: Obristan\nID#: 57VP0-BIN9K\nACCESS: Kolechia, Antegria, Arstotzka'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: HUK3V-7LAIN\nNATION: Republia\nNAME: Wolfe, Elena\nDOB: 1950.02.19\nSEX: F\nISS: Glorian\nEXP: 1993.05.11',
        'certificate_of_vaccination': 'NAME: Wolfe, Elena\nID#: HUK3V-7LAIN\nVACCINES: polio, cowpox, yellow fever, typhus',
        'access_permit': 'NAME: Wolfe, Elena\nNATION: Republia\nID#: HUK3V-7LAIN\nPURPOSE: VISIT\nDURATION: 2 MONTHS\nHEIGHT: 193cm\nWEIGHT: 64kg\nEXP: 1986.09.09'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Deny citizens of Impor, Obristan, United Federation, Republia, Antegria, Kolechia
Foreigners require tuberculosis vaccination
Wanted by the State: Erik Henriksson"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: 48MVR-6HP59\nNATION: Republia\nNAME: Zitna, Pablo\nDOB: 1966.03.29\nSEX: M\nISS: Great Rapid\nEXP: 1993.09.19',
        'certificate_of_vaccination': 'NAME: Zitna, Pablo\nID#: 48MVR-6HP59\nVACCINES: polio, tuberculosis, yellow fever, cowpox',
        'grant_of_asylum': 'NAME: Zitna, Pablo\nNATION: Republia\nID#: 48MVR-6HP59\nHEIGHT: 145cm\nWEIGHT: 62kg\nEXP: 1992.12.02'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: 4QO3H-RQEF6\nNATION: Obristan\nNAME: Hammerstein, Isaak\nDOB: 1961.11.12\nSEX: M\nISS: True Glorian\nEXP: 1987.09.03',
        'certificate_of_vaccination': 'NAME: Hammerstein, Isaak\nID#: 4QO3H-RQEF6\nVACCINES: polio, tuberculosis, measles, yellow fever',
        'grant_of_asylum': 'NAME: Hammerstein, Isaak\nNATION: Obristan\nID#: JQAW5-2UI6D\nHEIGHT: 152cm\nWEIGHT: 99kg\nEXP: 1987.07.11'}
    assert inspector.inspect(person) == 'Detainment: ID number mismatch.'

    person = {
        'passport': 'ID#: 7KONP-0S79C\nNATION: Republia\nNAME: Lovska, Misha\nDOB: 1966.08.31\nSEX: F\nISS: Lorndaz\nEXP: 1987.02.20',
        'certificate_of_vaccination': 'NAME: Lovska, Misha\nID#: 7KONP-0S79C\nVACCINES: cholera',
        'diplomatic_authorization': 'NAME: Lovska, Misha\nNATION: Republia\nID#: 7KONP-0S79C\nACCESS: Kolechia, Antegria, Impor'}
    assert inspector.inspect(person) == 'Entry denied: invalid diplomatic authorization.'

    person = {
        'passport': 'ID#: I6JWE-VXZ35\nNATION: Kolechia\nNAME: Jager, Zera\nDOB: 1951.02.01\nSEX: F\nISS: Shingleton\nEXP: 1990.01.22',
        'certificate_of_vaccination': 'NAME: Jager, Zera\nID#: I6JWE-VXZ35\nVACCINES: tetanus, polio, yellow fever, tuberculosis',
        'access_permit': 'NAME: Jager, Zera\nNATION: Kolechia\nID#: I6JWE-VXZ35\nPURPOSE: VISIT\nDURATION: 3 MONTHS\nHEIGHT: 167cm\nWEIGHT: 64kg\nEXP: 1993.05.20'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: K7GO1-BSCM2\nNATION: Antegria\nNAME: Costa, Dominik\nDOB: 1969.12.10\nSEX: M\nISS: East Grestin\nEXP: 1981.03.19',
        'certificate_of_vaccination': 'NAME: Costa, Dominik\nID#: K7GO1-BSCM2\nVACCINES: polio, measles, yellow fever, tuberculosis',
        'grant_of_asylum': 'NAME: Costa, Dominik\nNATION: Antegria\nID#: K7GO1-BSCM2\nHEIGHT: 209cm\nWEIGHT: 106kg\nEXP: 1987.05.10'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: IZONL-7S58T\nNATION: Obristan\nNAME: Steiner, Lukas\nDOB: 1957.05.20\nSEX: M\nISS: Lorndaz\nEXP: 1986.10.07',
        'certificate_of_vaccination': 'NAME: Steiner, Lukas\nID#: IZONL-7S58T\nVACCINES: yellow fever, measles, polio, tuberculosis',
        'access_permit': 'NAME: Steiner, Lukas\nNATION: Obristan\nID#: IZONL-7S58T\nPURPOSE: WORK\nDURATION: 6 MONTHS\nHEIGHT: 177cm\nWEIGHT: 66kg\nEXP: 1984.04.01'}
    assert inspector.inspect(person) == 'Entry denied: missing required work pass.'

    person = {
        'passport': 'ID#: 7DAK5-S0BVN\nNATION: Obristan\nNAME: Rabban, Cecelia\nDOB: 1954.04.21\nSEX: F\nISS: Orvech Vonor\nEXP: 1983.10.26',
        'certificate_of_vaccination': 'NAME: Rabban, Cecelia\nID#: 7DAK5-S0BVN\nVACCINES: polio, yellow fever, tuberculosis, measles',
        'diplomatic_authorization': 'NAME: Rabban, Cecelia\nNATION: Obristan\nID#: 7DAK5-S0BVN\nACCESS: Antegria, Arstotzka, Republia'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: BNK6I-4PNCW\nNATION: Antegria\nNAME: Lewandowski, Michael\nDOB: 1959.07.01\nSEX: M\nISS: Lesrenadi\nEXP: 1991.05.17',
        'certificate_of_vaccination': 'NAME: Lewandowski, Michael\nID#: BNK6I-4PNCW\nVACCINES: polio, yellow fever, tuberculosis, measles',
        'diplomatic_authorization': 'NAME: Lewandowski, Michael\nNATION: Antegria\nID#: BNK6I-4PNCW\nACCESS: Kolechia, Arstotzka'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: YUXM7-XCMN5\nNATION: Antegria\nNAME: Lundberg, Isabella\nDOB: 1967.01.30\nSEX: F\nISS: Outer Grouse\nEXP: 1984.02.01',
        'certificate_of_vaccination': 'NAME: Lundberg, Isabella\nID#: YUXM7-XCMN5\nVACCINES: measles, polio, tuberculosis, yellow fever',
        'grant_of_asylum': 'NAME: Lundberg, Isabella\nNATION: Antegria\nID#: YUXM7-XCMN5\nHEIGHT: 160cm\nWEIGHT: 89kg\nEXP: 1982.05.05'}
    assert inspector.inspect(person) == 'Entry denied: grant of asylum expired.'

    person = {
        'passport': 'ID#: GDQVP-H0YEL\nNATION: Arstotzka\nNAME: Kovacs, Michaela\nDOB: 1956.02.24\nSEX: F\nISS: Korista City\nEXP: 1988.03.20',
        'certificate_of_vaccination': 'NAME: Kovacs, Michaela\nID#: GDQVP-H0YEL\nVACCINES: cowpox, tuberculosis, HPV',
        'ID_card': 'NAME: Czekowicz, Anita\nDOB: 1956.02.24\nHEIGHT: 161cm\nWEIGHT: 73kg'}
    assert inspector.inspect(person) == 'Detainment: name mismatch.'

    person = {
        'passport': 'ID#: J48HC-K6G1B\nNATION: Arstotzka\nNAME: Wolfe, Felipe\nDOB: 1954.09.29\nSEX: M\nISS: Paradizna\nEXP: 1982.04.19',
        'certificate_of_vaccination': 'NAME: Wolfe, Felipe\nID#: J48HC-K6G1B\nVACCINES: cholera, HPV, measles, polio',
        'ID_card': 'NAME: Wolfe, Felipe\nDOB: 1954.09.29\nHEIGHT: 150cm\nWEIGHT: 91kg'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: N5DKJ-4N1PV\nNATION: Impor\nNAME: Crechiolo, Giovanni\nDOB: 1963.01.27\nSEX: M\nISS: Lesrenadi\nEXP: 1983.02.14',
        'certificate_of_vaccination': 'NAME: Crechiolo, Giovanni\nID#: N5DKJ-4N1PV\nVACCINES: typhus, tuberculosis, yellow fever, polio',
        'grant_of_asylum': 'NAME: Crechiolo, Giovanni\nNATION: Impor\nID#: N5DKJ-4N1PV\nHEIGHT: 205cm\nWEIGHT: 122kg\nEXP: 1983.05.27'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: RMA0V-OM8F6\nNATION: Arstotzka\nNAME: Medici, Dimitry\nDOB: 1970.05.14\nSEX: M\nISS: Tsunkeido\nEXP: 1993.03.18',
        'certificate_of_vaccination': 'NAME: Medici, Dimitry\nID#: RMA0V-OM8F6\nVACCINES: cholera, measles, tuberculosis, polio',
        'ID_card': 'NAME: Medici, Dimitry\nDOB: 1970.05.14\nHEIGHT: 197cm\nWEIGHT: 68kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    bulletin = """Allow citizens of Impor, Kolechia, United Federation
Foreigners no longer require yellow fever vaccination
Wanted by the State: Josefina Maars"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: 3MZQS-5A1ET\nNATION: Republia\nNAME: Baryshnikova, Nada\nDOB: 1951.02.28\nSEX: F\nISS: Tsunkeido\nEXP: 1993.04.05',
        'certificate_of_vaccination': 'NAME: Baryshnikova, Nada\nID#: 3MZQS-5A1ET\nVACCINES: tetanus, HPV, tuberculosis, polio',
        'access_permit': 'NAME: Baryshnikova, Nada\nNATION: Republia\nID#: 3MZQS-5A1ET\nPURPOSE: VISIT\nDURATION: 2 MONTHS\nHEIGHT: 175cm\nWEIGHT: 121kg\nEXP: 1992.01.25'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: QVP2J-M9VDE\nNATION: Antegria\nNAME: Romanowski, Amalie\nDOB: 1961.06.29\nSEX: F\nISS: St. Marmero\nEXP: 1981.07.21',
        'certificate_of_vaccination': 'NAME: Romanowski, Amalie\nID#: QVP2J-M9VDE\nVACCINES: polio, measles, yellow fever, tuberculosis',
        'access_permit': 'NAME: Romanowski, Amalie\nNATION: Antegria\nID#: QVP2J-M9VDE\nPURPOSE: VISIT\nDURATION: 2 MONTHS\nHEIGHT: 153cm\nWEIGHT: 130kg\nEXP: 1990.03.17'}
    assert inspector.inspect(person) == 'Entry denied: passport expired.'

    person = {
        'passport': 'ID#: DL1NA-7JFCV\nNATION: Obristan\nNAME: Owsianka, Anton\nDOB: 1968.06.08\nSEX: M\nISS: Yurko City\nEXP: 1992.05.07',
        'certificate_of_vaccination': 'NAME: Owsianka, Anton\nID#: DL1NA-7JFCV\nVACCINES: tetanus, measles, polio, tuberculosis',
        'access_permit': 'NAME: Owsianka, Anton\nNATION: Obristan\nID#: DL1NA-7JFCV\nPURPOSE: WORK\nDURATION: 6 MONTHS\nHEIGHT: 198cm\nWEIGHT: 69kg\nEXP: 1989.03.25'}
    assert inspector.inspect(person) == 'Entry denied: missing required work pass.'

    person = {
        'passport': 'ID#: Y7KQ0-KZ9WB\nNATION: Obristan\nNAME: Klass, Sharona\nDOB: 1955.02.09\nSEX: F\nISS: Bostan\nEXP: 1986.03.01',
        'certificate_of_vaccination': 'NAME: Klass, Sharona\nID#: Y7KQ0-KZ9WB\nVACCINES: measles, tuberculosis, polio, yellow fever',
        'access_permit': 'NAME: Klass, Sharona\nNATION: Obristan\nID#: Y7KQ0-KZ9WB\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 191cm\nWEIGHT: 67kg\nEXP: 1987.10.07'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: Q8LCK-G4WXV\nNATION: Obristan\nNAME: Maars, Josefina\nDOB: 1963.07.29\nSEX: F\nISS: Skal\nEXP: 1987.01.07',
        'certificate_of_vaccination': 'NAME: Maars, Josefina\nID#: Q8LCK-G4WXV\nVACCINES: yellow fever',
        'access_permit': 'NAME: Maars, Josefina\nNATION: Obristan\nID#: Q8LCK-G4WXV\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 203cm\nWEIGHT: 89kg\nEXP: 1981.01.06'}
    assert inspector.inspect(person) == 'Detainment: Entrant is a wanted criminal.'

    person = {
        'passport': 'ID#: LWUYD-SHYBM\nNATION: Obristan\nNAME: Watson, Sebastian\nDOB: 1967.03.31\nSEX: M\nISS: Tsunkeido\nEXP: 1987.09.25',
        'certificate_of_vaccination': 'NAME: Watson, Sebastian\nID#: LWUYD-SHYBM\nVACCINES: measles, hepatitis B, tuberculosis, polio',
        'access_permit': 'NAME: Watson, Sebastian\nNATION: Obristan\nID#: LWUYD-SHYBM\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 207cm\nWEIGHT: 57kg\nEXP: 1987.12.03'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: 4XNLS-P25GS\nNATION: United Federation\nNAME: Radic, Liliana\nDOB: 1956.03.01\nSEX: F\nISS: Skal\nEXP: 1984.01.22',
        'certificate_of_vaccination': 'NAME: Radic, Liliana\nID#: 4XNLS-P25GS\nVACCINES: polio, measles, tuberculosis, HPV',
        'access_permit': 'NAME: Radic, Liliana\nNATION: United Federation\nID#: 4XNLS-P25GS\nPURPOSE: TRANSIT\nDURATION: 2 DAYS\nHEIGHT: 208cm\nWEIGHT: 93kg\nEXP: 1983.11.06'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: 3R8UA-IY43R\nNATION: United Federation\nNAME: Bennet, Attila\nDOB: 1964.01.08\nSEX: M\nISS: East Grestin\nEXP: 1990.12.08',
        'certificate_of_vaccination': 'NAME: Bennet, Attila\nID#: 3R8UA-IY43R\nVACCINES: polio, measles, yellow fever, tuberculosis',
        'grant_of_asylum': 'NAME: Bennet, Attila\nNATION: United Federation\nID#: 3R8UA-IY43R\nHEIGHT: 185cm\nWEIGHT: 72kg\nEXP: 1992.10.15'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: I0N28-4SP13\nNATION: Arstotzka\nNAME: Jacobs, Matthew\nDOB: 1956.03.16\nSEX: M\nISS: Orvech Vonor\nEXP: 1986.11.23',
        'certificate_of_vaccination': 'NAME: Jacobs, Matthew\nID#: I0N28-4SP13\nVACCINES: typhus, measles, tuberculosis, polio',
        'ID_card': 'NAME: Jacobs, Matthew\nDOB: 1956.03.16\nHEIGHT: 187cm\nWEIGHT: 48kg'}
    assert inspector.inspect(person) == 'Glory to Arstotzka.'

    person = {
        'passport': 'ID#: W8DGT-KLD5N\nNATION: Kolechia\nNAME: Rabban, Elena\nDOB: 1953.05.17\nSEX: F\nISS: Tsunkeido\nEXP: 1986.11.17',
        'certificate_of_vaccination': 'NAME: Rabban, Elena\nID#: W8DGT-KLD5N\nVACCINES: typhus, polio, tuberculosis, yellow fever',
        'diplomatic_authorization': 'NAME: Rabban, Elena\nNATION: Kolechia\nID#: W8DGT-KLD5N\nACCESS: Obristan, Arstotzka'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: SD7KW-39MW7\nNATION: United Federation\nNAME: Costa, Attila\nDOB: 1968.05.21\nSEX: M\nISS: St. Marmero\nEXP: 1984.05.14',
        'certificate_of_vaccination': 'NAME: Costa, Attila\nID#: SD7KW-39MW7\nVACCINES: cholera, rubella, polio, tuberculosis',
        'grant_of_asylum': 'NAME: Costa, Attila\nNATION: United Federation\nID#: SD7KW-39MW7\nHEIGHT: 166cm\nWEIGHT: 56kg\nEXP: 1993.04.02'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    bulletin = """Allow citizens of Antegria
Citizens of Kolechia, Obristan, United Federation, Republia require HPV vaccination
Wanted by the State: Mikhail Schneider"""
    inspector.receive_bulletin(bulletin)

    person = {
        'passport': 'ID#: 36SZ4-EOLD0\nNATION: Obristan\nNAME: Klass, Vlad\nDOB: 1954.03.14\nSEX: M\nISS: West Grestin\nEXP: 1983.04.29',
        'certificate_of_vaccination': 'NAME: Klass, Vlad\nID#: 36SZ4-EOLD0\nVACCINES: HPV, measles, tuberculosis, polio',
        'access_permit': 'NAME: Klass, Vlad\nNATION: Obristan\nID#: 36SZ4-EOLD0\nPURPOSE: VISIT\nDURATION: 14 DAYS\nHEIGHT: 204cm\nWEIGHT: 102kg\nEXP: 1992.02.15'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: 6NUX3-VENWZ\nNATION: United Federation\nNAME: Lovska, Liliana\nDOB: 1959.09.07\nSEX: F\nISS: Shingleton\nEXP: 1987.04.17',
        'certificate_of_vaccination': 'NAME: Lovska, Liliana\nID#: 6NUX3-VENWZ\nVACCINES: tuberculosis, polio, typhus, HPV',
        'access_permit': 'NAME: Lovska, Liliana\nNATION: United Federation\nID#: 6NUX3-VENWZ\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 188cm\nWEIGHT: 62kg\nEXP: 1993.05.11'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: MAVPC-LAEK4\nNATION: United Federation\nNAME: Costanzo, Edine\nDOB: 1950.09.05\nSEX: F\nISS: Glorian\nEXP: 1985.06.17',
        'certificate_of_vaccination': 'NAME: Costanzo, Edine\nID#: MAVPC-LAEK4\nVACCINES: tuberculosis, cowpox, HPV, polio',
        'access_permit': 'NAME: Costanzo, Edine\nNATION: United Federation\nID#: MAVPC-LAEK4\nPURPOSE: WORK\nDURATION: 1 MONTH\nHEIGHT: 189cm\nWEIGHT: 78kg\nEXP: 1987.05.30',
        'work_pass': 'NAME: Costanzo, Edine\nFIELD: Accounting\nEXP: 1983.12.03'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: O9T5B-6IHNF\nNATION: Antegria\nNAME: Weisz, Lukas\nDOB: 1951.06.19\nSEX: M\nISS: Haihan\nEXP: 1992.03.08',
        'certificate_of_vaccination': 'NAME: Weisz, Lukas\nID#: O9T5B-6IHNF\nVACCINES: tuberculosis, cholera, measles, polio',
        'access_permit': 'NAME: Weisz, Lukas\nNATION: Antegria\nID#: O9T5B-6IHNF\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 194cm\nWEIGHT: 81kg\nEXP: 1991.01.31'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: QC7U9-Q5HW0\nNATION: Obristan\nNAME: Romanoff, Wilma\nDOB: 1959.07.02\nSEX: F\nISS: True Glorian\nEXP: 1992.06.11',
        'certificate_of_vaccination': 'NAME: Romanoff, Wilma\nID#: QC7U9-Q5HW0\nVACCINES: HPV, measles, polio, tuberculosis',
        'access_permit': 'NAME: Romanoff, Wilma\nNATION: Obristan\nID#: QC7U9-Q5HW0\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 182cm\nWEIGHT: 55kg\nEXP: 1987.04.07'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: JXV3Y-V3B64\nNATION: Impor\nNAME: Kaczynska, Cosmo\nDOB: 1960.10.09\nSEX: M\nISS: Skal\nEXP: 1992.09.22',
        'certificate_of_vaccination': 'NAME: Kaczynska, Cosmo\nID#: JXV3Y-V3B64\nVACCINES: tuberculosis, measles, polio, typhus',
        'grant_of_asylum': 'NAME: Kaczynska, Cosmo\nNATION: Impor\nID#: JXV3Y-V3B64\nHEIGHT: 201cm\nWEIGHT: 77kg\nEXP: 1988.08.04'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: WSBCT-SQDPR\nNATION: Obristan\nNAME: Peterson, Leonid\nDOB: 1951.02.22\nSEX: M\nISS: Great Rapid\nEXP: 1991.03.01',
        'certificate_of_vaccination': 'NAME: Peterson, Leonid\nID#: WSBCT-SQDPR\nVACCINES: measles, tuberculosis, polio, HPV',
        'access_permit': 'NAME: Peterson, Leonid\nNATION: Obristan\nID#: WSBCT-SQDPR\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 190cm\nWEIGHT: 70kg\nEXP: 1990.03.24'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: D6CX7-EU4LO\nNATION: Impor\nNAME: Michaelson, Ivana\nDOB: 1957.04.15\nSEX: F\nISS: Paradizna\nEXP: 1991.06.19',
        'certificate_of_vaccination': 'NAME: Michaelson, Ivana\nID#: D6CX7-EU4LO\nVACCINES: measles, rubella, polio, tuberculosis',
        'access_permit': 'NAME: Michaelson, Ivana\nNATION: Impor\nID#: D6CX7-EU4LO\nPURPOSE: VISIT\nDURATION: 2 MONTHS\nHEIGHT: 157cm\nWEIGHT: 74kg\nEXP: 1984.05.09'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: KRQSM-EJRYZ\nNATION: Antegria\nNAME: Maars, Julia\nDOB: 1966.12.08\nSEX: F\nISS: Vedor\nEXP: 1985.07.30',
        'certificate_of_vaccination': 'NAME: Maars, Julia\nID#: KRQSM-EJRYZ\nVACCINES: measles, tetanus, polio, tuberculosis',
        'access_permit': 'NAME: Maars, Julia\nNATION: Antegria\nID#: KRQSM-EJRYZ\nPURPOSE: IMMIGRATE\nDURATION: FOREVER\nHEIGHT: 150cm\nWEIGHT: 127kg\nEXP: 1987.04.16'}
    assert inspector.inspect(person) == 'Cause no trouble.'

    person = {
        'passport': 'ID#: PKTA6-X1WFR\nNATION: Republia\nNAME: Radic, Eleanor\nDOB: 1969.05.21\nSEX: F\nISS: Haihan\nEXP: 1991.12.17',
        'certificate_of_vaccination': 'NAME: Radic, Eleanor\nID#: PKTA6-X1WFR\nVACCINES: cholera, polio, tuberculosis, HPV',
        'grant_of_asylum': 'NAME: Radic, Eleanor\nNATION: Republia\nID#: PKTA6-X1WFR\nHEIGHT: 205cm\nWEIGHT: 118kg\nEXP: 1993.04.26'}
    assert inspector.inspect(person) == 'Entry denied: citizen of banned nation.'

    person = {
        'passport': 'ID#: EN8RF-HD3PV\nNATION: Arstotzka\nNAME: Lovska, Bernard\nDOB: 1963.10.23\nSEX: M\nISS: Haihan\nEXP: 1993.11.27',
        'certificate_of_vaccination': 'NAME: Lovska, Bernard\nID#: EN8RF-HD3PV\nVACCINES: tuberculosis, typhus, cowpox',
        'ID_card': 'NAME: Lovska, Bernard\nDOB: 1963.10.23\nHEIGHT: 208cm\nWEIGHT: 99kg'}
    assert inspector.inspect(person) == 'Entry denied: missing required vaccination.'

    person = {
        'passport': 'ID#: 8RTEL-HG7ZL\nNATION: United Federation\nNAME: Jensen, Alfred\nDOB: 1958.11.29\nSEX: M\nISS: Great Rapid\nEXP: 1992.09.13',
        'certificate_of_vaccination': 'NAME: Jensen, Alfred\nID#: 8RTEL-HG7ZL\nVACCINES: HPV, polio, cowpox, tuberculosis',
        'access_permit': 'NAME: Jensen, Alfred\nNATION: United Federation\nID#: 8RTEL-HG7ZL\nPURPOSE: TRANSIT\nDURATION: 14 DAYS\nHEIGHT: 146cm\nWEIGHT: 102kg\nEXP: 1989.11.22'}
    assert inspector.inspect(person) == 'Cause no trouble.'
