import sys

def is_toplevel() -> bool: 
    """Returns True if this module is executed as top-level entry point."""
    return __name__ == '__main__'

def print_toplevel_status() -> None:
    """Prints the module's top-level status."""
    status = 'is' if is_toplevel() else 'is not'
    print(f'Module {status} executed as top-level entry point.')

if is_toplevel():
    print_toplevel_status()
    sys.exit(0)

