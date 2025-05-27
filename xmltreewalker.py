import xml.etree.ElementTree as ET

xml_data = """
<root>
    <child name="A">Hello</child>
    <child name="B">World</child>
</root>
"""

root = ET.fromstring(xml_data)

def walk_xml(element):
    print(f"Tag: {element.tag}, Attributes: {element.attrib}, Text: {element.text.strip() if element.text else ''}")
    for child in element:
        print(child)
        walk_xml(child)

walk_xml(root)
