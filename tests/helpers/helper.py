from functools import partial
from pytest_bdd import parsers

EXTRA_TYPES = {
    'num': int,
    'str': str,
}

parse_custom = partial(parsers.cfparse, extra_types=EXTRA_TYPES)