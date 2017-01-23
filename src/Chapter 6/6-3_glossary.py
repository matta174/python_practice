#A python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.

glossary = {
    'attribute' : 'A value associated with an object which is referenced by name using dotted expressions.',
    'dictionary' : 'An associative array, where arbitrary keys are mapped to values.',
    'parameter': 'A named entity in a function (or method) definition that specifies an argument that the function can accept',
    'slice' : 'An object usually containing a portion of a sequence',
    'class': 'A template for creating user-defined objects.'
            }
print('Attribute:\n' + glossary['attribute']+'\n')
print('Dictionary:\n' + glossary['dictionary']+'\n')
print('Parameter:\n' + glossary['parameter']+'\n')
print('Slice:\n' + glossary['slice']+'\n')
print('Class:\n' + glossary['class']+'\n')