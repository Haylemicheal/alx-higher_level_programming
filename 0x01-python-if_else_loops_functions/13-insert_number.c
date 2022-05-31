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
	if (*head == NULL || (*head)->n >= number)
	{
		temp->next = *head;
		*head = temp;
		return (*head);
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
