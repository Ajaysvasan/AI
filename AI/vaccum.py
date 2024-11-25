def vaccum_world():
    goal_state = {'A':'0','B':'0'}
    cost = 0
    location_input = input("Enter the location of the Vaccum cleaner: ")
    status_input = input("Enter the status: ")
    complement_status = input("Enter the complement status: ")
    if location_input == 'A':
        print("Vaccum is present at location A")
        if status_input == '1':
            print("The room is empty")
            goal_state['A'] = 0
            cost+=1
            print(f"The cost for cleaning A is {cost}")
            print("Location has been cleaned")
            if complement_status == '1':
                print("Moving to room B")
                cost+=1
                print("Room B is empty")
                goal_state['B'] = 0
                cost+=1
                print(f"The cost of cleaning location B is {cost}")
                print("Location B has been cleaned")
            else:
                print("Moving to room B")
                cost+=1
                print("Room is clean")
        else:
            print("The room is clean")
            print(f"The cost is {cost}")
            if complement_status == '1':
                print("Moving to room B")
                cost+=1
                print("Room B is empty")
                goal_state['B'] = 0
                cost+=1
                print(f"The cost of cleaning location B is {cost}")
                print("Location B has been cleaned")
            else:
                print("Moving to room B")
                cost+=1
                print("Room is clean")
    else:
        print("Vaccum is present at location B")
        if status_input == '1':
            print("The room is empty")
            goal_state['B'] = 0
            cost+=1
            print(f"The cost for cleaning B is {cost}")
            print("Location has been cleaned")
            if complement_status == '1':
                print("Moving to room B")
                cost+=1
                print("Room A is empty")
                goal_state['A'] = 0
                cost+=1
                print(f"The cost of cleaning location A is {cost}")
                print("Location A has been cleaned")
            else:
                print("Moving to room B")
                cost+=1
                print("Room is clean")
        else:
            print("The room is clean")
            print(f"The cost is {cost}")
            if complement_status == '1':
                print("Moving to room B")
                cost+=1
                print("Room A is empty")
                goal_state['A'] = 0
                cost+=1
                print(f"The cost of cleaning location A is {cost}")
                print("Location A has been cleaned")
            else:
                print("Moving to room B")
                cost+=1
                print("Room is clean")
    print(f"Goal State:\n{goal_state}")
    print(f"Performance measurement: {cost}")

if __name__ == "__main__":
    vaccum_world()