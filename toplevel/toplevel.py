import sys

def is_toplevel(module) -> bool: 
    """Returns True if specified module is executed as top-level entry point."""
    return module.__name__ == '__main__'

def print_toplevel_status(module) -> None:
    """Prints the specified module's top-level status."""
    status = 'is' if is_toplevel(module) else 'is not'
    print(f'Module {status} executed as top-level entry point.')

if is_toplevel(sys.modules[__name__]):
    print_toplevel_status(sys.modules[__name__])
    sys.exit(0)

