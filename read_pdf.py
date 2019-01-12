
# importing all the required modules
import PyPDF2
import csv


# creating an object
file = open('vocabulary.pdf', 'rb')

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)

# print the number of pages in pdf file
page_nr = fileReader.numPages

voc_list = []

for i in range(4, page_nr):
    page = fileReader.getPage(i)
    page_text = page.extractText()
    # print(page_text)
    page_splitted = page_text.splitlines()
    for line_text in page_splitted:
        # print(line_text)
        if line_text.find("  ") > -1:
            line_splitted = line_text.split("  ")
            line_splitted = tuple(line_splitted)
            voc_list.append(line_splitted)
            # print(voc_list)

print(voc_list)
with open('./voc.csv', 'w') as file:
    wr = csv.writer(file, dialect='excel')
    wr.writerows(voc_list)
