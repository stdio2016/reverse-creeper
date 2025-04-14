# Creeper World 1

## Map file format
Map file is `.cwm`. It is a Zlib compressed XML.

Root tag is `<game>`. It contains the following tags:
* `<version>`: string. The latest editor version is `0380`.
* `<terrain>`: Contains the following tags:
  - `<terrainHeight>`: Comma-separated list of integers 1 to 5, like `1,2,3,1,5`. It has 3360=70x48 items.  
    Item index is [x + y*80], x from left to right, y from top to bottom
  - `<edgeSize>`: int from 0 to 10
  - `<tint1>`, `<tint2>`, `<tint3>`, `<tint4>`, `<tint5>`: Terrain level 1 to 5 tint, can be a float number from 0 to 2
* `<walls>`: Contains only one tag:
  - `<wallData>`: Comma separated list of integers 0, 1 or 1000000. 0 means no wall, 1 means normal wall, 1000000 means Crazonium wall.
* `<background>`: Contains only one tag:
  - `<backgroundMap>`: int from 0 to 5
* `<places>`: first occurence of `<places>` is an empty tag, seems to workaround some old game bugs
* `<specialplaces>`: Contains the following tags:
  - `<BaseGun>`: Odin city
  - `<Rift>`: Rift location
* `<places>`: Contains any number of `<Totem>` tags.
* `<emitters>`: Contains any number of `<emitter>` tags.
* `<upgrades>`: Contains any number of `<Upgrade>` tags.
* `<pods>`: Contains any number of `<SurvivalPod>` tags.
* `<ruins>`: Contains any number of `<Ruin>` tags. Ruin means artifact in game.
* `<collectors>`: Contains any number of `<Collector>` tags.
* `<relays>`: Contains any number of `<Relay>` tags.
* `<storage>`: Contains any number of `<Storage>` tags.
* `<speed>`: Contains any number of `<Speed>` tags.
* `<reactors>`: Contains any number of `<Reactor>` tags.
* `<blasters>`: Contains any number of `<Blaster>` tags.
* `<mortars>`: Contains any number of `<Mortar>` tags.
* `<sams>`: Contains any number of `<Sam>` tags.
* `<drones>`: Contains any number of `<Drone>` tags.
* `<mines>`: Contains any number of `<Mine>` tags.
* `<techs>`: Contains any number of `<Tech>` tags.
* `<sporewaves>`: Contains any number of `<SporeWave>` tags.
* `<tech>`: Contains all of the following tags. Tags are true/false indicating whether the technology is available.
  - `<collector>`, `<relay>`, `<storage>`, `<speed>`, `<reactor>`
  - `<blaster>`, `<mortar>`, `<sam>`, `<drone>`, `<thor>`
* `<player>`: Contains the following tags:
  - `<energycolor>`: Energy zone color
  - `<lockedcity>`: boolean. If true, Odin city cannot move
* `<creeper>`: Contains the following tags:
  - `<color>`: Creeper color
  - `<mistColor1>`: Mist color
  - `<mistColor2>`: Mist accent color
* `<title>`: string. Map title
* `<opening>`: string. Opening text
* `<custombackground>`: Base64 encoded background image. Tag only appears when the map has custom background.


Contents of `<BaseGun>` and `<Rift>`:
* `<gameSpaceX>`: integer from 0 to 69, left is 0, right is 69
* `<gameSpaceY>`: integer from 0 to 47, top is 0, bottom is 47
* `<health>`: Unused in custom map, always 0
* `<energyLevel>`: Unused in custom map, always 0

Contents of `<emitter>`:
* `<gameSpaceX>`: integer
* `<gameSpaceY>`: integer
* `<startTime>`: integer, start time in frames
* `<frequency>`: integer, interval in frames
* `<intensity>`: floating-point number. Negative intensity will not spread

Contents of `<Ruin>`:
* `<gameSpaceX>`: integer
* `<gameSpaceY>`: integer
* `<desc>`: URL-encoded string. Artifact text.

Contents of `<Totem>`, `<Upgrade>`, `<SurvivalPod>`, `<Collector>`, `<Relay>`, `<Storage>`, `<Speed>` and `<Reactor>`:
* `<gameSpaceX>`: integer
* `<gameSpaceY>`: integer

Contents of `<Blaster>`, `<Mortar>`, `<Sam>`, `<Drone>`:
* `<gameSpaceX>`: integer
* `<gameSpaceY>`: integer
* `<armed>`: boolean. Indicates whether the unit is fully armed.
* `<locked>`: boolean. Indicates whether the unit is initially locked.

Contents of `<SporeWave>`:
* `<time>`: integer, time in frames
* `<count>`: integer
* `<intensity>`: floating-point number.
* `<side>`: one of top, bottom, left, right

Contents of `<Tech>`:
* `<gameSpaceX>`: integer
* `<gameSpaceY>`: integer
* `<tech>`: integer from 0 to 9 corresponding to collector, relay, storage, speed, reactor, blaster, mortar, SAM, drone and Thor.

Color is an integer calculated as `r * 65536 + g * 256 + b`.

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
