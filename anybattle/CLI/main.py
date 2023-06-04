from rich import print
from ..engine import genCharector, genNemesis
import guidance

def cli():
    guidance.llm = guidance.llms.OpenAI('text-davinci-003')

    print("[bold red]Lets fight!!![/bold red]")
    example_charector = "A red wizard wielding a sword and a shield."
    print(f"[bold green]Describe your charector.[/bold green]\n[yellow]Example: [italic]{example_charector}[/italic][/yellow]")
    charector = input(">>>")

    char_prof = genCharector(description=charector)
    print(char_prof)

    nemesis = genNemesis(description=charector)
    print(nemesis)

    nemesis_prof = genCharector(description=nemesis)
    print(nemesis_prof)