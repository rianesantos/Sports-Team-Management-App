import services.services as sv
from services.commands.list_players_command import ListPlayersCommand
from services.commands.add_player_command import AddPlayerCommand
from services.commands.edit_player_command import EditPlayerCommand     
from services.commands.remove_player_command import RemovePlayerCommand
from services.commands.save_players_command import SavePlayersCommand
from services.strategies.list_all_events_strategy import ListAllEventsStrategy # type: ignore
from services.strategies.list_matches_strategy import ListMatchesStrategy # type: ignore
from services.facades.social_media_facade import SocialMediaFacade
from services.facades.financial_facade import FinancialFacade

# Inicializa os Facades para uso nas funções do menu
social_media_facade = SocialMediaFacade()
financial_facade = FinancialFacade()


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
    # USANDO O PADRÃO COMMAND
    while True:
        print("\nPlayers Management Menu")
        print("1. Add Player")
        print("2. List Players")
        print("3. Edit Player")
        print("4. Remove Player")
        print("5. Manage Recruits")
        print("6. Save Players Data (Adapter)") # NOVA OPÇÃO
        print("0. Back")
        option = input("Choose an option: ")

        if option == "1":
            AddPlayerCommand().execute()
        elif option == "2":
            ListPlayersCommand().execute()
        elif option == "3":
            EditPlayerCommand().execute()
        elif option == "4":
            RemovePlayerCommand().execute()
        elif option == "5":
            manage_player_recruitment()
        elif option == "6":
            SavePlayersCommand().execute() # CHAMA O NOVO COMANDO/ADAPTER
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
    # USANDO O PADRÃO STRATEGY (para listagem)
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
    # USANDO O PADRÃO FACADE (FinancialFacade)
    print("\nFinancial Management")
    while True:
        # Usa o Facade para obter o saldo, que internamente usa o serviço.
        print(f"\nCurrent Balance: $ {financial_facade.get_current_balance():.2f}")
        print("1. Register Income")
        print("2. Register Expense")
        print("0. Back")
        option = input("Choose an option: ")

        if option == "1":
            financial_facade.register_income()
        elif option == "2":
            financial_facade.register_expense()
        elif option == "0":
            break
        else:
            print("Invalid option.")

def media_and_social():
    # USANDO O PADRÃO FACADE (SocialMediaFacade)
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
            social_media_facade.create_poll()
        elif option == "2":
            social_media_facade.create_post()
        elif option == "3":
            social_media_facade.list_polls()
        elif option == "4":
            social_media_facade.list_posts()
        elif option == "5":
            social_media_facade.delete_poll()
        elif option == "6":
            social_media_facade.delete_post()
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