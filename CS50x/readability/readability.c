#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
//prototypes
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    //get the string
    string text = get_string("Text: ");
    //words
    int letters = count_letters(text);
    float words = count_words(text);
    int sentences = count_sentences(text);
    //calc l
    float l = (letters / words) * 100;
    //calc s
    float s = (sentences / words) * 100;
    //calc index
    float index = round((0.0588 * l) - (0.296 * s) - 15.8);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) index);
    }
}

//count sentences
int count_sentences(string text)
{
    int len = strlen(text);
    int sentences = 0;
    for (int i = 0 ; i < len ; i++)
    {
        //points for sentences
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }
    return sentences;
}
//count_words
int count_words(string text)
{
    int len = strlen(text);
    if (len == 0)
    {
        return 0;
    }
    else
    {
        int words = 1;
        for (int i = 0 ; i < len ; i++)
        {
            if (text[i] == 32)
            {
                words++;
            }
        }
        return words;
    }
}
//count letters
int count_letters(string text)
{
    int len = strlen(text);
    int letters = 0;
    for (int i = 0; i < len ; i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
    }
    return letters;
}