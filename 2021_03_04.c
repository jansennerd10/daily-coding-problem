/*
 * This problem was asked by Google.
 *
 * An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
 *
 * If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
 */

/*
 * This linked list implementation uses the object-oriented style for simplicity,
 * heap-allocating a container struct for every element of the list, which
 * contains a pointer to the payload.
 * 
 * Performance-optized linked list implementations that appear in kernel code
 * often invert this approach: they provide a linked list struct designed to
 * be included as a member of the payload type, so that space for the pointers
 * is allocated with the payload, which need not be on the heap. The internal
 * structs are then pointed to each other, and the payload elements extracted
 * with the use of clever macros to calculate the offset of the linked list
 * struct within the larger payload struct. The tradeoff is that such
 * implementations are somewhat more complex to write, and require that the
 * implementation of a struct that will be stored in the linked list be tightly
 * coupled to the implementation of that list.
 */

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

struct node {
    /* This field is declared as uintptr_t because it is not directly a pointer
     * to anything and must not be dereferenced, but needs to be of an integer
     * type compatible with pointers on the current platform. */
    uintptr_t pointers;
    void * payload;
};

struct node *first = NULL, *last = NULL;

void add(void * payload) {
    struct node *new = (struct node *)malloc(sizeof(struct node));
    /* This XOR operation may appear to do nothing; however, the C standard
     * technically allows NULL to be a value other than 0. */
    new->pointers = (uintptr_t)last ^ (uintptr_t)NULL;
    new->payload = payload;

    if(last == NULL) {
        first = new;
        last = new;
    }
    else {
        last->pointers = last->pointers ^ (uintptr_t)NULL ^ (uintptr_t)new;
        last = new;
    }
}

void * get(int index) {
    struct node * current = first;
    struct node * previous = NULL;
    struct node * next = NULL;

    for(int i = 0; i < index; i++) {
        if(current == NULL) {
            /* As is common in C, there's no way to tell whether NULL was
             * returned because the index didn't exist (as here) or because
             * NULL was stored as the payload.
             * 
             * An idiomatic implementation would either return success/failure
             * and return the payload via a void ** parameter, or require the
             * caller to check the error level whenever NULL is returned. */
            return NULL;
        }
        next = (struct node *)(current->pointers ^ (uintptr_t)previous);
        previous = current;
        current = next;
    }

    return current == NULL ? NULL : current->payload;
}

void print_retrieve(int index) {
    int * payload = (int *)get(index);
    if(payload == NULL) {
        printf("Retrieved NULL from index [%d]\n", index);
    }
    else {
        printf("Retrieved value %d from index [%d]\n", *payload, index);
    }
}

int main() {
    int a = 100, b = 200, c = 300;

    add(&a);
    printf("Stored value %d to index [0]\n", a);
    print_retrieve(0);
    print_retrieve(1);

    add(&b);
    printf("Stored value %d to index [1]\n", b);
    add(&c);
    printf("Stored value %d to index[2]\n", c);
    print_retrieve(0);
    print_retrieve(1);
    print_retrieve(2);
    print_retrieve(3);
}
