import threading
import time
userInput = 0

def printMessage(message: str):
    while userInput == 0:
        print(f"The message given by the system: {message}", end="\n")
        time.sleep(2)


if __name__ == "__main__":
    thread_1 = threading.Thread(target=printMessage, args=("Jai Shree Ram!!",))
    thread_1.start()

    userInput = int(input("Enter 100 to stop system messages: \n"))