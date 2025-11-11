import streamlit as st
from rock_paper_scissors import Rock_Papaer_Scissors


def determine_result(player_choice):
    game = Rock_Papaer_Scissors()
    comp_choice = game.get_computer_choice()
    result = game.get_winner(player_choice, comp_choice)
    return comp_choice, result


def main():
    st.title('Rock Paper Scissors')
    st.write('Choose your move and play against the computer')

    choices = ['rock', 'paper', 'scissors']
    player = st.radio('Your move', choices)

    if st.button('Play'):
        comp_choice, result = determine_result(player)
        st.info(f'Computer chose: {comp_choice}')
        if 'tie' in result.lower():
            st.write("It's a tie!")
        elif 'won' in result.lower():
            if 'congratulation' in result.lower():
                st.success('You win!')
            else:
                st.error(result)
        else:
            st.write(result)


if __name__ == '__main__':
    main()
