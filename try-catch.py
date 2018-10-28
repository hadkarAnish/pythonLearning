while True:
    try:
        number = int(input("enter a number: "))
        print(2/number)
        break
        
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Zero doesn't work")
    except Exception as e:
        print("some other error: " + repr(e))
        # repr gives u the complete exception + the message string whereas str(e) will give only the message string

    finally:
        print("next loop")
