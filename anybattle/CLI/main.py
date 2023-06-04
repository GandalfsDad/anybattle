from rich import print
from ..engine import genCharacter, genNemesis, genBattleScene, genMoveResults, genNemesisMove
from .format import printCharacterStats, printBattleScene
import guidance

def cli():
    guidance.llm = guidance.llms.OpenAI('text-curie-001')
    guidance.llms.OpenAI.cache.clear()

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

    scene = genBattleScene(character=character, nemesis=nemesis)
    printBattleScene(scene)

    while True:
        print("[bold green] describe your move.[/bold green]")
        move = input(">>>")
        impact = genMoveResults(move=move, character=character, nemesis=nemesis)
        print(f"Your Move: {impact}")

        nemesis_move = genNemesisMove(move=move, character=character, nemesis=nemesis)
        print(f"Nemesis' Move: {nemesis_move}")
        nemesis_impact = genMoveResults(move=nemesis_move, character=nemesis, nemesis=character)
        print(f"Nemesis' Move Impact: {nemesis_impact}")