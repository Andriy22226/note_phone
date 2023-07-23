from main_phone_book import CLIPhoneBookAssistant
from main_note_book import CLINoteBookAssistant
from main_sorter import CLISorterAssistant


CLI_pb_assist = CLIPhoneBookAssistant()


def bot_help():
    return "You can work with the following options:\n" \
          "- Phone Book -> please enter number '1' \n" \
          "- Note Book -> please enter number '2'\n" \
          "- Exit from Bot -> please enter number '0'\n"


bot_command_dict = {
    "1": CLI_pb_assist.run_phone_assistant,
    "2": CLINoteBookAssistant.run_notes_assistant,
    # "3": CLISorterAssistant.run_sorter_assistant,

    "#": bot_help,
    }


def personal_assistant():

    print("Welcome to your personal assistant based on CLI bot!\n")
    print("""You can work with the following options:
    - Phone Book -> please enter number '1'
    - Note Book -> please enter number '2'
    - to see all commands again -> please enter '#'
    - to Exit from Bot -> please enter number '0'
    """)

    while True:
        command = input("Please enter number of option (from 0 to 2 or #): ").strip()

        if command == "0":
            raise SystemExit("\nThank you for using CLI Bot assistant.\nSee you later! Take care of yourself!\n")

        elif command in bot_command_dict.keys():
            handler = bot_command_dict[command]
            answer = handler()
            print(answer)

        else:
            print("Incorrect input.\nPlease check and enter correct command (or '#' to help).")


if __name__ == "__main__":
    personal_assistant()

