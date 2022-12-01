from pytemplater import TemplatesLoader
tl = TemplatesLoader()
tl.load_template("test_template.txt")
print(repr(tl.get_template("test_template.txt").render(None)))
