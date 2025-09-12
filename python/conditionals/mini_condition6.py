seat_type = input("Enter seat type (General/AC/Luxury/Sleeper): ").lower()

match seat_type:
    case "sleeper":
        print("You selected Sleeper")
    case "ac":
        print("You selected AC")
    case "general":
        print("You selected general")
    case "luxury":
        print("You selected luxury")
    case _:
        print("Invalid seat type")
