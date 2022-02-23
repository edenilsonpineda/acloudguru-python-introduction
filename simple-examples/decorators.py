# def inspect(func, *args):
#    print(f"Running: {func.__name__}")
#    val = func(*args)  # One asterisk for arguments, Two asterisks for keywords
#    print(val)
#    return val

def inspect(func):
    def wrapped_func(*args, **kwargs):
        print(f"Running: {func.__name__}")
        val = func(*args, **kwargs)
        print(f"Result: {val}")
        return val
    return wrapped_func


@inspect
def combine(a, b):
    return a + b


class User:
    base_url = 'https://example.com/api'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def query(cls, query_string):
        assert isinstance(query_string, str)
        return cls.base_url + '?' + query_string

    @staticmethod
    def name():
        return 'Kevin Bacon'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

