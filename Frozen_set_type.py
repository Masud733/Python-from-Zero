def main():
    try:
        # Creating a frozenset
        animals = frozenset(["lion", "elephant", "giraffe"])
        print("Animals:", animals)

        # Attempting to modify the frozenset (will raise an AttributeError)
        try:
            animals.add("zebra")
        except AttributeError as e:
            print("Error:", e)


    except Exception as ex:
        print("An error occurred:", ex)

if __name__ == "__main__":
    main()
