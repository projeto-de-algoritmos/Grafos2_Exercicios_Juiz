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