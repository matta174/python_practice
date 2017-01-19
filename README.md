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

The following code does a few things we've already covered. ```message_name.title()``` will make each word included in the variable uppercase. Displaying as follows:

>Matthew Compton

all ```\n``` does is create a new line. Given the name ``` name = 'matthew compton'``` there are several things we could do wit this data. ```print(name.upper())``` will give us 

>MATTHEW COMPTON

When we are given ```print(name.lower())``` we will get:

>matthew compton

This won't change simply because it was already lowercase but say we gave ``` name = 'MaTtHeW CoMpToN' ``` and then tried ```print(name.lower()) ``` we would receive:

>matthew compton

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


#### 2.8 Numbers




