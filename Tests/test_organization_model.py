import unittest
from Source.settings_manager import settings_manager
from Source.Models.organization import organization_model


class test_organization_model(unittest.TestCase):
    def setUp(self):
        self.settings_manager = settings_manager()
        self.settings_manager.open("settings.json")
        self.settings_manager.convert()
        self.settings = self.settings_manager.data

    def test_organization_creation_with_settings(self):
        organization = organization_model("Test Organization")

        organization.inn = self.settings["inn"]
        organization.account = self.settings["account"]
        organization.bik = self.settings["bik"]
        organization.ownership_type = self.settings["ownership_type"]

        self.assertEqual(organization.name, "Test Organization")
        self.assertEqual(organization.inn, self.settings["inn"])
        self.assertEqual(organization.account, self.settings["account"])
        self.assertEqual(organization.bik, self.settings["bik"])
        self.assertEqual(organization.ownership_type, self.settings["ownership_type"])