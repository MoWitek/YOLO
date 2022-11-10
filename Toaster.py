from __future__ import annotations


class NotHumanConfirmed(Exception):
    pass


def visualize(dictionary, *, free_line=True):
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

    def tree_walker(thing, hook_part, passed_msg="Passed!", failed_msg="FAILED!", not_human_confirmed="!HUMAN"):
        yeet = passed_msg
        if type(thing) is function:
            try:
                try:
                    thing()
                except TypeError:
                    thing(None)

            except NotHumanConfirmed:
                yeet = not_human_confirmed
            except AssertionError:
                headaches.append(thing)
                yeet = failed_msg

            hook_part[thing.__name__] = yeet

        else:
            hook_part[thing.__name__] = {}
            for sub in class_name_extractor(thing):
                tree_walker(sub, hook_part[thing.__name__])

    hook = {}
    headaches = []
    for x in things:
        tree_walker(x, hook)

    visualize(hook)

    if headaches:
        print()
        if print_error_locations:
            print("errors at:")
            for err in headaches:
                print(err.__qualname__)


if __name__ == '__main__':
    class idk:

        def thing(self):
            assert True

        @staticmethod
        def other():
            assert True

        class aaaaa():
            @staticmethod
            def bbbb():
                assert True

            def error(self):
                assert True


    Test([idk])
