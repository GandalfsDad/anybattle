import guidance

def genBattleScene(character, nemesis):
    genScene = guidance("""The following is a description of two characters:
    {{character}}
    {{nemesis}}
    
    The following is a simple description of the location of the battle.
    {{gen 'scene' max_tokens=250 temperature=0}}
    """)
    result = genScene(character=character, nemesis=nemesis)
    return result['scene']
