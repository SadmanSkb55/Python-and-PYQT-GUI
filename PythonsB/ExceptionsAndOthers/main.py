try:
    age=int(input("Enter Age: "))
    income=int(input("Enter Income: "))
    risk=income/age
    print(risk)
except ZeroDivisionError:
    print("Math error")
except ValueError:
    print("invalid")
except Exception:
    print("Exception")