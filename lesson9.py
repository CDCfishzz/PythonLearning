from collections.abc import Iterable
from collections.abc import Iterator


print(isinstance([], Iterable))
print(isinstance((x for x in range(10)), Iterator))
