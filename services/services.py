from models.models import Player, Stats, Match, Training, Recruit, Equipment, Post, Poll, Tournament
from models.observers.notification_observer import NotificationObserver 
from models.singletons.data_manager import get_data_manager 
from services.factories.match_factory import MatchFactory
from services.factories.training_factory import TrainingFactory
from services.builders.player_builders import PlayerConcreteBuilder 
from services.builders.player_director import PlayerDirector


def add_player():
    try:
        builder = PlayerConcreteBuilder()
        director = PlayerDirector(builder)
        director.construct_full_player()

    except (ValueError, TypeError) as e:
        print(f"\nError registering player: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}") 


def list_players():
    data_manager = get_data_manager()
    if not data_manager.players:
        print("\nNo players registered in the system.")
        return

    print("\n----- Players List -----")
    for player in data_manager.players:
        print(f"ID: {player.id} | Name: {player.name} | Age: {player.age} | "
              f"Position: {player.position} | Health Status: {player.health}")
        print("-" * 90)

def find_player_by_id(player_id, data_manager):
    for player in data_manager.players:
        if player.id == player_id:
            return player
    return None

def edit_player():
    data_manager = get_data_manager()
    try:
        search_id = int(input("Enter player ID to edit: "))
        player = find_player_by_id(search_id, data_manager) 

        if not player:
            print("Player not found.")
            return

        print(f"\nEditing Player: {player.name} (ID: {player.id})")
        new_name = input(f"New name (or press Enter to keep '{player.name}'): ")
        new_position = input(f"New position (or press Enter to keep '{player.position}'): ")

        if new_name.strip():
            player.name = new_name
        if new_position.strip():
            player.position = new_position

        print("\nEdit Stats (press Enter to keep current values):")
        new_score_str = input(f"Goals (Current: {player.stats.score}): ")
        new_games_str = input(f"Games (Current: {player.stats.games_played}): ")

        if new_score_str.strip():
            player.stats.score = int(new_score_str) 
        if new_games_str.strip():
            player.stats.games_played = int(new_games_str) 
        
        print("\nPlayer updated successfully.")

    except (ValueError, TypeError) as e:
        print(f"\nError updating player: {e}")

def remove_player():
    data_manager = get_data_manager()
    try:
        search_id = int(input("Enter player ID to remove: "))
        player = find_player_by_id(search_id, data_manager)

        if player:
            data_manager.players.remove(player)
            print("Player removed successfully.")
        else:
            print("Player not found.")
    except ValueError:
        print("\nInvalid ID. Please enter a number.")

def schedule_match():
    try:
        date = input("Enter match date (DD/MM/YYYY): ")
        time = input("Enter match time: ")
        location = input("Enter match location: ")
        
        factory = MatchFactory()
        factory.create_event(date, time, location)

    except (ValueError, TypeError) as e:
        print(f"\nError scheduling match: {e}")

def schedule_training():
    try:
        date = input("Enter training date (DD/MM/YYYY): ")
        time = input("Enter training time: ")
        location = input("Enter training location: ")
        
        factory = TrainingFactory()
        factory.create_event(date, time, location)
        
    except (ValueError, TypeError) as e:
        print(f"\nError scheduling training: {e}")

def schedule_tournament():
    data_manager = get_data_manager()
    try:
        date = input("Enter tournament start date (DD/MM/YYYY): ")
        time = input("Enter tournament start time: ")
        location = input("Enter tournament location: ")
        name = input("Enter tournament name: ")

        new_tournament = Tournament(date, time, location, name)

        # Adicionar algumas partidas ao torneio (exemplo)
        match1 = Match(date, "10:00", "Team A", location)
        match2 = Match(date, "12:00", "Team B", location)
        new_tournament.add_event(match1)
        new_tournament.add_event(match2)
        
        # Adiciona o Torneio (que é um Event) à lista principal de eventos
        data_manager.events.append(new_tournament)
        print("\nTournament scheduled successfully.")

    except (ValueError, TypeError) as e:
        print(f"\nError scheduling tournament: {e}")

def list_events():
    data_manager = get_data_manager()
    if not data_manager.events:
        print("\nNo events registered.")
        return

    print("\n----- Events List -----")
    for event in data_manager.events:
        print(event.details())
        print("-" * 100)

def performance_tracking():
    data_manager = get_data_manager()
    if not data_manager.players:
        print("\nNo players registered.")
        return

    print("\n----- Player Performance Report -----")
    for player in data_manager.players:
        try:
            goals_per_game = player.stats.score / player.stats.games_played
        except ZeroDivisionError:
            goals_per_game = 0
        
        print(f"ID: {player.id} | Name: {player.name} | Goals per Game Average: {goals_per_game:.2f}")
    print("-" * 90)

def get_current_balance():
    data_manager = get_data_manager()
    return data_manager.account.balance

def add_recruit():
    data_manager = get_data_manager()
    try:
        name = input("Name: ")
        age = int(input("Age: "))
        pros = input("Strengths: ")
        cons = input("Weaknesses: ")
        position = input("Position: ")
        observation = input("Observation: ")
        
        recruit = Recruit(name, age, pros, cons, position, observation)
        data_manager.recruits.append(recruit)
        print("\nRecruit added successfully.")
    except (ValueError, TypeError) as e:
        print(f"\nError adding recruit: {e}")

def add_equipment():
    data_manager = get_data_manager()
    try:
        name = input("Name: ")
        eq_type = input("Type: ")
        quantity = int(input("Quantity: "))
        status = input(f"Status ({', '.join(Equipment.VALID_STATUSES)}): ")
        observation = input("Observations: ")
        
        new_equipment = Equipment(name, eq_type, quantity, status, observation)
        data_manager.equipments.append(new_equipment)
        print("\nEquipment added successfully.")
    except (ValueError, TypeError) as e:
        print(f"\nError adding equipment: {e}")

def register_income():
    data_manager = get_data_manager()
    try:
        value = float(input("Income value: "))
        data_manager.account.add_income(value) 
        print("Income registered successfully.")
    except (ValueError, TypeError) as e:
        print(f"\nError registering income: {e}")

def register_expense():
    data_manager = get_data_manager()
    try:
        value = float(input("Expense value: "))
        data_manager.account.add_expense(value) 
        print("Expense registered successfully.")
    except (ValueError, TypeError) as e:
        print(f"\nError registering expense: {e}")

def create_poll():
    data_manager = get_data_manager()
    try:
        title = input("Poll title: ")
        desc = input("Description: ")
        opt1 = input("Option 1: ")
        opt2 = input("Option 2: ")
        opt3 = input("Option 3 (optional): ")
        
        poll = Poll(title, desc, opt1, opt2, opt3)
        data_manager.polls.append(poll)

        observer = NotificationObserver()
        poll.attach(observer)
        poll.notify()

        print("\nPoll created successfully.")
    except (ValueError, TypeError) as e:
        print(f"\nError creating poll: {e}")

def create_post():
    data_manager = get_data_manager()
    try:
        title = input("Post title: ")
        content = input("Content: ")
        date = input("Date (DD/MM/YYYY): ")
        
        post = Post(title, content, date)
        data_manager.posts.append(post)

        observer = NotificationObserver()
        post.attach(observer)
        post.notify()

        print("\nPost created successfully.")
    except (ValueError, TypeError) as e:
        print(f"\nError creating post: {e}")

def list_equipments():
    data_manager = get_data_manager()
    if not data_manager.equipments:
        print("\nNo equipment registered.")
        return
    print("\n----- Equipment List -----")
    for eq in data_manager.equipments:
        print(f"Name: {eq.name} | Type: {eq.type} | Quantity: {eq.quantity} | "
              f"Status: {eq.status} | Observation: {eq.observation}")
        print("-"*90)

def list_injured_players():
    data_manager = get_data_manager()
    print("\n----- Injured Players List -----")
    injured_found = False
    for player in data_manager.players:
        if player.health.lower() != 'healthy':
            print(f" #{player.id} - {player.name} (Status: {player.health})")
            injured_found = True
    if not injured_found:
        print("No players are currently injured.")
    print("-"*30)

def list_polls():
    data_manager = get_data_manager()
    if not data_manager.polls:
        print("\nNo polls created.")
        return
    print("\n----- Polls List -----")
    for p in data_manager.polls:
        print("-"*90)
        print(f"Poll: {p.title} | {p.description} \n[1] {p.opt1} [2] {p.opt2} [3] {p.opt3}")
        print("-"*90)

def list_posts():
    data_manager = get_data_manager()
    if not data_manager.posts:
        print("\nNo posts created.")
        return
    print("\n----- Posts List -----")
    for post in data_manager.posts:
        print("-"*90)
        print(f"Post: {post.title} | {post.date}\n{post.content}\n")
        print("-"*90)

def list_recruits():
    data_manager = get_data_manager()
    if not data_manager.recruits:
        print("\nNo recruits registered in the system.")
        return

    print("\n----- Recruits List -----")
    for recruit in data_manager.recruits:
        print(f"Name: {recruit.name} | Age: {recruit.age} | Position: {recruit.position}")
        print(f"  Strengths: {recruit.pros}")
        print(f"  Weaknesses: {recruit.cons}")
        print(f"  Observation: {recruit.observation}")
        print("-" * 90)

def delete_event():
    data_manager = get_data_manager()
    if not data_manager.events:
        print("\nNo events registered to delete.")
        return

    print("\nCurrent Events:")
    list_events() 

    try:
        event_id_to_delete = int(input("\nEnter the ID of the event to delete: "))
        
        event_to_delete = None
        for event in data_manager.events:
            if event.id == event_id_to_delete:
                event_to_delete = event
                break
        
        if event_to_delete:
            data_manager.events.remove(event_to_delete)
            print("Event deleted successfully.")
        else:
            print("Error: Event with the specified ID not found.")

    except ValueError:
        print("\nError: Invalid ID. Please enter a number.")

def register_result():
    data_manager = get_data_manager()
    matches = [event for event in data_manager.events if isinstance(event, Match)]
    
    if not matches:
        print("\nNo matches scheduled to register results for.")
        return

    print("\nCurrent Matches:")
    for match in matches:
        print(match.details())  
    print("-" * 100)

    try:
        match_id_to_update = int(input("\nEnter the ID of the match to update: "))
        
        match_found = False
        for event in data_manager.events:
            if isinstance(event, Match) and event.id == match_id_to_update:
                match_found = True
                new_result = input(f"Enter the result for the match against {event.opponent}: ")
                
                if new_result.strip():
                    event.result = new_result 
                    print("Match result updated successfully.")
                else:
                    print("No changes made. Result cannot be empty.")
                break
        
        if not match_found:
            print("Error: Match with the specified ID not found.")

    except ValueError:
        print("\nError: Invalid ID. Please enter a number.")

def delete_post():
    data_manager = get_data_manager()
    if not data_manager.posts:
        print("\nNo posts to delete.")
        return

    print("\nCurrent Posts:")
    list_posts() 

    try:
        title_to_delete = input("\nEnter the exact title of the post to delete: ")

        post_to_delete = None
        for post in data_manager.posts:
            if post.title == title_to_delete:
                post_to_delete = post
                break
        
        if post_to_delete:
            data_manager.posts.remove(post_to_delete)
            print("Post deleted successfully.")
        else:
            print("Error: Post with the specified title not found. Verify and try again.")

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

def delete_poll():
    data_manager = get_data_manager()
    if not data_manager.polls:
        print("\nNo polls to delete.")
        return

    print("\nCurrent Polls:")
    list_polls()

    try:
        title_to_delete = input("\nEnter the title of the poll to delete: ")

        poll_to_delete = None
        for poll in data_manager.polls:
            if poll.title == title_to_delete:
                poll_to_delete = poll
                break
        
        if poll_to_delete:
            data_manager.polls.remove(poll_to_delete)
            print("Poll deleted successfully.")
        else:
            print("Error: Poll with the specified title not found. Verify and try again.")
            
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")