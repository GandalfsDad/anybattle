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

def genMoveResults(move, character, nemesis):
    
    genImpact = guidance("""The following is a description of two characters in an RPG game:
    CharacterA:
    {{character}}
    CharacterB:
    {{nemesis}}

    The following is a move made by CharacterA:
    {{move}}

    This results in the following damage to characterB:
    ```{
          'damage':{{gen 'impact' stop=',' temperature=0.0 max_tokens=10}} 
        }```
    """)

    result = genImpact(move=move, character=character, nemesis=nemesis)

    return result['impact']

def genNemesisMove(move, character, nemesis):
    
    genMove = guidance("""The following is a description of two characters in an RPG game:
    CharacterA:
    {{nemesis}}
    CharacterB:
    {{character}}

    The following is a move made by CharacterB:
    {{move}}

    This caused the following impact on CharacterA:
    {{gen 'impact' temperature=0.0 max_tokens=100}}

    After this move CharecterA does the following:
    {{gen 'nemesis_move' temperature=0.0 max_tokens=100}}
    """)

    result = genMove(move=move, character=character, nemesis=nemesis)

    return f"{result['impact']}{result['nemesis_move']}"

