import streamlit as st
from src.main import TicTacToe

st.set_page_config(page_title="Tic Tac Toe", layout="centered")
st.title("Tic Tac Toe")

# Initialize session state
if "game" not in st.session_state:
    st.session_state.game = TicTacToe()
    st.session_state.game.choose_starting_player()

game = st.session_state.game

# Display current player
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if game.winner:
        if game.winner == 'Draw':
            st.success("🤝 It's a Draw!")
        else:
            st.success(f"🎉 Player {game.winner.upper()} wins!")
    else:
        st.info(f"Current Player: {game.current_player.upper()}")

# Draw the board with buttons
st.write("### Click a cell to make your move")
board_cols = st.columns(3)

for i in range(3):
    with board_cols[i]:
        for j in range(3):
            pos = i * 3 + j + 1
            cell_value = game.board[pos] if game.board[pos] != ' ' else ''
            
            # Button styling based on cell value
            if cell_value == 'x':
                btn_color = '🔵'
            elif cell_value == 'o':
                btn_color = '❌'
            else:
                btn_color = '⬜'
            
            if st.button(f"{btn_color}", key=f"cell_{pos}", use_container_width=True):
                if not game.winner and game.board[pos] == ' ':
                    game.apply_move(pos)
                    if not game.check_winner():
                        game.switch_turn()
                    st.rerun()

# Reset button
st.divider()
if st.button("🔄 New Game", use_container_width=True):
    st.session_state.game = TicTacToe()
    st.session_state.game.choose_starting_player()
    st.rerun()
