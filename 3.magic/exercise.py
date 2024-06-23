class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        try:
            self.open_file = open(file=self.filename, mode=self.mode)
        except Exception as e:
            print(f"Exception opening file: {e}")
            raise
        return self.open_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.open_file:
            try:
                self.open_file.close()
            except Exception as e:
                print(f"Exception closing file: {e}")
                raise
        if exc_type is not None:
            print(f"Exception is not None: {exc_val}")
        return False


with FileHandler("11.txt", "r") as f:
    print(f.read())
