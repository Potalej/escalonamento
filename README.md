# 📘 Escalonamento
📈 Pequena função que escalona matrizes.

O escalonamento é feito se utilizando como base a quantidade de zeros antes do primeiro elemento não nulo em cada linha da matriz, dividindo as linhas em listas com base nessa quantidade.

Tendo essa divisão, se verifica se alguma lista possui mais de um elemento. Em caso positivo, se encontra o coeficiente que permita uma linha eliminar a outra e novamente é feita a divisão, de modo seguido até que não haja mais nenhuma lista com mais de um elemento.

Por exemplo, no caso da seguinte matriz, apenas se passa a matriz como parâmetro:

```python
matriz = [
  [2, 1, -2],
  [3, 2, 2],
  [5, 4, 3]
]
esq = escalonar(matriz)
```

O retornado contém, além da matriz escalonada, as operações realizadas:
```terminal
L3 = L3-5/2*L1
L2 = L2-3/2*L1
L2 = L2-1/3*L1
[ 2 1 -2 ]
[ 0 3/2 8 ]
[ 0 0 7/3 ]
```
