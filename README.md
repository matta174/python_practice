# Python Practice

## Repository for me to store my practice programs and coursework as I teach myself Python and work through Python Crash Course.


### Chapter 2

#### 2.1 Simple Message
The first "Hello World type program"

```python
message = "This is a simple message. Hurray!"
print(message)
```

This first program will print the message. `message = ` will set whatever string literal to the variable "message" which is then called by `print(message)` resulting in the following output:

>This is a simple message. Hurray!


#### 2.1 Simple Messages

This code shows a simple cocatenation of two separate messages I've made.
this time we have a `message` and a `message2` you can combine the outputs of these two separate variables by doing `print(message + message2)`

```python
#Simple hello message
message = "Oh Hello there!  "
print (message)
message2 = "This is concatenation"
print(message + message2)
```
The code above results in the following output:

>Oh Hello there! This is concatenation


#### 2.1 Personal Message

The following code does a few things we've already covered and a few new thins.

```python
message_name = "matthew compton"

message = "Hello " + message_name.title() + ". How are you doing today?\nWould you like to learn some Python?"
print(message)

second_name = "Jeremy Simpson"

# 2_4 Practice Famous Quote
print(second_name.upper())
print(second_name.lower())
print(second_name.title())

# 2_5 Practice
quote = 'Winson Churchill once said, "A joke is a very serious thing."\n'
print(quote)

# 2_6 Practice Famous Quote 2
famous_person = "winston churchill "
famous_quote = famous_person.title() + 'once said, "A joke is a very serious thing."\n'
print(famous_quote)
```



You may have noticed ```message_name.title()```  this will make each word included in the variable uppercase. Displaying as follows:

>Matthew Compton

all  ```\n```  does is create a new line. Given ``` name = 'matthew compton' ```  there are several things we could do wit this data.  ```print(name.upper())```  will give us 

>MATTHEW COMPTON

When we are given  ```print(name.lower())```  we will get:

>matthew compton

This won't change simply because it was already lowercase but say we gave  ``` name = 'MaTtHeW CoMpToN' ```  and then tried  ```print(name.lower()) ```  we would receive:

>matthew compton


#### 2.8 Numbers
##### Code:

```python
# The following file is meant to show how to work with various math functions in Python, as well as properly including numerical results in a string
print("5 + 3 = " + str(5+3))
print("4 * 2 = "+ str(4*2))
print("16 / 2 = "+str(16/2))
print("2^3 = "+ str(2**3))

favorite_number = 33
message= "My favorite number is: "+ str(favorite_number) + " pretty neat huh?"
print(message)
```

The above code shows how math functions work in python. The + and - signs work as you would expect however be careful as in most programming languages, Python included == actually means 'is equal to' when evaluating certain functions. You may have noticed another new thing showing up, ```print("5 + 3 = " + str(5+3)) ``` str tells python to print whatever is enveloped to print as a string rather than whatever other value.

### Chapter 3

#### 3.1 Working with Indexes
##### Code:

```python
friends = ['cody','josh','chase','preston']
print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())
```
The above code has our first example of an index in Python, you can declare an index by adding brackets []. 
For example: ``` my_index = [] ``` this will create an empty list. For the code above ``` print(friends[0].title()) ``` will output:

>Cody

Aside from ``` .title() ``` which we know how works ``` print(friends[0]) ``` will output whatever data is stored in the first location in the index. Which in Python starts at [0].

 
#### 3.2 Greetings
##### Code:

```python
friends = ['cody','josh','chase','preston']
print("Why hello there " + friends[0].title() + " how are you doing?")
print("Why hello there " + friends[1].title() + " how are you doing?")
print("Why hello there " + friends[2].title() + " how are you doing?")
print("Why hello there " + friends[3].title() + " how are you doing?")
```

This code is a slight modification of 3.1. The biggest difference is rather than ```print(friends[0].title())``` we have: ```print("Why hello there " +friends[0].title() + " how are you doing?")```. This just adds a simple greeting message to the above output resulting in:
>Why hello there Cody how are you doing?

I could add whatever message I wanted to this like perhapts I'd want to do. ```print(friends[0].title() + ' have you heard of Python before?'``` which would simply output:
>Cody have you heard of Python before?


#### 3.3 My Own List
##### Code:

```python
motorcycles = ['BMW','Honda','Harley Davidson','Ducati']
print(motorcycles)
message = "My favorite motorcycle is a "+motorcycles[0]
print(message)

print("I would like to own a "+motorcycles[1]+ " motorcycle.\n")

motorcycles.append('Yamaha')
print(motorcycles )

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[2]
print(motorcycles)

motorcycles = ['yamaha','honda','harley davidson','ducati']
last_motorcycle = motorcycles.pop()

print(motorcycles)
print("The last motorcycle I owned was a "+last_motorcycle.title())

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a '+ first_owned.title())

motorcycles = ['yamaha','honda','harley davidson','ducati']

waytooexpensive = 'ducati'
motorcycles.remove(waytooexpensive)
print(motorcycles)
print("\nA "+waytooexpensive.title() + " is too expensive for my tastes.")
```
Here I've done some stuff we already know and added a few things we don't yet. First I define my own list with ```motorcycles = ['BMW','Honda','Harley Davidson','Ducati']``` now say I wanted to add something to this list that I didn't have earlier. What I would do in this case is ```motorcycles.append('kawasaki')``` now when I try ```print(motorcycles)``` we would see:

>['BMW', 'Honda', 'Harley Davidson', 'Ducati', 'kawasaki']

append adds to the end of the list but what if I wanted to add an item at a particular spot. First let's delete the last item in that list with ```del motorcycles [4]``` which deletes the item at place 4 in the list (remember that lists begin at spot [0] in Python and most languages for that matter) let's now add Kawasaki to the center of the list. We can do this with ```motorcycles.insert(2,'Kawasaki')``` and when we print this we will see:

>['BMW', 'Honda', 'Kawasaki', 'Harley Davidson', 'Ducati']

#### 3.4 Guest List
##### Code:

```python
famous_guest_list = ['napoleon bonaparte','george orwell','alexander the great']

message= "Hello "+famous_guest_list[0].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[1].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[2].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
```

Here we create a list of famous people to be at my dinner party. We then print a message to invite them.

#### 3.5 Changing Guest List
##### Code:

```python
famous_guest_list = ['napoleon bonaparte','george orwell','alexander the great']

print("Oh no! it turns out "+famous_guest_list[0].title() + " won't be able to make it!\n")
famous_guest_list[0] = 'ronald reagan'

message= "Hello "+famous_guest_list[0].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[1].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[2].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
```

This code takes what we did in 3.4 with one exception. Napoleon wasn't able to make it, instead we changed the person who was going to attend out with Ronald reagan.

#### 3.6 More Guests
##### Code:

```python
famous_guest_list = ['napoleon bonaparte','george orwell','alexander the great']

print("Oh no! it turns out "+famous_guest_list[0].title() + " won't be able to make it!\n")
famous_guest_list[0] = 'ronald reagan'

message= "Hello "+famous_guest_list[0].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[1].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[2].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)

print('Hey everyone, luckily I was able to find a larger table to accommodate more people!\n')
famous_guest_list.insert(0,'franklin delano roosevelt')
famous_guest_list.insert(2,'john f kennedy')
famous_guest_list.append('thomas jefferson')

message= "Hello "+famous_guest_list[0].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[1].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[2].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[3].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[4].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
message= "Hello "+famous_guest_list[5].title() + " I'd like to have you as a guest at my dinner party!\n"
print(message)
```

Here we have the same code as 3.4 except we have added more guests inserting them at different places in the guest list. If we printed the guest list it would look like this:

>['franklin delano roosevelt', 'ronald reagan', 'john f kennedy', 'george orwell', 'alexander the great', 'thomas jefferson']

#### 3.7 Shrinking Guest List
##### Code:

```python
famous_guest_list = ['napoleon bonaparte','george orwell','alexander the great']
print("Oh no! it turns out "+famous_guest_list[0].title() + " won't be able to make it!\n")
famous_guest_list[0] = 'ronald reagan'
print('Hey everyone, luckily I was able to find a larger table to accomodate more people!\n')
famous_guest_list.insert(0,'franklin delano roosevelt')
famous_guest_list.insert(2,'john f kennedy')
famous_guest_list.append('thomas jefferson')
print("Unfortunately that table won't be able to arrive in time. Instead I only have space for two guests")



persontoleave = famous_guest_list.pop()
print('Sorry '+persontoleave.title()+" there just wasn't enough room for you. \n")
persontoleave = famous_guest_list.pop()
print('Sorry '+persontoleave.title()+" there just wasn't enough room for you. \n")
persontoleave = famous_guest_list.pop()
persontoleave = famous_guest_list.pop()
print('Sorry '+persontoleave.title()+" there just wasn't enough room for you. \n")

print("I'm happy to say that you "+famous_guest_list[0].title()+" are still invited!\n")
print("I'm happy to say that you "+famous_guest_list[1].title()+" are still invited!\n")

del famous_guest_list[0]
del famous_guest_list[0]
print(famous_guest_list)
```
 The above code if you've kept up with it will result in an empty guest list. the ```persontoleave = famous_guest_list.pop()``` line gets rid of the last item in the list, imagine the list as a stack and you are popping off the top.

#### 3.8 Seeing The World
##### Code:

```python
places_i_want_to_visit = ['taj mahal','the equator','moscow','australia','los angeles'] #declares the list initially
print(places_i_want_to_visit) #prints the data as is
```
Will output:
>['taj mahal', 'the equator', 'moscow', 'australia', 'los angeles']

```python
print(sorted(places_i_want_to_visit)) #temporarily sorts the data in the list alphabetically, leaving original data
```
Will output:
>['australia', 'los angeles', 'moscow', 'taj mahal', 'the equator']

However the sorted method only temporarily sorts alphabetically
```python
print(places_i_want_to_visit) #shows that the original list still exists
```

>['taj mahal', 'the equator', 'moscow', 'australia', 'los angeles']

```python
places_i_want_to_visit.reverse() #reverses the order of the list
print(places_i_want_to_visit) #prints reversed list
```
This will as expected reverse the list. Here's the output:
>['los angeles', 'australia', 'moscow', 'the equator', 'taj mahal']

```python
places_i_want_to_visit.reverse() #reverses again reverting it back to original list
print(places_i_want_to_visit) #prints newly returned original list
```
To revert back is easy. All that needs to be done is reverse again to get the original list.
>['taj mahal', 'the equator', 'moscow', 'australia', 'los angeles']

```python
places_i_want_to_visit.sort() #permanently sorts list alphabetically
print(places_i_want_to_visit) #prints new list
```
To permanently sort your list alphabetically you can use the sort() function. The above code results in this:
>['australia', 'los angeles', 'moscow', 'taj mahal', 'the equator']

**Be careful though you will __**NOT**__ be able to get the original order of this list after doing this!**

```python
places_i_want_to_visit.sort(reverse=True) #permanently reverses list alphabetically
print(places_i_want_to_visit) #prints new list
```
Finally if we want to sort in reverse alphabetical all we have to add in the function is sort(reverse=True)
Resulting in:
>['the equator', 'taj mahal', 'moscow', 'los angeles', 'australia']


The above code introduces various methods we can use to sort data in a list.
First we can temporarily sort data alphabetically using the sorted method in the example ```print(sorted(places_i_want_to_visit))``` I can temporarily sort the list alphabetically without
changing the original list order. If we want to reverse the list, say in a situation where you
want to show a list of newest to oldest items you could use ```places_i_want_to_visit.reverse()``` and it will reverse your list for you.

