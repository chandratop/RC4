# RC4

## Description

* Summer research on RC4 encryption algorithm.
* Under Prof. Subhamoy Maitra of ISI Kolkata

![alt text](https://www.isical.ac.in/~repro/wp-content/themes/isirepro/images/isi4_1.png "ISI Kolkata")

## Research Paper

This repository contains the code to test out the Theorems and
Corollaries of the research paper. To get access to the paper,
please [mail](mailto:chandratop.mail@gmail.com) me.

## Theorems & Corollaries

### Theorem 2

During RC4 PRGA, in 3 consecutive rounds (r, r +1 and r +2), j cannot take 3 consecutive
integer values. In other words, there is no r such that jr+2 = jr+1 + 1 = jr + 2.

### Theorem 3

In at most three consecutive rounds (r, r+1 and r+2), the value of j can
remain constant (jr = jr+1 = jr+2) or in other words there cannot exist
any r for which(jr = jr+1 = jr+2 = jr+3).

#### Corollary 3

If (jr = jr+1 = jr+2) then ir+2 = jr+2 and Sr+1[jr+1] = Sr+2[ir+2] = Sr+2[jr+2] = 0

#### Corollary 4

In two consecutive rounds (r and r+1), if the value of j remains
constant (i.e., jr = jr+1) then Sr+1[jr+1] must be 0.

#### Corollary 5

Once a value of j gets repeated in three consecutive rounds (r, r +1 and r +2),
no value can immediately be repeated in subsequent two rounds (for N > 2).
In other words, if jr = jr+1 = jr+2 it is not possible to have jr+3 = jr+4.

### Theorem 4

During RC4 PRGA, there cannot be a continuously decreasing sequence of
j of length more than 3 or in other words there cannot exist any r for which
(jr −jr+1) = (jr+1 −jr+2) = (jr+2 −jr+3) = k where (k < N −1).

#### Corollary 6

During RC4 PRGA, there cannot be a continuously increasing sequence of j
of length more than 3 or in other words there cannot exist any r for which
(jr+1 −jr) = (jr+2 −jr+1) = (jr+3 −jr+2) = k where (k > 1).
