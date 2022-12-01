# PyTemplatesForPython
## Install module
```bash
pip install pytemplatesforpython
```
## Create simple template
### Write some text:
```
Plain text
```
### Add some variable
```
Plain text written by {{insert(name)}}
```
### And more
```
Plain text is written by {{insert(author.name)}}
Some imformation about him:
He`s {{insert(author.age)}} years old, he lives in {{insert(author.city)}}
```
### You ask - what else can I do? I answer - all you can in the simple python!
#### Several nuances:
 - don`t allow symbols of a new line inside of the double braces ({{}})
 - you want to use for, while, if, etc? I am just going to show how to do it, now just remember: {{+}} to increase Tabs number, {{-}} to decrease it.
 - all of the expressions in double braces are connected, you can write {{a = 3}} first, and then {{insert(a)}}

```
Plain text is written by {{insert(author.name)}}
Several facts about him:
{{for i, fact in enumerate(author.facts):}}{{+}}
Факт №{insert(i)}: {{insert(fact)}}
{{-}}
```
### Can you see it now? Expressions those are between {{+}} and {{-}} will have a tab before them, just like
```python
for fact in author.facts:
  insert(i)
  insert(fact)
```
