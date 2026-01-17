import urllib.request as urllib
def main(dhruv):
    print("Checking connectivity ")
    response = urllib.urlopen(dhruv)
    print("Connected to" , dhruv, "succesfully")
    print("The response code was: ", response.getcode())
print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")
main(input_url)

