"""
Regras do FizzBuzz:

1. Se a posição for múltipla de 3: 'Fizz'
2. Se a posição for múltipla de 5: 'Buzz'
3. Se a posição for múltipla de 3 e 5: 'FizzBuzz'
4. Para qualquer outra posição, passe o próprio número

"""
from functools import partial

multiplo = lambda base, num: num % base == 0
multiplo_3 = partial(multiplo, 3)
multiplo_5 = partial(multiplo, 5)


def robot(pos):
    say = str(pos)

    if multiplo_5(pos):
        say = 'Buzz'

    if multiplo_3(pos):
        say = 'Fizz'

    if multiplo_5(pos) and multiplo_3(pos):
        say = 'FizzBuzz'
    return say


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'Fizz'
    assert robot(6) == 'Fizz'
    assert robot(9) == 'Fizz'

    assert robot(5) == 'Buzz'
    assert robot(10) == 'Buzz'
    assert robot(20) == 'Buzz'

    assert robot(15) == 'FizzBuzz'
    assert robot(30) == 'FizzBuzz'
    assert robot(45) == 'FizzBuzz'
