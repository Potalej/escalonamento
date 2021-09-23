# 📘 Escalonamento
📈 Pequena função que escalona matrizes.

O escalonamento é feito se utilizando como base a quantidade de zeros antes do primeiro elemento não nulo em cada linha da matriz, dividindo as linhas em listas com base nessa quantidade.

Tendo essa divisão, se verifica se alguma lista possui mais de um elemento. Em caso positivo, se encontra o coeficiente que permita uma linha eliminar a outra e novamente é feita a divisão, de modo seguido até que não haja mais nenhuma lista com mais de um elemento.

Por exemplo, no caso da seguinte matriz, apenas se passa a matriz como parâmetro:

```python
matriz = [
    [1, 0, -1, 2, 0],
    [2, 1, 3, 0, 0],
    [0, 1, -5, 4, 0],
    [1, 0, -11, 10, 0]
]
esq = escalonar(matriz)
```

O retornado contém, além da matriz escalonada, as operações realizadas:
```terminal
[ 1 0 -1 2 0 ]
[ 2 1 3 0 0 ]  
[ 0 1 -5 4 0 ] 
[ 0 0 -10 8 0 ]
L4 = L4-1*L1   

[ 1 0 -1 2 0 ] 
[ 0 1 -5 4 0 ] 
[ 0 0 -10 8 0 ]
[ 0 1 5 -4 0 ] 
L2 = L2-2*L1   

[ 1 0 -1 2 0 ]
[ 0 1 -5 4 0 ]
[ 0 0 -10 8 0 ]
[ 0 0 10 -8 0 ]
L4 = L4-1*L2

[ 1 0 -1 2 0 ]
[ 0 1 -5 4 0 ]
[ 0 0 -10 8 0 ]
[ 0 0 0 0 0 ]
L4 = L4+1*L3

[ 1 0 -1 2 0 ]
[ 0 1 -5 4 0 ]
[ 0 0 -10 8 0 ]
[ 0 0 0 0 0 ]
```
