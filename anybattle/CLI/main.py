from rich import print
from ..engine import genCharacter, genNemesis
from .format import printCharacterStats
import guidance

def cli():
    guidance.llm = guidance.llms.OpenAI('text-curie-001')

    print("[bold red]Lets fight!!![/bold red]")
    example_character = "A red wizard wielding a sword and a shield."
    print(f"[bold green]Describe your character.[/bold green]\n[yellow]Example: [italic]{example_character}[/italic][/yellow]")
    character = input(">>>")

    char_prof = genCharacter(description=character)
    print("[bold red]Your character stats:[/bold red]")
    printCharacterStats(char_prof)

    print("[bold red]Your Nemesis:[/bold red]")
    nemesis = genNemesis(description=character)
    print(nemesis)

    print("[bold red]Your Nemesis' stats:[/bold red]")
    nemesis_prof = genCharacter(description=nemesis)
    printCharacterStats(nemesis_prof)