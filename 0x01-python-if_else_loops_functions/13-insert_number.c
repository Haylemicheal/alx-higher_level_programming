#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a node
 * @head: Head list
 * @number: Number to be inserted
 * Return: The new node or Null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list = (listint_t *)malloc(sizeof(listint_t));
	listint_t *temp = (listint_t *)malloc(sizeof(listint_t));

	list = *head;
	temp->n = number;
	if (list == NULL)
	{
		list->n = number;
		return (list);
	}
	else if (list->n >= number)
	{
		temp->n = number;
		temp->next = list;
		return (temp);
	}
	else
	{
		while (list->next)
		{
			if (list->next->n > number)
			{
				temp->n = number;
				temp->next = list->next;
				list->next = temp;
				return (*head);
			}
			list = list->next;
		}
	}
	list->next = temp;
	return (list);
}
