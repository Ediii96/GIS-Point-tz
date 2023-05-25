import re

paragraph = [
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
]


def word_frequency(param: list) -> dict:
    result = {}

    update_list = sum([re.sub(r'[^\w]', ' ', p.lower()).split(' ') for p in param], [])
    remove_none_el = [ul for ul in update_list if ul]
    for r in remove_none_el:
        result[r] = result.get(r, 0) + 1

    return result


print(word_frequency(paragraph))

