from typing import Any, Callable, Dict, List
from functools import cmp_to_key


def sort_dict_collection_by_value(dict_collection: List[Dict[str, Any]], comparator: Callable[[Any, Any], int]) -> List[Dict[str, Any]]:
    return sorted(dict_collection, key = cmp_to_key(comparator))