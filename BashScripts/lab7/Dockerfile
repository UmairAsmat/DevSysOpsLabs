# Use an official base image
FROM ubuntu:latest

# Create a directory to serve as the source of our backup
RUN mkdir /source
WORKDIR /source

# Create some test files
RUN echo "This is file 1." > file1.txt && echo "This is file 2." > file2.txt

# Create a directory to serve as the backup destination
RUN mkdir /backup

# Copy the files from source to backup
CMD cp -r /source /backup
