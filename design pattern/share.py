#-*- encoding:utf-8 -*-
__author__ = ''
class Share_m():
    def __init__(self,name=""):
        self.value={}
        self.name=name
    def __getitem__(self, item):
        print("method __getitem__{item} return".format(item=item))
        return self.value[item]
    def __setitem__(self, key, value):
        print("method __setitem__")
        self.value[key]=value
    def __del__(self):
        print("delete item")
        del self.value
class Obj:
    def __init__(self, value):
        self.content = value

    def __str__(self):
        return self.content


class Share(object):
    def __init__(self):
        super().__init__()
        self.dct = {}

    def __getitem__(self, item):
        return self.dct.get(item, None)

    def __setitem__(self, key, value):
        self.dct[key] = value


def main():
    share = Share()
    share['one'] = Obj("a")
    share['two'] = Obj("b")
    share['one'] = Obj("c")
    one = share['one']
    print(str(one))


if __name__ == '__main__':
    main()
    # s = Share_m("share obj")
    # s["c1"] = "object"
    # print(s["c1"])
    # del s
