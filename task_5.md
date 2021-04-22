## Description

You've done an amazing job in the previous stage! Remember we mentioned retrieving large data? Let's improve your program by making it parse multiplewebsitepages. To make it even more useful, let's also implement the opportunity to parse several kinds of articles at once. 

## Objectives

1. Improve your code so that the function can take two parameters from the user input: the number of pages (an integer) and the type of articles (a string). The integer with the number of pages specifies the number of pages on which the program should look for the articles. 
2. Go back to the `https://www.nature.com/nature/articles` website and find out how to navigate between the pages with the `requests` module changing the URL.
3. Create a directory named `Page_N` (where *N* is the page number) for each page in the desired category, and put all the articles that are found on the page with the matched type to this directory.
4. Save the articles to separate `*.txt` files. Keep the same processing of the titles for the filenames as in the previous stage. You can give users some feedback on completion, but it is not required.

## Example

The program takes two input values from the user and then continues to process the Nature website data.

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

    > 4
    > Nature Briefing
    Saved all articles.
    

The main goal is to save the articles with the correct article bodies once the program has been executed.
