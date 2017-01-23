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
