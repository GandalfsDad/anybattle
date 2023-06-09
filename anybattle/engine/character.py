import guidance

def genCharacter(description):
    genChar = guidance("""The following is a character profile for an RPG game in JSON format.
    The range of values for health is 0-100.
    The range of values for attack, defense, spattack, and spdefense is 0-25 .
    ```json
    {
        "description": "{{description}}",
        "name": "{{gen 'name'}}",
        "attack": {{gen 'attack' stop=','}},
        "defense": {{gen 'defense'  stop=','}},
        "health": {{gen 'health'  stop=','}},
        "spattack": {{gen 'spattack'  stop=','}},
        "spdefense": {{gen 'spdefense'  stop='\\n'}},
        "items": [{{#geneach 'items' num_iterations=3}}
            "{{gen 'this'}}",{{/geneach}}
        ]
    }```""")

    result = genChar(description=description)
    return {k:V for k,V in result.variables().items() if k != 'llm'}

def genNemesis(description):
    genNem = guidance("""The following is a description of an RPG character:
    {{description}}
    Here is a description of an equally powerful nemesis:
    {{gen 'nemesis'}}
    """)

    result = genNem(description=description)
    return result['nemesis']