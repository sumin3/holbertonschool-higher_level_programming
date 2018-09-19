#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer that points to the address of the head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *cur = *head;
	int count = 0, tmp_count = 0, idx = 0, i, j, match = 0;
	char *buff = NULL;

	if (*head == NULL || head == NULL)
		return (1);
	while (tmp)
	{
		tmp = tmp->next;
		count++;
	}
	tmp_count = count;
	buff = malloc(sizeof(char) * count);
	while (tmp_count > 0)
	{
		buff[idx] = cur->n;
		cur = cur->next;
		tmp_count--;
		idx++;

	}
	for (i = 0, j = count - 1; i < count / 2; i++, j--)
	{
		if (buff[i] == buff[j])
			match = 1;
		else
		{
			match = 0;
			break;
		}
	}
	if (match == 1)
		return (1);
	else
		return (0);
}
