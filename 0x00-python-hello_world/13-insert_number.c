#include "lists.h"
#include <stdlib.h>
/**
  *insert_node - inserts a node in a sorted list
  *@head: head node of the list
  *@number: the number with which to form a new node
  *Return: the new node
  */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *ptr;

    ptr = *head;
    if (head == NULL || *head == NULL)
        return (add_nodeint_end(head, number));
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    new->n = number;
    new->next = NULL;
    if (number < ptr->n)
    {
        new->next = *head;
        *head = new;
        return (new);
    }
    while (ptr->next != NULL)
    {
        if (number < ptr->next->n)
        {
            new->next = ptr->next;
            ptr->next = new;
            return (new);
        }
        ptr = ptr->next;
    }
    free(new);
    return (add_nodeint_end(head, number));
}
