########################################################################################################################
screen fortmap:
    modal True
    use diary_nav
    imagemap:
        ground loadImage("screen_bg_map.png")
        hover  loadImage("screen_bg_map_selected.png")
        idle   loadImage("screen_bg_map_unavailable.png")

        if fortmap.contains_area("rowe"):
            hotspot (945, 85, 85, 75) clicked Return(1)
        if fortmap.contains_area("kilgour"):
            hotspot (827, 175, 205, 37) clicked Return(2)
        if fortmap.contains_area("rquad"):
            hotspot (840, 80, 100, 45) clicked Return(3)
        if fortmap.contains_area("library"):
            hotspot (784, 123, 115, 33) clicked Return(4)
        if fortmap.contains_area("gym"):
            hotspot (730, 104, 60, 83) clicked Return(5)
        if fortmap.contains_area("food"):
            hotspot (650, 160, 90, 35) clicked Return(6)
        if fortmap.contains_area("valley"):
            hotspot (350, 150, 250, 170) clicked Return(7)
        if fortmap.contains_area("oval"):
            hotspot (320, 305, 350, 190) clicked Return(8)
        if fortmap.contains_area("currycourts"):
            hotspot (225, 507, 203, 163) clicked Return(9)
        if fortmap.contains_area("bcourts"):
            hotspot (500, 500, 200, 180) clicked Return(10)
        if fortmap.contains_area("carpark"):
            hotspot (700, 480, 186, 202) clicked Return(11)
        if fortmap.contains_area("fortstreet"):
            hotspot (890, 475, 72, 207) clicked Return(12)
        if fortmap.contains_area("bridge"):
            hotspot (1225, 325, 126, 60) clicked Return(13)
        if fortmap.contains_area("place"):
            hotspot (1080, 240, 108, 119) clicked Return(14)
        if fortmap.contains_area("wilkins"):
            hotspot (966, 273, 95, 77) clicked Return(15)
        if fortmap.contains_area("quad"):
            hotspot (910, 320, 62, 56) clicked Return(16)
        if fortmap.contains_area("cohen"):
            hotspot (755, 405, 133, 54) clicked Return(17)
        if fortmap.contains_area("hall"):
            hotspot (800, 305, 102, 88) clicked Return(18)
        if fortmap.contains_area("lquad"):
            hotspot (775, 245, 103, 55) clicked Return(19)
        if fortmap.contains_area("lkilgour"):
            hotspot (660, 225, 117, 67) clicked Return(20)
        if fortmap.contains_area("uqad"):
            hotspot (890, 220, 108, 56) clicked Return(21)