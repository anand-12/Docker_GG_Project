import sys
from time import sleep

message = "Hello!"
message += " Greetings from your first Greengrass component."

while (True):
# Print the message to stdout, which Greengrass saves in a log file.
    print(message)
    sleep(1)
