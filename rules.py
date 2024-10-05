from typing import Callable


def underpop_rule(cell: bool, neigh: int) -> bool:
    """Underpopulation rule"""
    if cell:  # if cell is alive
        if neigh < 2:  # and has fewer than two living neighbours
            return False  # then it dies
    return cell  # otherwise it remains as is


def reproduction_rule(cell: bool, neigh: int) -> bool:
    """Reproduction rule"""
    if not cell:  # if cell is not alive
        if neigh == 3:  # and has exactly three neighbours
            return True  # then it becomes alive
    return cell  # otherwise it remains as is


def overpop_rule(cell: bool, neigh: int) -> bool:
    """Overpopulation rule"""
    if cell:  # if cell is alive
        if neigh > 3:  # and has more than 3 neighbours
            return False  # then it dies
    return cell  # otherwise it remains as is


FULL_RULES: list[Callable] = [underpop_rule, overpop_rule, reproduction_rule]
