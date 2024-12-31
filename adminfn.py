def admin_page():
    choose = input(
        "1. add\n"
        "2. display\n"
        "3. search\n"
        "4. sort\n"
        "5. modify\n"
        "6. exit\n"
        "Enter character: ")
    return choose


def add_menu():
    choose = input(
        "a. coach\n"
        "b. sport\n"
        "c. sport schedule\n"
        "d. exit\n"
        "Enter character: ")
    return choose


def display_records():
    choose = input(
        "a. coach\n"
        "b. sport\n"
        "c. registered student\n"
        "d. exit\n"
        "Enter character: ")
    return choose


def search_records():
    choose = input(
        "---------------- Search ------------------\n"
        "a. coach ID\n"
        "b. overall performance(Rating)\n"
        "c. sport ID\n"
        "d. student ID\n"
        "e. exit\n"
        "Enter character: ")
    return choose


def sort_records():
    choose = input(
        "-----------------------------------------------------\n"
        "a. sort Coaches by name.\n"
        "b. Coaches Hourly Pay Rate\n"
        "c. Coaches Overall Performance\n"
        "e. exit\n"
        "Enter character: ")
    return choose


def modify_menu():
    choose = input(
        "---------------- Modify ------------------\n"
        "a. Coaches records : \n"
        "b. sports records : \n"
        "c. sport schedule records: \n"
        "e. exit\n"
        "Enter character: ")
    return choose


def modify_by():
    choose = input(
        "---------------------- change -------------------------\n"
        "a. coach's name: \n"
        "b. coach's date Terminated: \n"
        "c. coach's hourly wage: \n"
        "d. coach's telephone number: \n"
        "e. coach's address: \n"
        "f. sports center code: \n"
        "g. sports center name: \n"
        "h. sports code: \n"
        "i. coach's sports: \n"
        "j. exit\n"
        "Enter character: ") 
    return choose


def _exit():
    section = "n"
    return section


def list_length(arr):
    count = 0
    for i in arr:
     count += 1
    return count


def dist_value(array):
    unique = []
    for x in array:
        if not x in unique:
            unique.append(x)
            
    return unique

def priceSort(index):
    coaches_info = open("data/coach.txt","r")
    coaches = coaches_info.readlines()
    coaches_info.close()
    for coach_dx in range(len(coaches)-1,0,-1):
         for dx in range(coach_dx):
             if coaches[dx].split(',')[index][2:] > coaches[dx+1].split(',')[index][2:]:
                 temp = coaches[dx]
                 coaches[dx] = coaches[dx+1]
                 coaches[dx+1] = temp
    return coaches


def nameRatingSort(index):
    coaches_info = open("data/coach.txt","r")
    coaches = coaches_info.readlines()
    coaches_info.close()
    for coach_dx in range(len(coaches)-1,0,-1):
         for dx in range(coach_dx):
             if coaches[dx].split(',')[index] > coaches[dx+1].split(',')[index]:
                 temp = coaches[dx]
                 coaches[dx] = coaches[dx+1]
                 coaches[dx+1] = temp
    return coaches

def add():
    add_page = "y"
    while add_page == "y":
        choose = add_menu()
        if choose == "a":
            is_coach = False
            print("------------ Enter Coach Details -------------")
            coach_id = input("ID: ").strip()
            coaches_info = open("data/coach.txt", "r")
            coaches = coaches_info.readlines()
            coaches_info.close()
            for coach in coaches:
                if coach.split(",")[0] == coach_id:
                    is_coach = True
                    break
            if not is_coach:
                name = input("name: ").strip()
                date_joined = input("Date of Joined: ").strip()
                date_terminated = input("Date of Terminated: ").strip()
                wage = input("hourly wage in RM(Range 100 to 500): ").strip()
                contact = input("contact: ").strip()
                address = input("address: ").strip()
                center_code = input("sport center code: ").strip()
                center_name = input("sport center name: ").strip()
                sport_code = input("sports code: ").strip()
                sport_name = input("coach's sports: ").strip()
                coaches = open("data/coach.txt", "a")
                coaches.write(f"{coach_id},{name},{date_joined},{date_terminated},RM{wage},{contact},{address},{center_code},{center_name},{sport_code},{sport_name}\n")
                print('*****Successfully added*****')
                coaches.close()
            else:
                print("---  Coach Id already exists ---")
        elif choose == "b":
            no_sport_their = True
            sport_center_name = input("Give a sport's Name: ").strip()
            sport_code = input("Give sports code: ").strip()
            sports = open("data/sports.txt", "r")
        
            for sport in sports:
                if sport.split(",")[1].strip() == sport_center_name:
                    print("*** \n 400 : Sports center already exists \n ***")
                    no_sport_their = False
                    break
            sports.close()
 
            if no_sport_their:
                sports = open("data/sports.txt", "a")
                sports.write(f"{sport_code},{sport_center_name}\n")
                sports.close()
                print(f"***\n Sports : {sport_center_name}  - Successfully added \n***")
        
        elif choose == "c":
            schedules = []
            no_sport_their = True
            
            sport_name = input("Enter sports name: ")
            
            sports = open("data/sports.txt", "r")
            for sport in sports:
                if sport.split(",")[1].strip() == sport_name:
                    no_sport_their = False
            sports.close()
            
            if no_sport_their:
                print("*** \n no Sport's records exists \n ***")
                
            else:
                sports_schedules = open("data/sports_schedules.txt", "r")
                all_sports_schedules = sports_schedules.readlines()
                sports_schedules.close()
                add_sports_schedules = open("data/sports_schedules.txt", "w")
                weekly = int(input("Weekly : "))
                print(f"{weekly} times")
                i = 1
                while 0 < weekly:
                    weekday = input(f"Enter {sport_name}'s {i} day of the week: ")
                    #print(f"added {schedules} into {sport_name}")
                    schedules.append(weekday)
                    weekly -= 1
                    i += 1
                add_sports_schedules.write(f"{sport_name}:{schedules}\n")
                add_sports_schedules.close()
                print(f"{sport_name}:{schedules} is added")
                
        elif choose == "d":
            add_page = _exit()
        else:
            print("no action: choose above chooses only")


def _display():
    display_section = "y"
    while display_section == "y":
        choose = display_records()
        if choose == "a":
            coaches = open("data/coach.txt", "r")
            for coach in coaches:
                print(coach.strip())
            coaches.close()
        elif choose == "b":
            sports = open("data/sports.txt", "r")
            for sport in sports:
                print(sport.strip())
            sports.close()
        elif choose == "c":
            users = open("data/users.txt", "r")
            lines = users.readlines()
            users.close()
            for line in lines:
                if line.split(",")[0].strip() != "admin":
                    print(line.split(",")[0].strip())
        elif choose == "d":
            display_section = _exit()
        else:
            print("no action: choose above chooses only")


def _find():
    search_section = "y"
    while search_section == "y":
        choose = search_records()
        if choose == "a":
            id_does_not_exist = True
            coach_id = input("enter coach ID: ")
            coaches = open("data/coach.txt", "r")
            for coach in coaches:
                if coach.split(",")[0].strip() == coach_id:
                    id_does_not_exist = False
                    print(f"{coach.strip()}")
                    break
            if id_does_not_exist:
                print(f"{coach_id} is not found")
        elif choose == "b":
            is_exist_coach = False
            input_rate = input("Enter search rating: ")
            coaches = open("data/coach.txt", "r").readlines()
            for coach in coaches:
                now_rate = coach.split(",")[11]
                if now_rate.strip() == input_rate:
                    print(coach.strip())
                    is_exist_coach = True
            if not is_exist_coach:
                print("not exist")
            print("------------------------------")
        elif choose == "c":
            code_does_not_exist = True
            sport_code_input = input("Enter sport code: ")
            sports = open("data/sports.txt", "r")
            for sport in sports:
                if sport.split(",")[0].strip() == sport_code_input:
                    code_does_not_exist = False
                    print(f"{sport.strip()}")
                    break
            if code_does_not_exist:
                print(f"{sport_code_input} is not found")
            print("------------------------------")
        elif choose == "d":
            does_not_exist = True
            student_id = input("Enter student ID: ")
            users = open("data/users.txt", "r").readlines()
            for user in users:
                if user.split(",")[8].strip() == student_id:
                    does_not_exist = False
                    print(f"{user.strip()}")
                    break
            if does_not_exist:
                print(f"{student_id} is not found")
            print("------------------------------")
        elif choose == "e":
            search_section = _exit()
        else:
            print("no action: choose above chooses only")


def _sort():
    sort_page = "y"
    while sort_page == "y":
        choose = sort_records()
        if choose == "a":
            sorted_data = nameRatingSort(1)
            for data in sorted_data:
                print(data)
        elif choose == "b":
            sorted_data = priceSort(4)
            for data in sorted_data:
                print(data)
        elif choose == "c":
            sorted_data = nameRatingSort(11)
            for data in sorted_data:
                print(data)
        elif choose == "e":
            sort_page = _exit()
        else:
            print("no action: choose above chooses only")


def _record():
    modify_page = "y"
    while modify_page == "y":
        choose = modify_menu()
        if choose == "a":
            is_exist = False
            coach_id = input("Enter coach's ID: ").strip()
            coaches = open("data/coach.txt", "r")
            for coach_info in coaches:
                if coach_info.split(",")[0].strip() == coach_id:
                    is_exist = True
                    break
            if not is_exist:
                print("404 : coach' ID not found")
            else:
                coaches.close()
                coaches = open("data/coach.txt", "r")
                lines = coaches.readlines()
                coaches.close()
                coaches = open("data/coach.txt", "w")
                coach = ""
                for line in lines:
                    if line.split(",")[0].strip() != coach_id:
                        coaches.write(f"{line.strip()}\n")
                    elif line.split(",")[0].strip() == coach_id:
                        coach = line.strip()
                coach_array = coach.split(",")
                loop = "y"
                while loop == "y":
                    modify_choose = modify_by()
                    if modify_choose == "a":
                        name = input("coach's name: ")
                        coach_array[1] = name
                    elif modify_choose == "b":
                        term = input("coach's date Terminated mm/dd: ")
                        coach_array[3] = term
                    elif modify_choose == "c":
                        wage = input("coach's hourly wage: ")
                        coach_array[4] = wage
                    elif modify_choose == "d":
                        contact = input("coach's contact number: ")
                        coach_array[5] = contact
                    elif modify_choose == "e":
                        address = input("coach's address: ")
                        coach_array[6] = address
                    elif modify_choose == "f":
                        center_code = input("sports center code: ")
                        coach_array[7] = center_code
                    elif modify_choose == "g":
                        center_name = input("sports center name: ")
                        coach_array[8] = center_name
                    elif modify_choose == "h":
                        code = input("coach's sports code: ")
                        coach_array[9] = code
                    elif modify_choose == "i":
                        sports = input("coach's sports: ")
                        coach_array[10] = sports
                    elif modify_choose == "j":
                        loop = _exit()     
                    else:
                        print("no action: choose above chooses only")
                coach = ",".join(coach_array)
                coaches.write(f"{coach.strip()}\n")
                coaches.close()
                print("---------- Coach details successfully modified ----------------")
        elif choose == "b":
            is_exist_sport = False
            sport_name = input("Enter sport name: ").strip()
            sports = open("data/sports.txt", "r")
            for sport in sports:
                if sport.split(",")[1].strip() == sport_name:
                    is_exist_sport = True
                    print(f"------ {sport_name} Modify info. -----")
            if not is_exist_sport:
                print("404 : sport name not found")
            else:
                sports.close()
                sport_input_menu = input("a. modify \nb. delete\nEnter character: ")
                sports = open("data/sports.txt", "r")
                lines = sports.readlines()
                sports.close()
                if sport_input_menu == "a":
                    new_sport_input = input("Enter new sport name: ").strip()
                    sports = open("data/sports.txt", "w")
                    for line in lines:
                        if line.split(",")[1].strip() != sport_name:
                            sports.write(f"{line.strip()}\n")
                        elif line.split(",")[1].strip() == sport_name:
                            sports.write(f"{line.split(',')[0]},{new_sport_input}")
                    sports.close()
                elif sport_input_menu == "b":
                    sports = open("data/sports.txt", "w")
                    for line in lines:
                        if line.split(",")[0].strip() != sport_input_menu:
                            sports.write(f"{line.strip()}\n")
                    sports.close()
            print("---------- sport details successfully changes applied ----------------")
            
        elif choose == "c":
            is_exist_sport = False
            sport_name = input("Enter sport name: ").strip()
            sports = open("data/sports.txt", "r")
            for sport in sports:
                if sport.split(",")[0].strip() == sport_name and sport.split(",")[1].strip() != "":
                    is_exist_sport = True
                    print(sport)
            if is_exist_sport:
                print("404: sport schedules not found")
            
            else:
                sports.close()
                sport_input_menu = input("a. modify\nb. delete\nEnter character: ")
                sports = open("data/sports_schedules.txt", "r")
                lines = sports.readlines()
                sports.close()
                if sport_input_menu == "a":
                    new_schedule = []
                    new_num_input = int(input("how many days a week : "))
                    i = 0
                    while i < new_num_input:
                        input_schedule = input(f"Enter {i + 1} day of the week : ")
                        new_schedule.append(input_schedule)
                        i += 1
                    sports = open("data/sports_schedules.txt", "w")
                    for line in lines:
                        if line.split(",")[0].strip() != sport_name:
                            sports.write(f"{line.strip()}\n")
                        elif line.split(",")[0].strip() == sport_name:
                            sports.write(f"{line.split(',')[0]}:{new_schedule}\n")
                    sports.close()
                    
                elif sport_input_menu == "b":
                    sports = open("data/sports_schedules.txt", "w")
                    for line in lines:
                        if line.split(",")[0].strip() != sport_name:
                            sports.write(f"{line.strip()}\n")
                    sports.write(f"{sport_name}\n")
                    sports.close()
            print("finish")
        elif choose == "e":
            modify_page = _exit()
        else:
            print("no action: choose above options only")

def admin_chooses():
    page = "y"
    while page == "y":
        choose = admin_page()
        if choose == '1':
            add()
        elif choose == '2':
            _display()
        elif choose == '3':
            _find()
        elif choose == '4':
            _sort()
        elif choose == '5':
            _record()
        elif choose == '6':
            page = _exit()
        else:
            print("Incorrect option")
