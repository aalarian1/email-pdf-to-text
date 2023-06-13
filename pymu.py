from typing import Mapping
import fitz
import pprint
import csv,json

def pdf_dump(filepath):
    text1 = []
    # with fitz.open(filepath ) as doc:
    #     for page in doc:
    #         blocks = page.getText('blocks')
    #         blocks.sort(key=lambda block: block[1])
    #         text1.append(blocks)
    # # print(text)
    # blocks = page.getText("blocks")
    # blocks.sort(key=lambda block: block[1])  # sort vertically ascending
    # for b in blocks:
    #     print(b[4])  # the text part of each block

    #initialize empty lists
    text = []
    xml = []
    #open pdf, loop through pages, append to list
    with fitz.open(filepath ) as doc:
        for page in doc:
            text.append(page.getText())
            xml.append(page.getText('xml'))
    # for line in lines:
    #     text.append(line.strip().split('\n'))

#json dump 
    with open(filepath + '.json', 'w+', encoding ='utf8') as json_file:        
        json.dump((text, xml), json_file, ensure_ascii = True)
    return print("PDF to text & XML conversion completed")


