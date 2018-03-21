while True:
    try:
        number=int(input("Enter ur fav no."))
        print(18/number)
        break
    except ZeroDivisionError:
        print("Dont pick zero.")
    except ValueError:
        print("Enter no. not string")
    finally:
        print("Nitya")
