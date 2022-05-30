#include "lists.h"

/**
 * check_cycle - Checks the cycle from  linkedlist
 * @list: input list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *temp_next = list;

	while (temp && temp_next)
	{
		temp = temp->next;
		temp_next = temp_next->next->next;
		if (temp == temp_next)
		{
			return (1);
		}
	}
	return (0);
}
