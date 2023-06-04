from rich import print

def cli():
    print("[bold red]Lets fight!!![/bold red]")

    example_charector = "A red wizard wielding a sword and a shield."
    print(f"[bold green]Describe your charector.[/bold green]\n[yellow]Example: [italic]{example_charector}[/italic][/yellow]")
    charector = input(">>>")