glossary = {
    'attribute' : 'A value associated with an object which is referenced by name using dotted expressions.',
    'dictionary' : 'An associative array, where arbitrary keys are mapped to values.',
    'parameter': 'A named entity in a function (or method) definition that specifies an argument that the function can accept',
    'slice' : 'An object usually containing a portion of a sequence',
    'class': 'A template for creating user-defined objects.',
    'argument' : 'A value passed to a function (or method) when calling the function.',
    'awaitable' : 'An object that can be used in an await expression. Can be a coroutine or an object with an __await__() method.',
    'coercion' : 'The implicit conversion of an instance of one type to another during an operation which involves two arguments of the same type.',
    'coroutine function' : 'A function which returns a coroutine object. A coroutine function may be defined with the async def statement, and may contain await, async for, and async with keywords. '
            }
for term,definition in glossary.items():
    print(term.title() + ':\n'
          + definition + '\n')