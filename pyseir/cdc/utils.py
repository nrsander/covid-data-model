from enum import Enum

class Target(Enum):
    CUM_DEATH = 'cum death'
    INC_DEATH = 'inc death'
    CUM_HOSP = 'cum hosp'
    INC_HOSP = 'inc hosp'


class ForecastTimeUnit(Enum):
    DAY = 'day'
    WK = 'wk'

class ForecastAccuracy(Enum):
    NO_ADJUST = 'no_adjust'
    DEFAULT = 'default'

def target_column_name(num, target, time_unit):
    """

    """
    num = list(num)
    for n in num:
        yield f'{int(n)} {time_unit.value} ahead {target.value}'
