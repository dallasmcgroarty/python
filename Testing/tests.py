import unittest
from activites import eat, nap, is_funny

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """testing eat healthy"""
        self.assertEqual(
            eat("broccoli",is_healthy=True),
            "I'm eating broccoli, because it's gooood"
        )
    def test_eat_unhealthy(self):
        """testing eat unhealthy"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO!"
        )
    def test_short_nap(self):
        """testing short nap"""
        self.assertEqual(
            nap(1),
            "I'm feeling good after an hour nap"
        )
    def test_long_nap(self):
        """testing long nap"""
        self.assertEqual(
            nap(3),
            "Ugh I overslept and now I'm groggy"
        )
    def test_is_funny(self):
        self.assertFalse(
            is_funny("Tim"), "Tim aint funny"
        )

if __name__ == "__main__":
    unittest.main()