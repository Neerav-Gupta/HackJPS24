import tika
from tika import parser
import requests
import os
import re 

def pdfScrape(pdf_url):
  tika.initVM()

  response = requests.get(pdf_url)
  pdf_file = 'assets/document.pdf'

  with open(pdf_file, 'wb') as file:
      file.write(response.content)

  parsed_pdf = parser.from_file("assets/document.pdf") 
  data = parsed_pdf['content']  
  os.remove("assets/document.pdf")
  paragraphs = data.split('\n')

  extractedTexts = [["0. Abstract", ""]]
  visistedAbsOrIntro = False
  for i in range(len(paragraphs)):
      if re.findall(r"^\d+\.\s+.*\d{4}.*$", paragraphs[i]) != []: 
        break
      if re.findall(r"^\d+\.\s+[\w\s]+$", paragraphs[i]) != [] and len(paragraphs) > 1500: 
        extractedTexts.append([" ", " "])
        extractedTexts[-1][0] = re.findall(r"^\d+\.\s+[\w\s]+$", paragraphs[i])[0]
        print(paragraphs[i])
      elif re.findall(r"^\d+\.\d+\s+[\w\s]+$", paragraphs[i]) != []: 
        extractedTexts.append([" ", " "])
        extractedTexts[-1][0] = re.findall(r"^\d+\.\d+\s+[\w\s]+$", paragraphs[i])[0]
        print(paragraphs[i])
      elif re.findall(r"^\d+\s+[A-Za-z\s]+$", paragraphs[i]) != []: 
        extractedTexts.append([" ", " "])
        print(paragraphs[i])
        extractedTexts[-1][0] = re.findall(r"^\d+\s+[A-Za-z\s]+$", paragraphs[i])[0]
      paragraph = paragraphs[i]
      extractedTexts[-1][1] += paragraph
  return extractedTexts

print(pdfScrape("https://www.nature.com/articles/nature10836"))