#!/usr/bin/python3
"""
serialization and deserialization using XML as an alternative format to JSON
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file

    Args:
        dictionary (dict): The dictionary to serialize
        filename (str): The name of the file to save the XML to
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ")
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary

    Args:
        filename (str): The name of the XML file to read from

    Returns:
        dict: The deserialized Python dictionary
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        deserialized_dict = {}
        for child in root:
            try:
                deserialized_dict[child.tag] = int(child.text)
            except ValueError:
                try:
                    deserialized_dict[child.tag] = float(child.text)
                except ValueError:
                    deserialized_dict[child.tag] = child.text
        return deserialized_dict
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except ET.ParseError:
        print(
            f"Error: Could not parse XML from '{filename}'. Check file format."
            )
        return None
