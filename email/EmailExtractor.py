# Email_Extractor.py
# This program will load a given webpage and pull all potential email addresses.
# Email addresses will be printed as a list without duplicates.
# The email address will also be stored to a given file.


import urllib.request
import sys, getopt
from bs4 import BeautifulSoup


def main():
    url = 'https://www.unomaha.edu/college-of-information-science-and-technology/about/faculty-staff/index.php'
    outputfile = 'emails.txt'
    print ('URL is "', url)
    print ('Output file is "', outputfile)
    url = input("Enter a new URL or leave blank for no change: ")
    outputfile = input("Enter a new output file or leave blank for no change: ")
    print ('URL is "', url)
    print ('Output file is "', outputfile)

    emails = []


    url_html = urllib.request.urlopen(url)
    soup = BeautifulSoup(url_html, "html.parser")
    # soup = BeautifulSoup(local_html, "html.parser")

    #Convert the soup to a string version
    soup = str(soup)

    #Get all emails NOT IN <a> tags
    #Split the text into a list, with the end of line \n as the delimiter
    for line in soup.split("\n"):
        if '@' in line:
            link = process_email(line)
            emails = add_to_list(link, emails)

    print('\nEmails Found:', len(emails))
    for email in emails:
        print(email)

    writeToFile(outputfile, emails)


def writeToFile(fileName, emails):
    outFile = open(fileName, 'w')
    for email in emails:
        outFile.write(email + "\n")

    outFile.close()


def add_to_list(to_add, emails):
    if to_add not in emails and to_add != '@':
        emails.append(to_add)
    return emails


def process_email(email):
    at = email.find('@')
    start = 0
    end = len(email) - 1

    if at >= 0:
        for x in range(1, at - start):
            if email[at - x].isalnum():
                x += 1
            else:
                start = at - x + 1
                break
        for y in range(1, end - at):
            if email[at + y].isalpha():
                y += 1
            elif email[at + y] == '.':
                y += 1
            else:
                end = at + y
                break

    email = email[start:end]
    return email

if __name__ == '__main__':
    main()
