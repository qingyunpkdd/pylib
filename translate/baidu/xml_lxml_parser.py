from lxml import etree
xml_file = etree.parse(r'd:\test.xml')
root_node = xml_file.getroot()
concept_list = xml_file.xpath('//DescriptorRecord/DescriptorName/String/text()')
#translate each concept for future parsing
