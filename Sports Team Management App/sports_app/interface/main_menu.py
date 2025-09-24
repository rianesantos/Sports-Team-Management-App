import services.services as sv
from commands.list_players_command import ListPlayersCommand
from commands.add_player_command import AddPlayerCommand
from commands.edit_player_command import EditPlayerCommand     
from commands.remove_player_command import RemovePlayerCommand
from services.strategies.list_all_events_strategy import ListAllEventsStrategy
from services.strategies.list_matches_strategy import ListMatchesStrategy

def manage_player_recruitment():
    print("\nRecruits Management")
    while True:
        print("1. Add Recruit")
        print("2. List Recruits")
        print("0. Back")
        choice = input("Choose an option: ")

        if choice == "1":
            sv.add_recruit()
        elif choice == "2":
            sv.list_recruits()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

def manage_players():
    while True:
        print("\nPlayers Management Menu")
        print("1. Add Player")
        print("2. List Players")
        print("3. Edit Player")
        print("4. Remove Player")
        print("5. Manage Recruits")
        print("0. Back")
        option = input("Choose an option: ")

        if option == "1":
            add_player_cmd = AddPlayerCommand()
            add_player_cmd.execute()
        elif option == "2":
            list_players_cmd = ListPlayersCommand()
            list_players_cmd.execute()
        elif option == "3":
            edit_player_cmd = EditPlayerCommand()
            edit_player_cmd.execute()
        elif option == "4":
            remove_player_cmd = RemovePlayerCommand()
            remove_player_cmd.execute()
        elif option == "5":
            manage_player_recruitment()
        elif option == "0":
            break
        else:
            print("Invalid option.")

def team_management():
    while True:
        print("\nTeam Management Menu")
        print("1. Manage Players")
        print("2. Performance Tracking")
        print("3. Health Monitoring")
        print("0. Back")
        option = input("Choose an option: ")
        
        if option == "1":
            manage_players()
        elif option == "2":
            sv.performance_tracking()
        elif option == "3":
            health_monitoring()
        elif option == "0":
            break
        else:
            print("Invalid option.")

def schedule_event():
    while True:
        print("\nEvents Management Menu")
        print("1. Schedule Match")
        print("2. Schedule Training")
        print("3. List All Events")
        print("4. List only Matches")
        print("5. Remove Event") 
        print("6. Add Match Result")
        print("0. Back")
        option = input("Choose an option: ")

        if option == "1":
            sv.schedule_match()
        elif option == "2":
            sv.schedule_training()
        elif option == "3":
            strategy = ListAllEventsStrategy()
            sv.list_events(strategy)
        elif option == "4":
            strategy = ListMatchesStrategy()
            sv.list_events(strategy)
        elif option == "5":
             sv.delete_event() 
        elif option == "6":
             sv.register_result()
        elif option == "0":
            break
        else:
            print("Invalid option.")

def health_monitoring():
    while True:
        print("\nHealth Monitoring")
        print("1. List Injured Players")
        print("0. Back")
        option = input("Choose an option: ").strip()

        if option == "1":
            sv.list_injured_players()
        elif option == "0":
            break
        else:
            print("Invalid option.")

def manage_equipments():
    print("\nEquipment Management")
    while True:
        print("1. Add Equipment")
        print("2. List Equipment")
        print("0. Back")
        choice = input("Choose an option: ")

        if choice == "1":
            sv.add_equipment()
        elif choice == "2":
            sv.list_equipments()
        elif choice == "0":
            break
        else:
            print("Invalid option.")

def manage_finances():
    print("\nFinancial Management")
    while True:
        print(f"\nCurrent Balance: $ {sv.data.account.balance:.2f}")
        print("1. Register Income")
        print("2. Register Expense")
        print("0. Back")
        option = input("Choose an option: ")

        if option == "1":
            sv.register_income()
        elif option == "2":
            sv.register_expense()
        elif option == "0":
            break
        else:
            print("Invalid option.")

def media_and_social():
    print("\nMedia and Public Relations")
    while True:
        print("1. Create Poll")
        print("2. Create Post")
        print("3. List Polls")
        print("4. List Posts")
        print("5. Delete Poll")
        print("6. Delete Post")
        print("0. Back")
        option = input("Choose an option: ")

        if option == "1":
            sv.create_poll()
        elif option == "2":
            sv.create_post()
        elif option == "3":
            sv.list_polls()
        elif option == "4":
            sv.list_posts()
        elif option == "5":
            sv.delete_poll()
        elif option == "6":
            sv.delete_post()
        elif option == "0":
            break
        else:
            print("Invalid option.")

def main_menu():
    while True:
        print("\n----- Sports Team Management App -----")
        print("Select an option:")
        print("1. Manage Team and Players")
        print("2. Manage Matches and Training")
        print("3. Manage Equipment")
        print("4. Manage Finances")
        print("5. Media and Social")
        print("0. Exit")
        option = input("Choose an option: ")

        if option == "1":
            team_management()
        elif option == "2":
            schedule_event()
        elif option == "3":
            manage_equipments()
        elif option == "4":
            manage_finances()
        elif option == "5":
            media_and_social()
        elif option == "0":
            print("Closing system.")
            break
        else:
            print("Invalid option.")