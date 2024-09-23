#In this file, which actually works, we will investigate the evenness of the grou of points on different elliptic curves.
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import itertools as it
import argparse
 
x, y = sp.symbols('x y')

#Returns whether an elliptic curve y^2 = x^3 + Ax + B over f_q is even or odd, for q a prime
def is_even(A, B, q) -> bool:
    F = sp.FiniteField(q)
    y2 = sp.poly(x**3 + A*x + B, domain = F)
    field_poly = x**q - x
    gcd = sp.gcd(y2, field_poly, domain=F)
    if (gcd == 1):
        return False
    else:
        return True
    

def is_even_plotter(a_range, b_range, q_range):
    num_even = 0
    total = 0
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    A_values = np.arange(1, a_range, 1) 
    B_values = np.arange(1, b_range, 1) 
    q_values = sp.primerange(1, q_range)
    pairs = it.product(A_values, B_values, q_values)
    for pair in pairs:
        total += 1
        A = pair[0]
        B = pair[1]
        q = pair[2]
        if is_even(A, B, q):
            ax.scatter(A, B, q, color='red')
            num_even += 1
        else:
            ax.scatter(A, B, q, color='blue')
    ax.set_xlabel('A')
    ax.set_ylabel('B')
    ax.set_zlabel('q')
    prop_even = num_even / total
    ax.text2D(0.05, 0.95, f'Proportion Even: {prop_even}', transform=ax.transAxes)
    ax.legend(['Even', 'Odd'])
    plt.show()

def proportion_even(a_list, b_list, q_list):
    num_even = 0
    total = 0
    for A in a_list:
        for B in b_list:
            for q in q_list:
                total+=1
                if is_even(A, B, q):
                    num_even += 1
    return num_even / total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Even Elliptic Curves',
                    description='Determine the proportion of elliptic curves over finite field of different sizes that have an even number of points.')
    parser.add_argument('a_range', type=int, help='The range of A values to consider')
    parser.add_argument('b_range', type=int, help='The range of B values to consider')
    parser.add_argument('q_range', type=int, help='The upper bound on prime values for finite field to consider')
    args = parser.parse_args()
    print(proportion_even(np.arange(1, args.a_range), np.arange(1, args.b_range), sp.primerange(1, args.q_range)))
    is_even_plotter(10, 10, 20)
