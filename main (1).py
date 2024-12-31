
import adminfn
import studentsfn
def home():
    choose = input(
        "1. admin login\n"
        "2. student login\n"
        "3. admin register\n"
        "4. student register\n"
        "5. sports details\n"
        "6. sports schedule\n"
        "Enter number: ")
    return choose


def start():
    print("***** Dashboard Real Champions Sports Academy *****")
    homeMenu = "I"
    while homeMenu == "I":
        choose = home()
        if choose == "1":
            is_admin = False
            admin_data = open("data/admin.txt", "r")
            users = admin_data.readlines()
            admin_data.close()
            if len(users) > 0:
                name = input("Username: ").strip()
                password = input("password: ").strip()
                for user in users:
                    user = user.split(',')
                    user_name = user[0].strip()
                    user_password = user[1].strip()
                    if name == user_name and password == user_password:
                        print('********admin login successful********')
                        adminfn.admin_chooses()
                        is_admin = True
                        break
                if not is_admin:
                    print("No Admin Found")
            else:
                print("Please register a new admin -- no admins")

        elif choose == "2":
            is_user = False
            name = input("Username: ").strip()
            password = input("password: ").strip()
            users_data = open("data/users.txt", "r")
            users = users_data.readlines()
            users_data.close()
            for user in users:
                user = user.split(',')
                user_name = user[0].strip()
                user_password = user[1].strip()
                if name == user_name and password == user_password:
                    print(f"******** Welcome to Real Champions Sports Academy *********\n")
                    studentsfn.student_func(user_name)
                    is_user = True
                    break
            if not is_user:
                print("No user found")
        
        elif choose == "3":
            is_admin = False
            new_admin_name = input("please enter admin name:").strip()
            admin_data = open("data/admin.txt", "r")
            admins = admin_data.readlines()
            admin_data.close()
            for admin in admins:
                if admin.split(',')[0] == new_admin_name:
                    is_admin = True
                    break
            if is_admin:
                print("Already this admin name existed")
                
            else:
                password = input("Set password:").strip()
                admin_data = open("data/admin.txt", "a")
                admin_data.write(f"{new_admin_name},{password}\n")
                admin_data.close()
                print('successfully new admin added')    
            
        elif choose == "4":
            is_user = False
            new_user_name = input("please enter your name: ").strip()
            users = open("data/users.txt", "r")
            count = 0
            for user in users:
                if user.split(",")[0] == new_user_name:
                    print("You can add this user name. already existed!!")
                    is_user = True
                    count += 1
            if not is_user:
                new_user = ''
                users.close()
                new_user_pass = input("please enter your password: ").strip()
                user_gender = input("please enter your gender: ").strip()
                user_age = input("please enter your age: ").strip()
                user_sport = input("please enter your sport: ").strip()
                user_address = input("please enter your address: ").strip()
                user_contact = input("please enter your contact: ").strip()
                user_email = input("please enter your mail: ").strip()
                users = open("data/users.txt", "a")
                new_user = f"{new_user_name},{new_user_pass},{user_gender},{user_age},{user_sport},{user_address},{user_contact},{user_email},TS{count}"
                users.write(f"{new_user}\n")
                users.close()

                print(f"{new_user} (msg : details successfully Registered)")
            
        elif choose == "5":
            sports = open("data/sports.txt", "r")
            print("**********Sports Records**********")
            for sport in sports:
                print(f"{sport}\n")
            print("----------------------------------")
            sports.close()
                
        elif choose == "6":
            is_exists = False
            sports = open("data/sports_schedules.txt", "r")
            print("***********Sports Schedules*************")
            for sport in sports:
                print(sport.strip())
                is_exists = True
            if not is_exists:
                print("No schedules exists")
            print("--------------------------------------")
            sports.close()
        else:
            print("Incorrect option")

start()
