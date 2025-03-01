import time
import winsound
def study_timer():
    try:
        minutes = int(input("Enter study time in minutes:"))
        seconds = minutes * 60
        print(f"Timer is running for {minutes} minutes")
        while seconds >= 0:
            mins,secs = divmod(seconds,60)
            print(f"\r{mins:02}:{secs:02}",  end = "", flush = True  )
            time.sleep(1)
            seconds -= 1
        print("\nTime is up")
        winsound.Beep(1000,3000)
    except KeyboardInterrupt:
        print("\nTIMER INTERRUPTED")
    except ValueError:
        print("\nInvalid input. Please enter a number")
study_timer()





