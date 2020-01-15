# PyMaths

### Kaprekar Constant

Kaprekar's routine is an iterative algorithm that, with each iteration, 
takes a natural number in a given number base, creates two new numbers 
by sorting the digits of its number by descending and ascending order, 
and subtracts the second from the first to yield the natural number for 
the next iteration.

##### Input: 5342

Num  | Max  | Min  | Subs
-----|------|------|-----
5342 | 5432 | 2345 | 3087
3087 | 8730 | 0378 | 8352
8352 | 8532 | 2358 | 6174
