def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        # Conta i caratteri, inclusi spazi e newline
        total_characters = len(file_contents)

        # Conta le parole
        words = file_contents.split()
        total_words = len(words)

        # Stampa i risultati
        #print(f"Total characters: {total_characters}")
        #print(f"Total words: {total_words}")

        # Conta le lettere
        chars = {}
        list_chars = []
        for c in file_contents:
            lowered = c.lower()
            if lowered.isalpha():
                if lowered in chars:
                    chars[lowered] += 1
                else:
                    chars[lowered] = 1

                
         # Crea la struttura desiderata
        list_chars = [{"letter": letter, "count": count} for letter, count in chars.items()]

        # Ordina la lista per conteggio decrescente
        list_chars.sort(key=lambda x: x["count"], reverse=True)

         # Stampa i risultati nel formato richiesto
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{total_words} words found in the document")
        
        
        for item in list_chars:  # item è un dizionario con "letter" e "count"
            letter = item["letter"]
            count = item["count"]
            print(f"The '{letter}' character was found {count} times")

        print("--- End report ---")

        
main()



