#include <stdio.h>
int dfs(int v, int nv, int visited[], int matrix[nv][nv])
{
    int i;
    visited[v] = 1;
    for (i = 1; i <= nv; i++)
    {
        if (matrix[v][i] && !visited[i])
        {
            visited[i] = 1;
            dfs(i, nv, visited, matrix);
        }
    }
    return *visited;
}

int main()
{
    int flag;
    scanf("%d", &flag);

    // Number of vertex and edges
    int vertices, arestas;
    scanf("%d %d", &vertices, &arestas);

    // Initialization of matrix
    int i, j, matriz[vertices + 1][vertices + 1];
    for (i = 1; i <= vertices; i++)
    {
        for (j = 1; j <= vertices; j++)
        {
            matriz[i][j] = 0;
        }
    }

    // Filling of matrix
    int v1, v2, p;
    for (i = 0; i < arestas; i++)
    {
        scanf("%d %d %d", &v1, &v2, &p);
        matriz[v1][v2] = p;
    }

    // Initialization of array visitados
    int visitados[vertices];
    for (i = 1; i <= vertices; i++)
    {
        visitados[i] = 0;
    }

    // Call of DFS while vertex are not all visited
    int componentes = 0;
    for (i = 1; i <= vertices; i++)
    {
        if (visitados[i] == 0)
        {
            visitados = dfs(1, vertices, visitados, matriz);
            componentes = componentes + 1; // Count of calls of DFS
        }
    }

    // Print of number of connected components
    printf("%d", componentes);

    return 0;
}
