#include "lists.h"
/**
 * check_cycle - check if the linked list has a cycle or not
 * @list: head of linked list
 * Return: return 1 if the list has a cycle, otherwise, return 0
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	while (tmp->next->next != NULL && list->next != NULL)
	{
		list = list->next;
		tmp = tmp->next;
		tmp = tmp->next;
		if (list == tmp)
			return (1);
	}
	return (0);
}
