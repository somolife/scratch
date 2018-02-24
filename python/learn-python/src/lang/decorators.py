def print_fn_name(fn):
    def _print_fn_name(*args, **kwargs):
        print "<!-- fn:", fn.__name__, "-->"
        fn(*args, **kwargs)

    return _print_fn_name
