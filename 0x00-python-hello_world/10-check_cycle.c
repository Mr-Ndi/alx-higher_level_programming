#include "lists.h"

/*
 *This code implements the Floyd's Tortoise and Hare algorithm
 *which is used to detect cycles in a linked list
 */

/**
  *check_cycle - checks whether the linked list has a circle in it or not
  *@list: first node of the list
  *
  *Return: Integer (0 for no circle, 1 for circle found)
  */

int check_cycle(listint_t *list)
{
	listint_t *node1 = list;
	listint_t *node2 = list;

	while (node1 != NULL && node1->next != NULL)
	{
		node2 = node2->next;
		node1 = node1->next->next;
		if (node1 == node2)
			return (1);
	}
	return (0);
}
