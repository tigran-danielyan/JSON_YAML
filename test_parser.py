from parser import json_to_yaml_parser
import unittest


class TestParser(unittest.TestCase):
    
    def test_json_to_yaml_files(self):
        self.assertRaises(ValueError,json_to_yaml_parser,"","")
        self.assertRaises(ValueError,json_to_yaml_parser,"","a")
        self.assertRaises(ValueError,json_to_yaml_parser,"b","")

    def test_json_to_yaml_func(self):
        self.assertEqual(json_to_yaml_parser("test.json","test.yaml"),"\nDone")
        self.assertNotEqual(json_to_yaml_parser("other.json","test.yaml"),"\nDone")
        self.assertEqual(json_to_yaml_parser("no.json","test.yaml"),
                                            F"JSON file with name no.json isn't found")
        self.assertEqual(json_to_yaml_parser("test_incorrect.json","test.yaml"),
                                            "The Json file is misconfigured")
        self.assertEqual(json_to_yaml_parser("./","test.yaml"),"Something went wrong")
        self.assertEqual(json_to_yaml_parser("test.json","./"),"Something went wrong")



if __name__ == "__main__":
    unittest.main()