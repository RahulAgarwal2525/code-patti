from game_engine import Game
from playerBot import Player as PlayerBot
from practice_bot import PracticeBot


def main():
    game = Game()

    bots = {
        0: PlayerBot(0),
        1: PracticeBot(1),
        2: PracticeBot(2),
        3: PracticeBot(3)
    }

    for pid, bot in bots.items():
        bot.receive_cards([game.deck.draw_card() for _ in range(7)])
        game.players[pid] = bot

    game.turn_order = list(bots.keys())
    # game.current_player = game.turn_order[0]
    game.played_cards.append(game.deck.draw_card())
    print(f"Game Start — Top card: {game.played_cards[-1]}")

    round_counter = 0
    while True:
        current_player = game.current_player
        bot = game.players[current_player]
        top_card = game.played_cards[-1]

        print(f"\n🔁 Turn: Player {current_player} — Hand: {bot.hand}")
        print(f"Top Card: {top_card}")

        move = bot.choose_card(top_card)
        if move:
            print(f"Player {current_player} plays: {move} current direction: {game.dir}")
            winner = game.play_turn(current_player, move, bot)
            if winner is not None:
                print(f"🏁 Game Over — Player {winner} wins!")
                break
        else:
            print(f"Player {current_player} has no move, drawing...")
            winner = game.play_turn(current_player, None, bot)
            if winner is not None:
                print(f"🏁 Game Over — Player {winner} wins!")
                break

        round_counter += 1
        if round_counter > 5000:
            print("❌ Game stopped after 500 turns — possible bot deadlock.")
            break


if __name__ == "__main__":
    main()
