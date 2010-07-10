#!/bin/env python
k = 2

def emission(x, z, mu):
    return mu[z][x]

def forward(X, A, pi, mu):
    l = len(X)
    alpha = [pi]
    for x in X:
        alpha.append(
            [emission(x, j, mu) *
            sum(A[i][j]*alpha[-1][i]
            for i in range(k))
            for j in range(k)])
    return alpha

def backward(X, A, mu):
    beta = [[1] * k]
    for x in X:
        beta.append(
            [sum(A[j][i]*beta[-1][j]*emission(X[i], i, mu)
            for i in range(k))
            for j in range(k)])
    return beta

def baum_welch(X, A, pi, mu):
    alpha = forward(X, A, pi, mu)
    beta = backward(X, A, mu)
    return [[alpha[i][j]*beta[i][j]
        for j in range(k)]
        for i in range(len(X))]

def likelyhood(X, A, pi, mu):
    alpha = forward(X, A, pi, mu)
    return sum(alpha[-1])

def display(result):
    for i in range(len(result)):
        print i, ':', result[i]

if __name__ == '__main__':
    #reverse state always
    A = [[0, 1],[1, 0]]
    X = [0, 2, 0, 1, 0, 2]
    pi = [0.75, 0.25]
    mu = [[1, 0, 0],[0, 0.5, 0.5]]
    print "A:", A
    print "X:", X
    print "pi:", pi
    print "mu:", mu
    result = baum_welch(X, A, pi, mu)
    display(result)
    L = likelyhood(X, A, pi, mu)
    print "likelyhood:", L

