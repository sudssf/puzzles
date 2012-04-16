# coding=utf-8

'''
Problem 45
06 June 2003

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle        T_(n)=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Pentagonal 	  	P_(n)=n(3n−1)/2 	  1, 5, 12, 22, 35, ...
Hexagonal 	  	H_(n)=n(2n−1)       1, 6, 15, 28, 45, ...

It can be verified that T_(285) = P_(165) = H_(143) = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

hexagonal, pentagonal = {}, {}
for i in range(143+1, 10**5): hexagonal[i*(2*i-1)] = True
for i in range(165+1, 10**5): pentagonal[0.5*i*(3*i-1)] = True
print int(max([0.5*i*(i+1) for i in range(285+1, 10**5) if (0.5*i*(i+1) in hexagonal) and (0.5*i*(i+1) in pentagonal)]))