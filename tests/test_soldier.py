import unittest
from models.units.soldier import Soldier


class TestSoldier(unittest.TestCase):

    def test_check_active_active(self):
        soldier = Soldier()
        self.assertTrue(soldier.check_active())

    def test_check_active_not_active(self):
        soldier = Soldier(health=0)
        self.assertFalse(soldier.check_active())
