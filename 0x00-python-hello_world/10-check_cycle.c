#include "lists.h"
/**
 * check_cycle - check if the linked list has a cycle or not
 * @list: head of linked list
 * Return: return 1 if the list has a cycle, otherwise, return 0
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	tmp = tmp->next;
	while (tmp->next != NULL && list->next != NULL)
	{
		if (list == tmp)
			return (1);
		list = list->next;
		tmp = tmp->next;
		tmp = tmp->next;
	}
	return (0);
}
