import re    #import regex module

# Define Regex pattern to match IP address and status code in Apache log format, I keep the method(GET|POST|HEAD)
# inside the pattern in case in future I can also print them out since they can provide more information about
# the threat and we can obtain more insight of this paticular attack
pattern = r'(\d+\.\d+\.\d+\.\d+) .* "(GET|POST|HEAD) .+" (\d{3}) '
#for this regex pattern, group 1 (\d+\.\d+\.\d+\.\d+) match Ip address, group 2 (GET|POST|HEAD) is method
# (\d{3}) is group3 that match the code (403 404), the group are denoted in regex pattern using ()

# Pointing the path of the file, use r to ensure the\ in path is a string
logfile_path = r"C:\Users\leizy\OneDrive\桌面\Linux_log\apache_logs.txt"

def parse_log(logfile_path):
    # Nested Dictionary to store counts of 403 and 404 errors by IP, It will store all the 403 code
    # with its corresponding ip address : count pair, also for 404
    error_counts = {'403': {}, '404': {}}

    # Open and read log file
    with open(logfile_path, 'r') as file:
        for line in file:
            # Attempt to match pattern in the current line, re.match is the sub module in re module
            # it will match pattern we defined in line variable, and the result will be stored in the match variable
            match = re.match(pattern, line)
            if match is not None:
                ip = match.group(1)   # Group is a method of the match method, just remember match.group(1) is always used and correct. Extract IP address since IP address is group1 of our pattern variable
                code = match.group(3) # Extract code, it is the group3 in our regex pattern variable
                #print(code)  #keep print for debugging purpose
                #print(ip) #debugging
                   
                # Check if status code is 403 or 404
                if code in ['403', '404']:
                    if ip not in error_counts[code]: #when ip in code 403 and 404, set the first ip occurance
                        error_counts[code][ip] = 1  #the first occurance count is set to 1
                    else:
                        error_counts[code][ip] += 1 #increament each ip occurance and add the count

    return error_counts

#call the parse_log function
error_counts = parse_log(logfile_path)
#print(error_counts) #print to see if the nested log can be printed, for debugging

# Now we need to sort the IP based on counts, first we define 2 variable according to 403 404
# use get()function to extract ip_count dictionary from the error_counts main dictionary
ip_counts403 = error_counts.get('403', {})
ip_counts404 = error_counts.get('404', {})
# then we sort the count from biggest to smallest, we use .items() function to store the view of our ip_count dictionary
# then we sort it in descending order based on count
sorted_count403 = sorted(ip_counts403.items(), key=lambda x: x[1], reverse=True)
sorted_count404 = sorted(ip_counts404.items(), key=lambda x: x[1], reverse=True)


# Print counts for 403 errors
print("403 Errors:")
for ip, count in sorted_count403:
    print(f"IP: {ip}, Count: {count}")

# Print counts for 404 errors
print("\n404 Errors:")
for ip, count in sorted_count404:
    print(f"IP: {ip}, Count: {count}")