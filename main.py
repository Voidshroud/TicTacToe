import customtkinter
from player import Player

gameplay_board = []
board_state = []
player_one = None
player_two = None
current_player = None
remaining_moves = 0


def button_play_singleplayer():
    pass
    # main_menu_frame.forget()
    # gameplay_frame.pack()
    # create_gameplay_board()


def button_play_multiplayer():
    global player_one
    global player_two
    player_one = Player("X", False)
    player_two = Player("O", False)
    main_menu_frame.forget()
    gameplay_frame.pack()
    create_gameplay_board()


def button_return():
    restart_gameplay_board()
    gameplay_frame.forget()
    main_menu_frame.pack()


def button_exit():
    app.destroy()


def create_gameplay_board():
    global gameplay_board
    global board_state
    global current_player
    global remaining_moves
    gameplay_board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    board_state = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    current_player = player_one
    remaining_moves = 9

    for i in range(3):
        for j in range(3):
            gameplay_board[i][j] = customtkinter.CTkButton(gameplay_frame,
                                                           height=200, width=200, fg_color="black",
                                                           corner_radius=0, border_width=5, border_color="green",
                                                           text="", font=("Helvetica", 100),
                                                           command=lambda r=i, c=j: clicked(r, c))
            gameplay_board[i][j].grid(row=i+1, column=j)

    gameplay_label.configure(text=f"Player '{current_player.sign}' turn.")
    gameplay_label.grid(row=0, column=1)


def restart_gameplay_board():
    restart_btn.grid_forget()
    create_gameplay_board()


def clicked(r, c):
    global current_player
    global remaining_moves
    remaining_moves -= 1
    board_state[r][c] = current_player.sign
    if current_player == player_one:
        gameplay_board[r][c].configure(text=f"{current_player.sign}")
        check_victory()
        current_player = player_two
    else:
        gameplay_board[r][c].configure(text=f"{current_player.sign}")
        check_victory()
        current_player = player_one

    try:
        gameplay_label.configure(text=f"Player '{current_player.sign}' turn.")
    except:
        pass


def check_victory():
    global current_player
    global remaining_moves

    for i in range(3):
        if board_state[i][0] == board_state[i][1] == board_state[i][2] != 0:
            gameplay_label.grid_forget()
            restart_btn.configure(text=f"Winner is {current_player.sign}. Restart?")
            restart_btn.grid(row=0, column=1)
            break

        elif board_state[0][i] == board_state[1][i] == board_state[2][i] != 0:
            gameplay_label.grid_forget()
            restart_btn.configure(text=f"Winner is {current_player.sign}. Restart?")
            restart_btn.grid(row=0, column=1)
            break

        elif board_state[0][0] == board_state[1][1] == board_state[2][2] != 0:
            gameplay_label.grid_forget()
            restart_btn.configure(text=f"Winner is {current_player.sign}. Restart?")
            restart_btn.grid(row=0, column=1)
            break

        elif board_state[0][2] == board_state[1][1] == board_state[2][0] != 0:
            gameplay_label.grid_forget()
            restart_btn.configure(text=f"Winner is {current_player.sign}. Restart?")
            restart_btn.grid(row=0, column=1)
            break

        elif remaining_moves == 0:
            gameplay_label.grid_forget()
            restart_btn.configure(text=f"Tie. Restart?")
            restart_btn.grid(row=0, column=1)
            break


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x660")

main_menu_frame = customtkinter.CTkFrame(app, width=600, height=660)
main_menu_frame.pack()
gameplay_frame = customtkinter.CTkFrame(app, width=600, height=660)

warning_label = customtkinter.CTkLabel(master=main_menu_frame,
                                       text="AI implementation pending. Please use Multiplayer option.",
                                       text_color="red")
warning_label.place(relx=0.5, rely=0.15, anchor=customtkinter.CENTER)
play_singleplayer_btn = customtkinter.CTkButton(master=main_menu_frame, text="Singleplayer",
                                                command=button_play_singleplayer)
play_singleplayer_btn.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

play_multiplayer_btn = customtkinter.CTkButton(master=main_menu_frame, text="Multiplayer",
                                               command=button_play_multiplayer)
play_multiplayer_btn.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)

exit_btn = customtkinter.CTkButton(master=main_menu_frame, text="Exit",
                                   command=button_exit)
exit_btn.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

return_btn = customtkinter.CTkButton(master=gameplay_frame, text="Return",
                                     command=button_return)
return_btn.grid(row=4, column=1)

restart_btn = customtkinter.CTkButton(master=gameplay_frame,
                                      command=restart_gameplay_board)

gameplay_label = customtkinter.CTkLabel(master=gameplay_frame)

app.mainloop()
