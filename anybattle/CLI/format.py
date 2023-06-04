from rich import print

def printCharacterStats(stats):
    toPrint = ['health','attack','defense','spattack','spdefense']
    printable = {k:V.strip() for k,V in stats.items() if k in toPrint}
    print('|'.join([f"[bold blue]{k}[/bold blue]: {(stats[k]).strip()}" for k in printable]))
    print(f"[bold blue]items[/bold blue]: {', '.join(stats['items'])}")

def printBattleScene(scene):
    print('[bold red]Scene of the battle[/bold red]:')
    print(f"[italic yellow]{scene}[/italic yellow]")