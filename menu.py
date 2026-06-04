import userrecord
import activityclass
import stress_analysis

def main():
    while True:
        print("Menu")
        print("1. User")
        print("2. Activity")
        print("3. Stress Report")
        print("4. Exit")
        print()
        choice=int(input("Enter choice\t"))
        if choice==1:
            print("User menu")
            print("1. Add User")
            print("2. Display User")
            print("3. Search User")
            print("4. Update User")
            print("5. Delete User")
            print()
            ch=int(input("Enter choice\t"))
            if ch==1:
                userrecord.add_user_data()
            elif ch==2:
                userrecord.display_userrecord_data()
            elif ch==3:
                uid=input('enter user id:')
                userrecord.search_userrecord_by_id(uid)
            elif ch==4:
                uname=input('enter username')
                userrecord.update_userrecord(uname)
            elif ch==5:
                uid=input('enter user id:')
                userrecord.user_delete(uid)
            


        elif choice==2:
            print("1. Add Activity Data")
            print("2. Display All Activity")
            print("3. Search Activity")
            print("4. Update Activity")
            print("5. Delete Activity")
            print()
          

            ch = int(input("Enter your choice: "))

            if ch == 1:
                activityclass.add_activity_data()
            elif ch == 2:
                activityclass.display_activity_data()
            elif ch == 3:
                aid=input('enter activity id')
                activityclass.search_activity_data(aid)
            elif ch == 4:
                aid=input('Enter activity id')
                activityclass.update_activity_data(aid)
            elif ch == 5:
                aid=input('Enter activity id')
                activityclass.delete_activity_data(aid)

        elif choice==3:
            print("1. Add Stress Report")
            print("2. Display Stress Report")
            print("3. Update Stress Report")
            print("4. Delete Stress Report")
            print()

            ch=int(input("enter choice"))

            if ch==1:
                stress_analysis.add_record_stress_analysis()
            elif ch==2:
                stress_analysis.display_record_stress_analysis()
            elif ch==3:
                stress_analysis.update_record_stress_analysis()
            elif ch==4:
                stress_analysis.delete_record_stress_analysis()
            
        
        elif choice==4:
            print('exiting program')
            break

main()
