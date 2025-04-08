import time

def main():
    seconds = 0
    while True:
        try:
            user_input = int(input("Enter the countdown duration in seconds: "))
            if user_input < 0:
                print("Invalid input. Please enter a positive number of seconds.")
                continue
            seconds = user_input
            break
        except ValueError:
            print("Invalid input. Please enter a valid number of seconds.")

    for i in range(seconds, 0, -1):
        print(f"Time left: {i} seconds.", end="\r")
        time.sleep(1)

    print("\nCountdown finished!")  

main()