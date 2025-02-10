import unittest
from typing import List

def count_names_with_more_than_seven_letters(names: List[str]) -> int:
    """
    Compte le nombre de prénoms dont le nombre de lettres est strictement supérieur à 7.

    :param names: Liste de prénoms.
    :return: Nombre de prénoms comportant plus de 7 lettres.
    """
    count = 0
    for name in names:
        name_length = len(name)
        status = "supérieur" if name_length > 7 else "inférieur ou égal"
        print(f"{name} est un prénom avec un nombre de lettres {status} à 7")
        if name_length > 7:
            count += 1
    return count

class TestCountNamesWithMoreThanSevenLetters(unittest.TestCase):
    def test_count_names_with_more_than_seven_letters(self):
        names_list = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_names_with_more_than_seven_letters(names_list)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
