from mailextract import mail_map
from pymu import pdf_dump
from ocrtrial import ocr_txt

""""
READ ME:

The question Rajeev asked about extracting PDF attachments from emails and decoding their contents into a JSON file really intrigued me. SO I gave it a simple try

This project does not parse or sort data collected simply because each pdf file has different information and layouts .
 What I implemented is as following
 1) connect to email IMAP4
 2) fetch last email
 4) create a folder for it, and download attaachment into it 
 3) File location then is passed to pdf_dump() and file location dumps the text and xml file into a JSON file ( these files are not sorrted but xml can be used later for parsing confg per form requirment)
 4)I decided to add an extra  OCR (optical charecter recognition ) model to this. For comparision sake.
            turns out pdf text scraping does a much better job for numeral and symbol recognition
 5) The output is returned as a .txtfile with name of attachment.

 FINAL NOTE: Again I wanted to elaborate in regarding to the stucture of copied data. I was going to parse it and make it look neat but realized that this is only required for 
            stuctured forms. I tested my code against different types of pdfs and all data was extracted from all of them succesfully. PArsing while simple requires structured forms than need to be handled individually
            Finally, I was going to use a CNN but realized that the time required to train and collect those data forms will be very tedious so decided to go with the OCR and dump approach


TIME ELAPSED: 6 HOURS NOT 40 MINS :)


P.S if config file still locked i pasted the contents under this line
username = "mail.export.ex@gmail.com"
password = "JohnRedcorn123"
server = "imap.gmail.com"

"""

if __name__ == "__main__":
    #creates folder for email fetched and downloads attachment
    x = mail_map()
    #dump attachments as xml and text into JSON 
    # if csv is wanted just uncomment csv line in function pdf_dump
    pdf_dump(x)
    # or use ocr to create txt file 
    ocr_txt(x)

