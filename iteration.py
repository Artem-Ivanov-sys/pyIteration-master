"""Just function. Look README.md"""

import math


def sin_(argument: float) -> float:
    """Function"""

    answer = 0
    for i in range(10):
        answer += (-1)**i*argument**(2*i+1)/math.factorial(2*i+1)
    return answer


if __name__ == '__main__':
    print(sin_(math.pi/6))
