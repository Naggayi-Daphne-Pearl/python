import urllib.request, urllib.parse, urllib.error

# This line uses the urlopen function from the urllib.request module to open the specified URL and assign the resulting file-like object to the variable fhand
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

#This line starts a for loop that iterates over the lines in the file-like object fhand.
for line in fhand:

    #This line prints each line of the file, after it has been decoded from bytes to a string using the decode method, and after the leading and trailing whitespace has been removed using the strip method.
    print(line.decode().strip())