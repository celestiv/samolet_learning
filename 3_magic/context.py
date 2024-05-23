with open("file.txt", "w") as f:
    f.write("Hello")


with open("file1.txt", "r") as f1, open("file2.txt", "w") as f2:
    f2.write(f1.read())


from contextlib import ExitStack
filenames = ["file1.txt", "file2.txt", "file3.txt"]
with open("output_file.txt", "a") as out_file:
    with ExitStack() as stack:
        file_pointers = [stack.enter_context(open(file, "r")) for file in filenames]
        for fp in file_pointers:
            out_file.write(fp.read())


