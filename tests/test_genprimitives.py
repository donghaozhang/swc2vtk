# -*- coding: utf-8 -*-
import unittest
import swc2vtk


class TestGenPrimitives(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.gen_primitives = swc2vtk.GenPrimitives()

    def test_cuboid(self):
        self.gen_primitives.cuboid()

    def test_sphere(self):
        self.gen_primitives.sphere()

    def test_hemisphere(self):
        self.gen_primitives.hemisphere()


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestGenPrimitives))
    return suite


if __name__ == '__main__':
    unittest.main()
