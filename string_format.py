
# template
from string import Template
s = Template('$people $do $things')
s = s.substitute(people = 'Meng', do = 'likes', things = 'cooking')

print s



###########################################################
# substitution
# %s replace string
# %d replace number
# {} works for both and is consistent with C#


s2 = 'happy %s' %('birthday')
print s2

s3 = '#%d is going to be %s' % (1, 'Meng')
print s3

S = '{0} {1} {2}'.format('Meng', 'likes', 'cooking')
print s

