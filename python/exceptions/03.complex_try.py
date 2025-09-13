def serve_chai(flavour):
    try:
        if flavour == "Unknown":
            raise ValueError("We don't know that flavour")
        else:
            print(f"Preparing {flavour} chai....")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavour} chai is served")
    finally:
        print("Next customer please")

serve_chai("Masala")
serve_chai("Unknown")

