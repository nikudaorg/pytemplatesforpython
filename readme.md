# PyTemplatesForPython Quick Start (Beta)

## 📦 Installation

```bash
pip install pytemplatesforpython
```

---

## ✨ Creating a Simple Template

Start with basic text:

```
Plain text
```

Add a variable:

```
Plain text written by {{ insert(name) }}
```

Use an object:

```
Plain text is written by {{ insert(author.name) }}
Some information about him:
He’s {{ insert(author.age) }} years old, he lives in {{ insert(author.city) }}
```

Wondering what else you can do?  
The answer is: *pretty much anything you can do in plain Python!*

---

### ⚠️ A Few Notes

- Avoid using newline characters inside `{{ ... }}`.
- Want control structures like `for`, `while`, `if`, etc.?  
  Use `{{+}}` to increase indentation and `{{-}}` to decrease it.
- Expressions inside double braces can be sequential:  
  First `{{ a = 3 }}`, then `{{ insert(a) }}`.

Example:

```
Plain text is written by {{ insert(author.name) }}
Several facts about him:
{{ for i, fact in enumerate(author.facts): }}{{+}}
Fact №{{ insert(i) }}: {{ insert(fact) }}
{{-}}
```

Which will be rendered with indentation similar to:

```python
for i, fact in enumerate(author.facts):
  insert(i)
  insert(fact)
```

---

## 📌 Working with Context

By default, all expressions reference a single `context` parameter.  
To improve clarity, you can unpack it:

```
{{ man: Creature = context["man"] }}
{{ monkey: Creature = context["monkey"] }}

Man loves {{ insert(man.loves) }} and monkey loves {{ insert(monkey.loves) }}.
Man lives in {{ insert(man.lives_in) }}, monkey lives in {{ insert(monkey.lives_in) }}.
```

---

## 🌐 HTML Templates Example

Most common use case is rendering HTML:

```html
<!DOCTYPE html>
{{ author = context["author"] }}
<html>
<body>
  <p>Plain text is written by {{ insert(author.name) }}</p>
  <p>Several facts about him:</p>
  <ul>
    {{ for i, fact in enumerate(author.facts): }}{{+}}
      <li>
        Fact №{{ insert(i) }}: {{ insert(fact) }}.
      </li>
    {{-}}
  </ul>
</body>
</html>
```

---

## 🛠 Working with Templates in Python

### Step 1: Import `FileTemplate`

```python
from pytemplatesforpython import FileTemplate
```

### Step 2: Create a `FileTemplate` instance

```python
template = FileTemplate("template.html")
```

### Step 3: Define your data

```python
class Author:
    def __init__(self, name, facts):
        self.name = name
        self.facts = facts

author = Author(
    "Alexey",
    ["lives in Israel", "knows Python, Java, and JavaScript", "can’t think of more facts"]
)
```

### Step 4: Render the template

```python
result = template.render({"author": author})
```

### Step 5: Display or save the result

```python
print(result)
```

```python
with open("result.html", "w+") as file:
    file.write(result)
```

### Step 6: Django integration

```python
from django.http import HttpResponse

def view(req):
    return HttpResponse(template.render({"author": author}))
```

---

## 📁 Managing Multiple Templates

In a real project, you'll likely need multiple templates. Use `TemplatesLoader` for that.

### Step 1: Import

```python
from pytemplatesforpython import TemplatesLoader
```

### Step 2: Initialize

```python
loader = TemplatesLoader("templates/")
```

### Step 3: Load templates

Load one manually:

```python
loader.load_template("example.html")
```

Or load all templates recursively:

```python
loader.recursively_load_folder()
```

### Step 4: Retrieve a template

```python
template = loader.get_template("example.html")
```

> 🔹 All paths are relative to the directory you passed to `TemplatesLoader`.

---

## 🎉 Good Luck!
