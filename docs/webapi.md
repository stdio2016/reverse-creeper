# Web API

Some information is from https://knucklecracker.com/wiki/doku.php?id=web_apis.

## Get map list
Creeper World 1, 2 has no get map list API. For newer games, the following URL can get the list of custom maps. The result is a Gzip compressed XML.

* Creeper World 3: https://knucklecracker.com/creeperworld3/queryMaps.php?query=maplist
* Particle Fleet: https://knucklecracker.com/particlefleet/queryMaps.php?query=maplist
* Creeper World 4: https://knucklecracker.com/creeperworld4/queryMaps.php?query=maplist
* Creeper World IXE: https://knucklecracker.com/creeperworldixe/queryMaps.php?query=maplist


## Download map thumbnail
Replace `{GUID}` with the map GUID, or in Creeper World 1 and 2, Map ID. Thumbnail is JPEG format.

* Creeper World 1: https://knucklecracker.com/creeperworld/thumb.php?id={GUID} (no CORS header)
* Creeper World 2: https://knucklecracker.com/creeperworld2/thumb.php?id={GUID} (no CORS header)
* Creeper World 3: https://knucklecracker.com/creeperworld3/queryMaps.php?query=thumbnail&guid={GUID}
* Particle Fleet: https://knucklecracker.com/particlefleet/queryMaps.php?query=thumbnail&guid={GUID}
* Creeper World 4: https://knucklecracker.com/creeperworld4/queryMaps.php?query=thumbnail&guid={GUID}
* Creeper World IXE: https://knucklecracker.com/creeperworldixe/queryMaps.php?query=thumbnail&guid={GUID}


## Download map
Replace `{GUID}` with the map GUID, or in Creeper World 1 and 2, Map ID.

* Creeper World 1: https://knucklecracker.com/creeperworld/mapdownload.php?id={GUID} (no CORS header)
* Creeper World 2: https://knucklecracker.com/creeperworld2/mapdownload.php?id={GUID} (no CORS header)
* Creeper World 3: https://knucklecracker.com/creeperworld3/queryMaps.php?query=map&guid={GUID}
* Particle Fleet: https://knucklecracker.com/particlefleet/queryMaps.php?query=map&guid={GUID}
* Creeper World 4: https://knucklecracker.com/creeperworld4/queryMaps.php?query=map&guid={GUID}
* Creeper World IXE: https://knucklecracker.com/creeperworldixe/queryMaps.php?query=map&guid={GUID}
