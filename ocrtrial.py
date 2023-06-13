# Import libraries
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
  
# # Path of the pdf
# PDF_file = "11.pdf"

def ocr_txt(PDF_file):

  # Store all the pages of the PDF in a variable
  pages = convert_from_path(PDF_file, 500)
    
  # Counter to store images of each page of PDF to image
  image_counter = 1
    
  # Iterate through all the pages stored above
  for page in pages:
 
      # PDF page name
      filename = "page_"+str(image_counter)+".jpg"
        
      # Save the image of the page in system
      page.save(filename, 'JPEG')
    
      # Increment the counter to update filename
      image_counter = image_counter + 1
    
  '''
  Part #2 - Recognizing text from the images using OCR
  '''
  # Variable to get count of total number of pages
  filelimit = image_counter-1
    
  # Creating a text file to write the output
  outfile = str(PDF_file + ".txt")
    
  # Open the file in append mode
  f = open(outfile, "a")
    
  # Iterate from 1 to total number of pages
  for i in range(1, filelimit + 1):
    
      # Set filename to recognize later
      
      filename = "page_"+str(i)+".jpg"
            
      # Recognize the text as string in image using pytesserct
      text = str(((pytesseract.image_to_string(Image.open(filename)))))
    
    #remove /n line strings
      text = text.replace('-\n', '')    
    
      #  write processed text to the .txt file.
      f.write(text)
    
  # Close the file after writing all the text.
  f.close()

