#include "lists.h"

/**
  *find_node - find the n(th) node in a list
  *@head: first node of the linked list
  *@n: the position of the node
  *Return: the address of node
  */

listint_t *find_node(listint_t **head, int n)
{
    listint_t *current;
    int i;
    
    current = *head;
    for(i = 1; i < n; i++)
    {
        current = current->next;
    }
    return (current);
}

/**
  *is_palindrome - checks if a linked list is a palindrome
  *@head: first node of the linked list
  *Return: 1 if palindrome and 0 if not
  */
int is_palindrome(listint_t **head)
{
    listint_t *ptr, *left_ptr, *right_ptr;
    int i = 0, nodes = 0, n, left, right;

    ptr = *head;
    while (ptr != NULL)
    {
        ptr = ptr->next;
        nodes++;
    }
    if (nodes % 2 == 0)
    {
        left = nodes/2;
        right = left + 1;
        n = left;
    }
    else
    {
        left = right = n = nodes/2 + 1;
    }

    for (i = 0; i < n; i++)
    {
        left_ptr = find_node(head, left);
        right_ptr = find_node(head, right);
        if (left_ptr->n != right_ptr->n)
            return (0);
        left--;
        right++;
    }
    return (1);
}
