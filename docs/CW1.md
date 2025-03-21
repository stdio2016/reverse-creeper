# Creeper World 1

## Map file format
Map file is `.cwm`. It is a Zlib compressed XML.

Root tag is `<game>`. It contains the following tags:
* `<version>`: string
* `<terrain>`
* `<walls>`
* `<background>`
* `<places>`: first occurence of `<places>` is an empty tag, seems to workaround some old game bugs
* `<specialplaces>`
* `<places>`
* `<emitters>`
* `<upgrades>`
* `<pods>`
* `<ruins>`
* `<collectors>`
* `<relays>`
* `<storage>`
* `<speed>`
* `<reactors>`
* `<blasters>`
* `<mortars>`
* `<sams>`
* `<drones>`
* `<mines>`
* `<techs>`
* `<sporewaves>`
* `<tech>`
* `<player>`
* `<creeper>`
* `<title>`: string. Map title
* `<opening>`: string. Opening text
* `<custombackground>`: Base64 encoded background image. Tag only appears when the map has custom background.

## Save directory
- `#airversion/`: Folder contains an empty file representing Adobe Air version.
- `customgames/`: All imported custom maps
  - `*.cwm`: File name is 8 random lowercase alphabets.
- `Local Store/`: Empty directory. Seems unused
- `gameData.dat`: RC4 Encrypted and Zlib compressed XML.
- `gameState.dat`: AMF serialized format of an object.
- `workingmap.cwm`: Map imported from map editor using "Deploy Working Map To Game" feature. Click "Launch Your Custom Game" in game to play.

## gameData.dat

Root tag is `<games>`. It contains the following tags:
* `<playerName>`: string
* `<groupName>`: string
* `<muteMainMusic>`: true/false
* `<musicVolume>`: float number 0 to 1
* `<mistEffects>`: true/false
* `<particleEffects>`: true/false
* `<unchartedGames>`: Chronom missions. Contains any number of `<IndividualGame>` tags.
* `<specialGames>`: Special Ops missions. Contains 10 `<IndividualGame>` tags, each with gameNumber 0 to 9.
* `<randomGames>`: Conquest missions. Contains 25 `<IndividualGame>` tags, each with gameNumber 1 to 25.
* `<storyGames>`: Story missions. Contains 20 `<IndividualGame>` tags, each with gameNumber 0 to 19.
* `<customGames>`: Custom maps. Contains any number of `<IndividualGame>` tags.

Contents of `<IndividualGame>`:
* `<gameNumber>`: int, or -1 if custom map or Chronom mission
* `<gameName>`
    - If custom map, File name `*.cwm` in `customgames/` folder.
    - If Chronom mission, days since January 1, 0000, 0-based (This number is not correct due to buggy date implementation)
    - Otherwise, this tag does not exist
* `<highScore>`: int, or 0 if not beaten
* `<lastScore>`: int, or 0 if not beaten
* `<minTime>`: int. Play time in frames (36 frames per second), or 0 if not beaten
* `<playCount>`: int, or 0 if not beaten
* `<lastPlayed>`: number, as javascript epoch, or 0 if not beaten
* `<scoreSubmitted>`: javascript epoch of submission time, or 0 if not submitted

## gameState.dat
AMF3 format object
* `windowDisplayState`: string (normal/maximized)
* `windowBounds`: many members exists, however only the following are used
    - `x`: int
    - `y`: int
    - `width`: int
    - `height`: int
