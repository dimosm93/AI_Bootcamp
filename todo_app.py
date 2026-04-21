# Η λίστα όπου θα αποθηκεύουμε τις εργασίες μας
tasks = []

print("--- AI Engineering To-Do App ---")
print("Οδηγίες: Γράψε την εργασία σου. Γράψε 'show' για να τις δεις ή 'exit' για έξοδο.")

while True:
    # Παίρνουμε την είσοδο από τον χρήστη
    user_input = input("\nΤι θέλεις να κάνεις; ").strip().lower()

    if user_input == 'exit':
        print("Τερματισμός εφαρμογής. Καλή συνέχεια!")
        break # Σπάει το loop και βγαίνει από το πρόγραμμα
    
    elif user_input == 'show':
        print(f"\nΟι εργασίες σου ({len(tasks)}):")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
            
    elif user_input == '':
        print("Παρακαλώ γράψε κάτι, μην το αφήνεις κενό!")
        
    else:
        # Προσθήκη της εργασίας στη λίστα
        tasks.append(user_input)
        print(f"Προστέθηκε: {user_input}")
print(results)