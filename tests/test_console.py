#!/usr/bin/python3
"""Test Console"""

from console import HBNBCommand
import unittest
from models.base_model import BaseModel
import os
from os import getenv
from models.engine.file_storage import FileStorage
import sys
from io import StringIO
from unittest.mock import patch
import pep8
from re import search


class TestHBCommand(unittest.TestCase):
    """Test for the console"""

    if getenv("HBNB_TYPE_STORAGE") != "db":

        def set_init(self):
            """Initialize the json file after each test"""
            if os.path.isfile("file.json"):
                os.remove("file.json")
            FileStorage._FileStorage__objects = {}

    def test_docstring(self):
        """Test doc strings.
        """
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.precmd.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_style_base(self):
        """test pep8 style"""
        style = pep8.StyleGuide()
        res = style.check_files(["console.py"])
        self.assertEqual(res.total_errors, 0, "fix pep8")

    def test_help_EOF(self):
        """Test EOF"""
        with patch('sys.stdout', res=StringIO()) as text:
            HBNBCommand().onecmd("help EOF")
        value = text.getvalue()
        message = "Exits the program without formatting\n\n"
        self.assertEqual(value, message)

    def test_help(self):
        """Test help message"""
        with patch('sys.stdout', res=StringIO()) as text:
            HBNBCommand().onecmd("help")
        value = text.getvalue()
        message = """\nDocumented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update\n\n"""
        self.assertEqual(value, message)

    def test_quit(self):
        """ """
        with patch('sys.stdout', res=StringIO()) as text:
            HBNBCommand().onecmd("help quit")
        value = text.getvalue()
        message = "Exits the program with formatting\n\n"
        self.assertEqual(value, message)

    if getenv("HBNB_TYPE_STORAGE") != "db":

        def test_create(self):
            """ """
            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("help create")
            value = text.getvalue()
            message = "Creates a class of any type\n\
[Usage]: create <className>\n\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("create HELL")
            value = text.getvalue()
            message = "** class doesn't exist **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("create BaseModel")
            value = text.getvalue()
            trex = r"\w+[-]\w+[-]\w+[-]\w+[-]\w+\n"
            self.assertTrue(search(trex, value))

        def test_show(self):
            """ """
            res = BaseModel()
            res.save()
            nid = res.id

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("help show")
            value = text.getvalue()
            message = "Shows an individual instance of a class\n\
[Usage]: show <className> <objectId>\n\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("show")
            value = text.getvalue()
            message = "** class name missing **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("show Hi")
            value = text.getvalue()
            message = "** class doesn't exist **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("show Place")
            value = text.getvalue()
            message = "** instance id missing **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("show State 8")
            value = text.getvalue()
            message = "** no instance found **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("show BaseModel {}".format(nid))
            value = text.getvalue()
            trex = r"\[BaseModel\] \(.*\) .*"
            self.assertTrue(search(trex, value))

        def test_count(self):
            """ """
            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("help count")
            value = text.getvalue()
            message = "Usage: count <class_name>\n"
            self.assertEqual(value, message)

            res = BaseModel()
            res.save()

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("count BaseModel")
            value = text.getvalue()
            message = "1\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("count User)")
            value = text.getvalue()
            message = "0\n"
            self.assertEqual(value, message)

        def test_destroy(self):
            """ """
            res = BaseModel()
            res.save()
            nid = res.id

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("help destroy")
            value = text.getvalue()
            message = "Destroys an individual instance of a class\n\
[Usage]: destroy <className> <objectId>\n\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("destroy")
            value = text.getvalue()
            message = "** class name missing **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("destroy Hi")
            value = text.getvalue()
            message = "** class doesn't exist **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("destroy State")
            value = text.getvalue()
            message = "** instance id missing **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("destroy Place 6")
            value = text.getvalue()
            message = "** no instance found **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("destroy BaseModel {}".format(nid))
            value = text.getvalue()
            message = ""
            self.assertEqual(value, message)

        def test_help_all(self):
            """ """
            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("help all")
            value = text.getvalue()
            message = "Shows all objects, or all of a class\n\
[Usage]: all <className>\n\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("all")
            value = text.getvalue()
            message = "[]\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("all Hi")
            value = text.getvalue()
            message = "** class doesn't exist **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("all Place")
            value = text.getvalue()
            message = "[]\n"
            self.assertEqual(value, message)

            res = BaseModel()
            res.save()
            nid = res.id

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("all BaseModel {}".format(nid))
            value = text.getvalue()
            trex = r"[\.*]"
            self.assertTrue(search(trex, value))

        def test_update(self):
            """ """
            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("help update")
            value = text.getvalue()
            message = "Updates an object with res information\n\
Usage: update <className> <id> <attName> <attVal>\n\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("update Hi")
            value = text.getvalue()
            message = "** class doesn't exist **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("update")
            value = text.getvalue()
            message = "** class name missing **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("update Place")
            value = text.getvalue()
            message = "** instance id missing **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("update BaseModel {} Hi".format(nid))
            value = text.getvalue()
            message = "** value missing **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("update State 6)
            value = text.getvalue()
            message = "** no instance found **\n"
            self.assertEqual(value, message)

            res = BaseModel()
            res.save()
            nid = res.id

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("update BaseModel {}".format(nid))
            value = text.getvalue()
            message = "** attribute name missing **\n"
            self.assertEqual(value, message)

            with patch('sys.stdout', res=StringIO()) as text:
                HBNBCommand().onecmd("update BaseModel {} a 6".format(nid))
            value = text.getvalue()
            message = ""
            self.assertEqual(value, message)


if __name__ == "__main__":
    unittest.main()
