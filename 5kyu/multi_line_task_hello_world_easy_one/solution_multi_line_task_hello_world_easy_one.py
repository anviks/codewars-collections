"""https://www.codewars.com/kata/multi-line-task-hello-world-easy-one"""

# Given
t = type
k = lambda x: lambda _: x

# Solution
# @formatter:off
f\
=\
t(
''
,(
),
{
'\
_\
_\
n\
e\
w\
_\
_\
':
k(
'\
H\
e\
l\
l\
o\
,\
 \
w\
o\
r\
l\
d\
!'
)}
)
# @formatter:on

# Normalized: f=t('',(),{'__new__':k('Hello, world!')})
# Alternate:  f=t('',(),{'f':k('Hello, world!')})().f
