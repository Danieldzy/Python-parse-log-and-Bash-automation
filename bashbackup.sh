!/bin/bash

#define the file that need backup and the backup directory
file="/home/student/member_data.txt"
dir="/home/student/Autobackup"

#add time stamp to the member_data file so each time of backup 
#a new time stamped file will appear
newfile="$dir/member_data_$(date +%Y%m%d_%H%M%S).txt"

# Copy the file to the backup directory and rename to newfile with time stamp
cp "$file" "$newfile"

# Print a message indicating the backup was successful
echo "Backup of $file completed and saved as $newfile"
