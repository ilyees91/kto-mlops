from typing import List

def count_long_names(names: List[str], threshold: int = 7) -> int:
    """
    Retourne le nombre de chaînes dans `names` dont la longueur
    est strictement supérieure à `threshold`.
    """
    return sum(1 for name in names if len(name) > threshold)


if __name__ == "__main__":
    prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
    count = count_long_names(prenoms)
    print(f"Nombre de prénoms dont le nombre de lettres est supérieur à {7} : {count}")
