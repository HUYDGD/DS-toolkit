init python:
    # Multi Game Persistent Character Names
    # Recommended: male_fname, male_sname, female_fname, female_sname, futa_fname, futa_sname, other_fname or other_sname (or any, or all of these).
    # Other recommendations: bigsis_fname, lilsis_fname, bigbro_fname, lilbro_fname, mom_fname, dad_fname, malebff_fname or femalebff_fname. (Again, use any or use none).
    mp_ndata = MultiPersistent("namedata.f95zone.to")

# https://github.com/DRincs-Productions/DS-toolkit/wiki/Information#renaming_mc
label renaming_mc:
    # allow default name(s) to be saved across multiple games
    if renpy.variant("pc"):
        if mp_ndata.male_fname != None:
            $ mcI.set("name_default", mp_ndata.male_fname)
        if mp_ndata.male_sname != None:
            $ mcI.set("sname_default", mp_ndata.male_sname)

    "Player" "My name is:"
    $ mcI.changeName()
    "Player" "My surname is:"
    $ mcI.changeSurname()

    if renpy.variant("pc"):
        if mcI.name != mcI.get("name_default"):
            $ mp_ndata.male_fname = mcI.name
        if mcI.sname != mcI.get("sname_default"):
            $ mp_ndata.male_sname = mcI.sname
        $ mp_ndata.save()
    return
