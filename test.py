from pytemplatesforpython import TemplatesLoader
tl = TemplatesLoader("test_files")
tl.recursively_load_folder("test")
t = tl.get_template("test_files/test_template2.txt")

print(t.render([
    {"first":1, "second":2, "result":3},
    {"first":2, "second":5, "result":6},
    ]))
