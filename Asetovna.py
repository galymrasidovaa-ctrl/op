from typing import List, Dict

def read_lines(path: str) -> List[str]:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

def write_lines(path: str, lines: List[str]) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

class ParseError(Exception):
    pass

def parse_csv_line(line: str, delimiter: str = ',') -> Dict[str,str]:
    try:
        items = line.split(delimiter)
        result = {}
        for item in items:
            if ':' not in item:
                raise ParseError(f"Invalid item: {item}")
            k, v = item.split(':', 1)
            result[k.strip()] = v.strip()
        return result
    except Exception as e:
        if isinstance(e, ParseError):
            raise
        raise ParseError(str(e))

x_global = "global x"

def outer():
    x_enclosing = "enclosing x"
    def inner():
        x_local = "local x"
        print("inner:", x_local)
    inner()
    print("outer:", x_enclosing)

def shared():
    return "shared helper"

def func_in_b():
    return "hello from b"

def call_b():
    print("a -> calling b.func_in_b() ->", func_in_b())

def call_a():
    print("b -> calling a.call_b()")
    call_b()

def demo_file_io():
    p = "sample.txt"
    lines = ["name:Alice,age:30", "name:Bob,age:25"]
    write_lines(p, lines)
    r = read_lines(p)
    print("Read lines:", r)

def demo_parsing():
    line = "name:Charlie, age:40"
    parsed = parse_csv_line(line)
    print("Parsed:", parsed)

def demo_alias():
    print("Using alias parse:", parse_csv_line("k:1,v:2"))

def demo_namespaces():
    print("global:", x_global)
    outer()

def demo_circular_fix():
    print("Demonstrating fixed circular import:")
    call_b()
    call_a()

if __name__ == "__main__":
    demo_file_io()
    print("-" * 40)
    try:
        demo_parsing()
    except Exception as e:
        print("Parse failed:", e)
    print("-" * 40)
    try:
        demo_alias()
    except Exception as e:
        print("Alias parse failed:", e)
    print("-" * 40)
    demo_namespaces()
    print("-" * 40)
    demo_circular_fix()
