class MatrixException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.msg = args[0] if args else None

    def __str__(self):
        return f"Error: {self.msg}"
