from django.test import TestCase

# Create your tests here.

l1=['a','b']
print(l1)
l2=['c']
l1.extend(l2)
l3=['d']
l1.extend(l3)
print(l1)

ls=['a','b']
ot=', '.join(ls)
print(ot)