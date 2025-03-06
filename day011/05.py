class A:

    def aa(self):
        print("bb")


class B:

    def bb(self):
        print("bb")


class C(A, B):

    def cc(self):
        print("cc")


c1 = C()
c1.aa()
c1.bb()
c1.cc()

