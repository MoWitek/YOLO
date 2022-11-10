from __future__ import annotations

def fak(dictionary, *, free_line=True):
    head = "│ "
    string_parts = []

    def ff(dikt, headers):
        for k, v in dikt.items():
            if type(v) is dict:
                string_parts.append(f'{"".join(headers + [head])}') if free_line else None
                string_parts.append(f'{"".join(headers)}├─┬─> {k} <─')
                ff(v, headers + [head])
                continue
            string_parts.append(f"{''.join(headers)}├─> {k}: {v}")

    ff(dictionary, [])
    string = "\n".join(string_parts)
    print(string)


def Test(things: list, *, class_name_extractor: callable = None, print_error_locations=True):
    if class_name_extractor is None:
        class_name_extractor = lambda cls: list(
            filter(None.__ne__, [(getattr(cls, atr) if atr[:2] != "__" else None) for atr in dir(cls)]))
    function = type(lambda: None)

    def tree_walker(thing, hooker_part):
        yeet = True
        if type(thing) is function:
            try:
                try:
                    thing()
                except TypeError:
                    thing(None)

            except AssertionError:
                headaches.append(thing)
                yeet = False

            hooker_part[thing.__name__] = yeet

        else:
            hooker_part[thing.__name__] = {}
            for sub in class_name_extractor(thing):
                tree_walker(sub, hooker_part[thing.__name__])

    hooker = {}
    headaches = []
    for x in things:
        tree_walker(x, hooker)

    fak(hooker)

    if headaches:
        print()
        if print_error_locations:
            print("fucks at:")
            for fuck_up in headaches:
                print(fuck_up.__qualname__)


if __name__ == '__main__':

    class idk:

        def FAK(self):
            assert True

        @staticmethod
        def fuck():
            assert True

        class faaak():
            @staticmethod
            def kys():
                assert True

            def error(self):
                assert True


    Test([idk])
