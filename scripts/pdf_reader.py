import re
import json
from PyPDF2 import PdfReader

filepath = '2_2.pdf'

pdf_file = open(filepath, "rb")
pdf_reader = PdfReader(pdf_file)
total_pages = len(pdf_reader.pages)


text = ""
for page in range(total_pages):

    page_obj = pdf_reader.pages[page]
    page_text = page_obj.extract_text()
    page_text = page_text.replace('\n', '  ').encode('ascii', 'ignore').decode()
    text += page_text

pdf_file.close()

structured_data = {
    'Details': {},
    'Total': ''
}

main_regex = r"([A-Z ]+ [\d]+)(.*?)(Sub Total ... [\d\,\.]+)"

matches = re.finditer(main_regex, text, re.MULTILINE | re.DOTALL)

for matchNum, match in enumerate(matches, start=1):
    
    description = match.group(1).strip().split('  ')[0]
    details = match.group(2)
    sub_total = match.group(3).strip().replace('Sub Total ... ', '')

    inner_regex = r"([A-Za-z \.\(\)]+) ([\d\,\.]+)"

    inner_matches = re.finditer(inner_regex, details, re.MULTILINE | re.DOTALL)

    for inner_matchNum, inner_match in enumerate(inner_matches, start=1):
        
        inner_description = inner_match.group(1).strip()
        inner_amount = inner_match.group(2).strip()

        if(description not in structured_data['Details']):
            structured_data['Details'][description] = {
                'details': [],
                'sub_total': sub_total
            }

        structured_data['Details'][description]['details'].append({
            'description': inner_description,
            'amount': inner_amount
        })

total_regex = r"(  Total ... [\d\,\.]+)"

total_amount = re.findall(total_regex, text, re.MULTILINE | re.DOTALL)

structured_data['Total'] = total_amount[0].strip().replace('Total ... ', '')


print(json.dumps(structured_data, default=str))

