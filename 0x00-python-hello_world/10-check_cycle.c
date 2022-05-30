#include "lists.h"

/**
 * check_cycle - Checks the cycle from  linkedlist
 * @list: input list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (list == NULL)
		return (0);

	temp = list->next;

	while (temp)
	{
		if (temp == list)
		{
			return (1);
		}
		temp = temp->next;
	}
	return (0);
}
