#!/usr/bin/python3
import string
print(*list(getattr(string, '__dict__')['ascii_uppercase']), sep='')
