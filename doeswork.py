import pandas
def displayval():
#reads specific column-'Link' from the file tp.csv
    io_link = pandas.read_csv('tp.csv',sep=",",usecols=['Link'])
#Neglects the empty cells in the column 'Link'
    io_link = io_link[pandas.notnull(io_link['Link'])]
#To extract dates of the format yyyy-mm-dd from the URL
    io_link['date'] = io_link['Link'].str.extract('([0-9]{4}-[0-9]{2}-[0-9]{2})', expand=False).str.strip()
#To extract the query from the URL
    io_link['query'] = io_link['Link'].str.extract('q=(.*)')
    io_link['pre_result1'] = io_link['query'].str.replace('%20',' ')
#Removes unnecesssary substrings when the string contains special characters
    io_link['pre_result2'] = io_link['pre_result1'].str.replace('%E2%80%99',' ')
#Removes unnecessary substrings when the string contains a % as a keyword
    io_link['result'] = io_link['pre_result2'].str.replace('25%20',' ')
#Prints the dates and query from the URL
    print(io_link['date'],io_link['result'])
displayval()
