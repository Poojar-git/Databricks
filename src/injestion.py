import logging

logging.basicConfig(level=logging.INFO)

def add(a, b):
    logging.info("Adding two numbers")
    return a + b

print(add(10, 20))
#Ingestion means taking data from one place and bringing it into your program for processing.