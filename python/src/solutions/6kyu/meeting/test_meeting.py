"""https://www.codewars.com/kata/59df2f8f08c6cec835000012"""
import unittest

from solution_meeting import meeting


class FixedTests(unittest.TestCase):
    def do_testing(self, s, exp):
        ans = meeting(s)
        self.assertEqual(ans, exp)

    def test_solution(self):
        self.do_testing(
            "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn",
            "(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)")
        self.do_testing(
            "John:Gates;Michael:Wahl;Megan:Bell;Paul:Dorries;James:Dorny;Lewis:Steve;Alex:Meta;Elizabeth:Russel;Anna:Korn;Ann:Kern;Amber:Cornwell",
            "(BELL, MEGAN)(CORNWELL, AMBER)(DORNY, JAMES)(DORRIES, PAUL)(GATES, JOHN)(KERN, ANN)(KORN, ANNA)(META, ALEX)(RUSSEL, ELIZABETH)(STEVE, LEWIS)(WAHL, MICHAEL)")
        self.do_testing(
            "Alex:Arno;Alissa:Cornwell;Sarah:Bell;Andrew:Dorries;Ann:Kern;Haley:Arno;Paul:Dorny;Madison:Kern",
            "(ARNO, ALEX)(ARNO, HALEY)(BELL, SARAH)(CORNWELL, ALISSA)(DORNY, PAUL)(DORRIES, ANDREW)(KERN, ANN)(KERN, MADISON)")
        self.do_testing(
            "Anna:Wahl;Grace:Gates;James:Russell;Elizabeth:Rudd;Victoria:STAN;Jacob:Wahl;Alex:Wahl;Antony:Gates;Alissa:Meta;Megan:Bell;Amandy:Stan;Anna:Steve",
            "(BELL, MEGAN)(GATES, ANTONY)(GATES, GRACE)(META, ALISSA)(RUDD, ELIZABETH)(RUSSELL, JAMES)(STAN, AMANDY)(STAN, VICTORIA)(STEVE, ANNA)(WAHL, ALEX)(WAHL, ANNA)(WAHL, JACOB)")
        self.do_testing(
            "Ann:Russel;John:Gates;Paul:Wahl;Alex:Tolkien;Ann:Bell;Lewis:Kern;Sarah:Rudd;Sydney:Korn;Madison:Meta",
            "(BELL, ANN)(GATES, JOHN)(KERN, LEWIS)(KORN, SYDNEY)(META, MADISON)(RUDD, SARAH)(RUSSEL, ANN)(TOLKIEN, ALEX)(WAHL, PAUL)")
        self.do_testing(
            "Paul:Arno;Matthew:Schwarz;Amandy:Meta;Grace:Meta;Ann:Arno;Alex:Schwarz;Jacob:Rudd;Amber:Cornwell",
            "(ARNO, ANN)(ARNO, PAUL)(CORNWELL, AMBER)(META, AMANDY)(META, GRACE)(RUDD, JACOB)(SCHWARZ, ALEX)(SCHWARZ, MATTHEW)")
        self.do_testing(
            "Abba:Bell;Lewis:Cornwell;Jacob:STAN;Matthew:Schwarz;Ann:STAN;Sophia:Gates;Victoria:Korn;Anna:Bell;Paul:Kern;Alissa:Tolkien",
            "(BELL, ABBA)(BELL, ANNA)(CORNWELL, LEWIS)(GATES, SOPHIA)(KERN, PAUL)(KORN, VICTORIA)(SCHWARZ, MATTHEW)(STAN, ANN)(STAN, JACOB)(TOLKIEN, ALISSA)")
        self.do_testing(
            "Victoria:Thorensen;Ann:Arno;Alexis:Wahl;Emily:Stan;Anna:STAN;Jacob:Korn;Sophia:Gates;Amber:Kern",
            "(ARNO, ANN)(GATES, SOPHIA)(KERN, AMBER)(KORN, JACOB)(STAN, ANNA)(STAN, EMILY)(THORENSEN, VICTORIA)(WAHL, ALEXIS)")
        self.do_testing(
            "Andrew:Arno;Jacob:Russell;Anna:STAN;Antony:Gates;Amber:Korn;Lewis:Dorries;Ann:Burroughs;Alex:Kern;Anna:Arno;Elizabeth:Kern;John:Schwarz;Sarah:STAN",
            "(ARNO, ANDREW)(ARNO, ANNA)(BURROUGHS, ANN)(DORRIES, LEWIS)(GATES, ANTONY)(KERN, ALEX)(KERN, ELIZABETH)(KORN, AMBER)(RUSSELL, JACOB)(SCHWARZ, JOHN)(STAN, ANNA)(STAN, SARAH)")
        self.do_testing(
            "Megan:Wahl;Alexis:Arno;Alex:Wahl;Grace:STAN;Amber:Kern;Amandy:Schwarz;Alissa:Stan;Paul:Kern;Ann:Meta;Lewis:Burroughs;Andrew:Bell",
            "(ARNO, ALEXIS)(BELL, ANDREW)(BURROUGHS, LEWIS)(KERN, AMBER)(KERN, PAUL)(META, ANN)(SCHWARZ, AMANDY)(STAN, ALISSA)(STAN, GRACE)(WAHL, ALEX)(WAHL, MEGAN)")
