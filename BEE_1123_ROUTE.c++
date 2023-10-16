#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define inf 100000
#define maxsize 101010

int visited[maxsize];
int distance[maxsize];

typedef struct node{
    int no, value;
    struct node *next;
};

typedef struct graph{
    node *adj;
};

void dijkstra(graph *g, int s, int size){
    node *k;
    int i, j, v;

    for(i = 0;i < size;++i){
        distance[i] = inf;
    }

    memset(visited,false,sizeof(visited));

    distance[s] = 0;

    for(i = 0;i < size;++i){
        v = -1;

        for(j = 0;j<size;++j){
            if(!visited[j] && (v == -1||distance[j] < distance[v])){
                v = j;
            }
        }

        if(distance[v] == inf){
            break;
        }

        visited[v] = true;

        for(k = g->adj[v].next;k != NULL;k=k->next){
            int to = k->no;
            int len = k->value;

            if(distance[v] + len < distance[to]){
                distance[to] = distance[v] + len;
            }
        }

    }
}

graph * create_graph(int size){
    int i;
    graph *g = (graph *) malloc(sizeof(graph));
    g->adj = (node *) malloc(sizeof(node) * (size + 1));

    for (i = 0;i < size; ++i){
        g->adj[i].next = NULL;
    }

    return g;
}

node * create_node(int no,int value){
    node *newnode = (node *) malloc(sizeof(node));

    newnode->no = no;
    newnode->value = value;
    newnode->next = NULL;

    return newnode;
}

void p_back(graph *g,int no,int v,int value){
    node *newnode = create_node(no,value);
    newnode->next = g->adj[v].next;
    g->adj[v].next = newnode;
}

int main(int argc, char **argv){
    int i;
    int n, m, c, k, a, b, w;

    while(scanf("%d %d %d %d", &n, &m, &c, &k),(c && n && m && k)){
        graph *graph = create_graph(n + 1);
        for(i = 0;i<m;++i){
            scanf("%d %d %d", &a, &b, &w);

            if(a >= c && b >= c || ((a < c) && (b < c) && (abs(a-b)==1))){
                p_back(graph, a, b, w),p_back(graph, b, a, w);
            }

            if(a >= c && b < c){
                p_back(graph, b, a, w);
            }

            if(b >= c && a < c){
                p_back(graph, a, b, w);
            }
        }

        dijkstra(graph, k, n);
        printf("%d\n",distance[c - 1]);
    }
    return 0;
}