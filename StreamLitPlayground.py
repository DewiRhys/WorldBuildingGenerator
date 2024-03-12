# streamlit run "C:\Users\dewir\OneDrive\Documents\Digital Futures\Python\Streamlit\StreamLitPlayground.py"

import streamlit as st
import pandas as pd
import numpy as np

import random
import re

words = {
    'adjopinion': [['good'], ['great'], ['awful'], ['bad'], ['unwelcoming'], ['cool'], ['warm'], ['hot'], ['cold'], ['beautiful'], ['ugly']],
    'adjsize': [['big'], ['huge'], ['medium-sized'], ['small'], ['tiny']],
    'adjphysical': [['untidy'], ['pristine'], ['clean'], ['fluffy'], ['smooth'], ['jagged'], ['wiry']],
    'adjage': [['old'], ['new'], ['ancient'], ['young'], ['aged']],
    'adjcolour': [['green'], ['blue'], ['yellow'], ['purple'], ['red'], ['orange'], ['gold'], ['silver'], ['black'], ['white'], ['rainbow']],
    'adjmaterial': [['stone'], ['wood'], ['living'], ['metal'], ['sand'], ['rock'], ['marble'], ['mahogany'], ['glass'], ['leather']],
    'verbing': [['jumping'], ['playing'], ['standing'], ['whistling'], ['sleeping'], ['eating'], ['yawning'], ['floating']],
    'verbed': [['jumped'], ['played'], ['stood'], ['whistled'], ['slept'], ['ate'], ['yawned'], ['floated']],
    'verb': [['jump'], ['play'], ['stand'], ['whistle'], ['sleep'], ['eat'], ['yawn'], ['float']],
    'creature': [['owlbear'], ['owl'], ['bear'], ['dragon']],
    'object': [['chair'], ['door'], ['candle']],
    'region': [['desert'], ['meadow'], ['forest'], ['mountain'], ['cave'], ['beach'], ['plain'], ['cliff'], ['jungle'], ['tundra'], ['taiga'], ['floodplain'], ['atoll'], ['valley'], ['hill']],
    'building': [['cabin'], ['castle'], ['tower'], ['fort'], ['library'], ['wall'], ['monument'], ['temple dedicated to', '@genholyfigure'], ['statue of', '@gencharacter']],
    'feature': [['river'], ['tree'], ['mound'], ['pile of', '@adjmaterial'], ['stone', 'circle'], ['corpse of', '?an', '@creature'], ['corpse of', '?an', '@race'], ['ruin']],
    'concept': [['nature'], ['fire'], ['water'], ['earth'], ['food'], ['joy'], ['honour'], ['sex'], ['death'], ['life'], ['chance']],
    'genholyfigure': [['@concept'], ['the god of', '@concept'], ['the god of', '@concept', 'and', '@concept']],
    'shop': [['bakery'], ['butcher\'s'], ['alchemist\'s']],
    'martialclass': [['bard'], ['paladin'], ['monk'], ['barbarian'], ['fighter'], ['ranger']],
    'magicclass': [['wizard'], ['druid'], ['sorcerer'], ['cleric'], ['artificer'], ['warlock']],
    'race': [['human'], ['elf'], ['orc'], ['ogre'], ['halfling'], ['fairy'], ['dragonborn'], ['aasimar'], ['aarakocra'], ['warforged'], ['kalashtar']],
    'genshop': [['?an', '@adjopinion', '@adjage', '@shop'], ['?an', '@adjopinion', '@adjmaterial', '@shop'], ['?an', '@adjage', '@adjmaterial', '@shop']],
    'genbuilding': [['?an', '@adjopinion', '@adjage', '@building'], ['?an', '@adjopinion', '@adjmaterial', '@shop'], ['?an', '@adjage', '@adjmaterial', '@building']],
    'genregion': [['?an', '@adjsize', '@region'], ['?an', '@adjcolour', '@region'], ['?an', '@adjphysical', '@region']],
    'genfeature': [['?an', '@adjopinion', '@feature'], ['?an', '@adjsize', '@feature'], ['?an', '@adjage', '@feature'], ['?an', '@adjcolour', '@feature']],
    'genlocation': [['@genregion', 'in which', '@genbuilding', 'stands'], ['@genregion', 'featuring', '@genfeature']],
    'gencreature': [['?an', '@adjsize', '@creature'], ['?an', '@adjcolour', '@creature']],
    'gennpc': [['?an', '@adjage', '@race']],
    'genclass': [['@martialclass'], ['@magicclass'], ['multiclassed', '@martialclass', '@magicclass']],
    'gencharacter': [['?an', '@adjage', '@genclass', '@race']],
    'genperson': [['@gennpc'], ['@gencharacter']],
    'gendescription': [['You see', '@genlocation', '.'], ['You see', '@genlocation', '.', '@genadddescription']],
    'genencounter': [['You see', '@gencreature', '@verbing', '.'], ['You see', '@genperson', '@verbing', '.']],
    'genadddescription': [['There is', '@genshop', 'run by', '@gennpc', '.'], ['There is', '@genshop', 'run by', '@gennpc', 'who is', '@verbing', '.'], ['You see', '@genperson', 'and', '@genperson', '@verbing', 'by', '@genfeature', '.']]
}


def get_random(lst):
    i = random.randint(0, len(lst) - 1)
    return lst[i]


def insert_position(position, list1, list2):
    return list1[:position] + list2 + list1[position:]

def Generate_World():
    main_list = ['@gendescription', '@genencounter']

    ongoing = True

    while ongoing == True:
        ongoing = False
        for i in range(len(main_list)):
            if main_list[i][0] == '@':
                ongoing = True
                pull_list_index = main_list[i][1:]
                main_list.pop(i)
                add_list = get_random(words[pull_list_index])
                main_list = insert_position(i, main_list, add_list)
                break

    for i in range(len(main_list)):
        if main_list[i][0] == '?':
            if main_list[i] == '?an':
                if main_list[i + 1][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                    main_list[i] = 'an'
                else:
                    main_list[i] = 'a'

    sentence = " ".join(main_list)
    sentence = re.sub(r' \.', '.', sentence)

    return sentence

# Set the page title
st.markdown('<p style="color:#f9f2eb; font-size: 60px;">World Building Generator</p>', unsafe_allow_html=True)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {'#440f2b'};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

submitted = st.button('Generate')
if submitted:
    generatedWorld = Generate_World()
    st.markdown(f'<p style="color:#f9f2eb; font-size: 40px;">{generatedWorld}</p>', unsafe_allow_html=True)