def short_words(my_list: list[str]) -> list[str]:
        """Return words that are shorter than 5 characters."""
        my_list2: list[str] = []
        i: int = 0
        while i < len(my_list):
            if len(my_list[i]) < 5:
                my_list2.append(my_list[i])
            else: 
                print(f"{my_list[i]} was too long.")
            i += 1

        print(my_list2)
        return my_list2

my_list = ["sun", "cloud", "sky"]
short_words(my_list)