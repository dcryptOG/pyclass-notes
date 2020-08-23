#
#!add CSV NOTES
#!CSV stand sfor comma separated values
# *CSV IS imported into Spreadsheets or a Statistics Package
# ?STAT PROGRAMS STAYED ARE SPSS
# EXCEL
# SHEETS
# R
# Sata

fileconnection = open("olympics.txt", "r")
lines = fileconnection.readlines()
for lin in lines[:6]:
    print(lin.strip())
print("------------------")
header = lines[0]
#
field_names = header.strip().split(',')
# first strip get rid of new line character at end of each line
# split(',') get rid of where there is a comma
print(field_names)
# once you use split a list is returned and you can use indexing
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        # print name if person won medal
        print("{}: {}; {}".format(
            vals[0],
            vals[4],
            vals[5]))

#! more advanced version of CSV format where it separates in commas and encloses all values in quotes
# * if CSV is in quotes use Pythons built in CSV module

# * sometims you get a different column sepataor
#! Such as | or tab
# * just call
#! .split('|') or .split(\\t)

#! WRITING DATA TO ACSV FILE

olympians = [("John Aalberg", 31, "Cross Skiing"), ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 53, "Art Competitions"), ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
outfile.write("Name,Age,Sport")
# if one of name has commas we can put all values in quotes
# ?outfile.write('"Name","Age","Sport"')
# use single quotes as delimiter
outfile.write('\n')
for olympian in olympians:
    # can also use .join() method
    #','.join([olympian[0], str(olympian[1]), olympian[2]])
    # can use concat method too
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

#!-------------------------------------------
#! File Names
# *Dont use comma names in file names
# *don't use mre than 1 period
# Dont use \ or /
# ?Don't use spaces
