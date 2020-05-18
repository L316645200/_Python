# monkeypath 用于运行时动态修改类或模块。

from SomeOtherProduct.SomeModule import SomeClass


def speak(self):
    return "ook ook eee eee eee!"


SomeClass.speak = speak
