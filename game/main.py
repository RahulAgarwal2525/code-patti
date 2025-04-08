print("✅ main.py started")

from game_engine import Game
from bot import Bot
from rules import Rules
from playerSubmitted import Player  # <- Import player submission

def main():
    game = Game()
    bot = Bot(player_id=1)
    player = Player(player_id=0)  # <- Create instance of player code
    while True:
        state = game.get_game_state()
        current_player = state["current_player"]
        top_card = state["top_card"]

        print("\n---------------------------")
        print(f"Top card on pile: {top_card}")
        print(f"Your cards: {game.players[0]}")
        print(f"Bot has {len(game.players[1])} cards.")

        if current_player == 0:
            # Use player's bot logic
            player_move = player.choose_card(game.players[0], top_card)
            print(f"Player plays: {player_move if player_move else 'draws a card'}")
            if player_move:
                game.play_turn(0, player_move, player)
            else:
                game.play_turn(0)

            #human game 
            # top_card = game.played_cards[-1] if game.played_cards else None

            # move = input("Enter the card to play (or 'draw' to pick a card): ").strip().upper()

            # if move == "DRAW":
            #     drawn_card = game.deck.draw_card()
            #     player_hand.append(drawn_card)
            #     print(f"Player {current_player} drew {drawn_card}.")
            #     if game.play_turn(0, move, player):  # try to play drawn card
            #         continue
            #     else:
            #         print("No playable card drawn. Turn ends.")

            # elif move in player_hand:
            #     success = game.play_turn(0, move, player)
            #     if not success:
            #         print("Invalid move. Card cannot be played.")
            #     else:
            #         continue
            # else:
            #     print("Invalid input! Try again.")
            #     continue

        else:
            # Predefined bot turn
            bot_move = bot.choose_card(game.players[1], top_card)
            print(f"Bot plays: {bot_move if bot_move else 'draws a card'}")
            if bot_move:
                game.play_turn(1, bot_move, bot)
            else:
                game.play_turn(1)

        # Check for winner
        if game.check_winner():
            break

if __name__ == "__main__":
    main()
