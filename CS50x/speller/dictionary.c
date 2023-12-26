// Implements a dictionary's functionality
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"


// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

int count_words;
void insert_debut(node *table[], node *n);

void insert_debut(node *table[], node *n)
{
    unsigned int place = hash(n->word);
    if (place == -1)
    {
        return;
    }
    else
    {
        if (table[place] == NULL)
        {
            table[place] = n;
        }
        else
        {
            n->next = table[place]->next;
            table[place] = n;
        }
    }
}
// TODO: Choose number of buckets in hash table
const unsigned int N = 27;

// Hash table
node *table[N];


// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int len = strlen(word);
    char word_copy[len + 1];
    word_copy[len] = '\0';
    for (int i = 0; i < len; i++)
    {
        word_copy[i] = tolower(word[i]);
    }
    int hashcode = hash(word_copy);
    node *tmp = table[hashcode];
    if (tmp == NULL)
    {
        return false;
    }
    while (tmp != NULL)
    {
        if (strcasecmp(tmp->word, word_copy) == 0)
        {
            return true;
        }
        tmp = tmp->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    if (isalpha(word[0]))
    {
        return toupper(word[0]) - 65;
    }
    else
    {
        return 26;
    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *input = fopen(dictionary, "r");
    if (input == NULL)
    {
        fclose(input);
        return false;
    }
    char buff[LENGTH + 1];
    while (fscanf(input, "%s", buff) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(input);
            return false;
        }
        else
        {
            count_words++;
            strcpy(n->word, buff);
            n->next = NULL;
            insert_debut(table, n);
        }
    }
    fclose(input);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++) // loop all the arrays
    {
        node *tmp1 = table[i];
        while (tmp1 != NULL)
        {
            node *tmp2 = tmp1;
            tmp1 = tmp1 -> next;
            free(tmp2);
        }
    }
    return true;
}
