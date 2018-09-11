#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert a number to sorted linked list
 * @head: pointer point to the head of list
 * @number: number need to insert
 * Return: return a pointer of the list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new = NULL;
	listint_t *tmp = NULL;

	if (!(*head))
		return (NULL);
	while (current->next)
	{
		if (number < current->next->n)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			tmp = current->next;
			current->next = new;
			new->next = tmp;
			return (*head);
		}
		current = current->next;
	}
	add_nodeint_end(&current, number);
	return (*head);
}
