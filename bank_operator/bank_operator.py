from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from bank_operator import bank_operator

console = Console()

def menu():
    while True:
        console.clear()

        table = Table(title="\U0001F3E6 Bank System Menu", title_style="bold magenta")

        table.add_column("Option", style="cyan", justify="center")
        table.add_column("Description", style="white")

        table.add_row("1", "Create User")
        table.add_row("2", "List Users")
        table.add_row("3", "Add Account")
        table.add_row("4", "Deposit")
        table.add_row("5", "Withdraw")
        table.add_row("6", "View Transactions")
        table.add_row("7", "Exit")

        console.print(table)

        choice = Prompt.ask("\U0001F449 Choose option", choices=[str(i) for i in range(1, 8)], default="7")

        if choice == '1':
            bank_operator.create_user()
        elif choice == '2':
            bank_operator.list_users()
        elif choice == '3':
            if not bank_operator.users:
                console.print("[red]No users available. Please create a user first.[/red]")
                Prompt.ask("Press Enter to continue")
                continue
            bank_operator.create_account()
        elif choice == '4':
            if not bank_operator.users:
                console.print("[red]No users available. Please create a user first.[/red]")
                Prompt.ask("Press Enter to continue")
                continue
            if not bank_operator.deposit_money():
                console.print("[red]Deposit failed. Please try again.[/red]")
                Prompt.ask("Press Enter to continue")
        elif choice == '5':
            if not bank_operator.users:
                console.print("[red]No users available. Please create a user first.[/red]")
                Prompt.ask("Press Enter to continue")
                continue
            if not bank_operator.withdraw_money():
                console.print("[red]Withdrawal failed. Please try again.[/red]")
                Prompt.ask("Press Enter to continue")
        elif choice == '6':
            if not bank_operator.users:
                console.print("[red]No users available. Please create a user first.[/red]")
                Prompt.ask("Press Enter to continue")
                continue
            bank_operator.view_transactions()
        elif choice == '7':
            console.print("\n\U0001F44B Exiting... Thank you for using the Bank System!", style="bold green")
            break

if __name__ == "__main__":
    menu()
