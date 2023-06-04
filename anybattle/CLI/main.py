from rich import print
from ..engine import genCharacter, genNemesis
import guidance

def cli():
    guidance.llm = guidance.llms.OpenAI('text-curie-001')

    print("[bold red]Lets fight!!![/bold red]")
    example_character = "A red wizard wielding a sword and a shield."
    print(f"[bold green]Describe your character.[/bold green]\n[yellow]Example: [italic]{example_character}[/italic][/yellow]")
    character = input(">>>")

    char_prof = genCharacter(description=character)
    print(char_prof)

    nemesis = genNemesis(description=character)
    print(nemesis)

    nemesis_prof = genCharacter(description=nemesis)
    print(nemesis_prof)