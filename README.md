# boot-camp-12-day-3
Contains all the codes and their tests for third day bootcamp 12 Andelabs.

### 1.The HTML_AND_CSS_UI
This is a simple program that demonstrates ome basic HTML/CSS techniques:

**The basics**
> 1).How to reference a CSS file in a HTML script.

>2).How to create classe in CSS and using these classes in HTML scripts to determine the various properties and layout of content.

>3).How to reference images in a HTML script and using css classes to manipulate various image poperties.

>4).How to create child classes in CSS that inherit a few properties the parent classes and adding new properties to these child classes.

It is important to note that color properties in HTML/CSS can be manipulated eihter by the color names or Hex Codes. eg:RED and #FF0000 mean the same thing.

### 2.The Binary_Search
This code demonstrates a combination of both programming logic and Objet Oriented programming.

**The logic**

The code creates a list b, whose length is determined by another variable a.

A for loop is then used to populate this list for as long as the length is not exeeed.

A function is then used to define a way of camparing items using the binary search algorithm:

>The code starts by examining the middle item. If the item is not the desired item, then that is all, if not, then the ordered nature of the list(ordering is guaranteed from how the list is populated) is used to eliminate one half of the list as well as the middle item.The half to be eliminated is determined by: If the desired item is greater than the middle item of the list, then the lower half is eliminated, otherwise the upper half.
The process is repeated until the desired item is found.


### 3.The Missing_number
This program simply compares two lists and returns any item that is available in one list and not in the other.However, it is part of the logic to determine first if these lists contain anyy numbers before comparison can begin.
The tests in **missing_nuber_tests.py** can be used to understand how Test Driven Development is implemented.

