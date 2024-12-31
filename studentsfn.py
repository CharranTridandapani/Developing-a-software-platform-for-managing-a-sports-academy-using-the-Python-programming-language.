def studentOption():
   choose = input(
        "1. All Coaches \n"
        "2. Your Profile \n"
        "3. Your Sport Schedule only\n"
        "4. Edit your profile \n"
        "5. Provide feedback to Coach.\n"
        "6. exit \n"
        "Choose a character: ").strip()
   return choose


def edit_menu():
   choose = input(
        "------------ Edit your details ------------\n"
        "1. your name\n"
        "2. your gender\n"
        "3. your age\n"
        "4. your sports\n"
        "5. your address\n"
        "6. your contact\n"
        "7. your e-mail\n"
        "8. exit\n"
        "Choose a character: ")

   return choose
  
def _exit():
    section = "n"
    return section
  
def coaches():
    coaches = open("data/coach.txt", "r")
    lines = coaches.readlines()
    for coach_info_data in lines:
        print(coach_info_data)


def your_profile(name):
    users = open("data/users.txt", "r")
    lines = users.readlines()
    users.close()
    for user_line in lines:
        user_data = user_line.split(",")
        if user_data[0] == name:
            print(user_line)
            break


def schedule_details(name):
    users_info = open("data/users.txt", "r")
    users = users_info.readlines()
    users_info.close()
    currentUser = ""
    for user in users:
        if user.split(",")[0] == name.strip():
            currentUser = user
            break
    schedules = open("data/sports_schedules.txt","r")
    lines = schedules.readlines()
    schedules.close()

    for data in lines:
       if currentUser.split(',')[4] == data.split(":")[0]:
          print(data)

def edit_your_profile(name): 
    users_file = open("data/users.txt", "r")
    lines = users_file.readlines()
    users_file.close()
    users_file = open("data/users.txt", "w")
    user = ""
    for line in lines:
        line_array = line.split(",")
        if line_array[0].strip() != name.strip():
            users_file.write(f"{line.strip()}\n")
        elif line_array[0].strip() == name.strip():
             user = line.strip()
             user_array = user.split(",")
             edit_page = "y"
             while edit_page == "y":
                choose= edit_menu()
                if choose == "1":
                    user_array[0] = input("name: ").strip()
                elif choose== "2":
                    gender = input("gender: ").strip()
                    user_array[2] = gender
                elif choose== "3":
                    age = input("age: ").strip()
                    user_array[3] = age
                elif choose== "4":
                    sports = input("sport: ").strip()
                    user_array[4] = sports
                elif choose== "5":
                    address = input("address: ").strip()
                    user_array[5] = address
                elif choose== "6":
                    phone = input("contact: ").strip()
                    user_array[6] = phone
                elif choose== "7":
                    email = input("e-mail: ").strip()
                    user_array[7] = email
                elif choose== "8":
                    edit_page = _exit()
             user = ",".join(user_array) 
             users_file.write(f"{user.strip()}\n")
             print("Successfully added info.")
    users_file.close()

   
def index_in_list(a_list, index):
   return index < len(a_list)
        
def coach_rating():
    is_exist_coach = False
    coach_name = input("please enter your coach: ").strip()
    score = int(input("please enter score: "))
    if 1 > score or score > 5:
        print("invalid number (1 <= score <= 5)")
    else:
        coach_info_file = open("data/coach.txt", "r")
        lines = coach_info_file.readlines()
        coach_info_file.close()
        coach_info_file = open("data/coach.txt", "w")
                     
        coach = ""
        for line in lines:
            line_array = line.split(",")
            if line_array[1].strip() != coach_name:
                coach_info_file.write(f"{line.strip()}\n")
            elif line_array[1].strip() == coach_name:
                coach = line.strip()
                is_exist_coach = True
       
        if not is_exist_coach:
            print("this coach not found")
        else:
            coach_array = coach.split(",")
            if index_in_list(coach_array, 11):
                old_score = float(coach_array[11])
            else:
                old_score = 0
                coach_array.append(0)
            if not index_in_list(coach_array,12):
                coach_array.append(0)
            voted_num = int(coach_array[12])
            new_score = (old_score * voted_num + score)/(voted_num+1)
            coach_array[11] = str(new_score)
            coach_array[12] = str(int(coach_array[12])+1)
            coach = ",".join(coach_array)
            coach_info_file.write(f"{coach.strip()}\n")
            print('**** Thanks for your rating ****')
        coach_info_file.close()


def student_func(name):
    studentPage = "y"
    while studentPage == "y":
       student_option = studentOption()
       if student_option == '1':
           coaches()
       elif student_option == '2':
           your_profile(name)
       elif student_option == '3':
           schedule_details(name)
       elif student_option == '4':
           edit_your_profile(name)
       elif student_option == '5':
           coach_rating()
       elif student_option == '6':
           studentPage = _exit()
       else:
           print("Incorrect option")        
