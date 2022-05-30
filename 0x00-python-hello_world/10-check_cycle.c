#include "lists.h"
/**
 * check_cycle - checs to see if there is a cycle in a linked list
 * @list: head node pointer
 *
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *pointer;

	if (list->next == NULL)
		return (0);
	pointer = list->next;
	while (pointer != NULL)
	{
		if (pointer == list)
			return (1);
		pointer = pointer->next;
	}
	return (0);
}
