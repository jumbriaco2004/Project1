from direct.showbase.ShowBase import ShowBase

class SpaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()

    def SetupScene(self):
        
        #Setting Universe
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.obj")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        UniverseTexture = self.loader.loadTexture("./Assets/Universe/starfield-in-blue.jpg")
        self.Universe.setTexture(UniverseTexture, 1)

        #Setting Planet 1
        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(150, 5000, 67) #X, Y, Z
        self.Planet1.setScale(350)
        Planet1Texture = self.loader.loadTexture("Assets/Planets/planet1.jpg")
        self.Planet1.setTexture(Planet1Texture, 1)

        #Setting Planet 2
        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(5000, 5000, 180)
        self.Planet2.setScale(350)
        Planet2Texture = self.loader.loadTexture("Assets/Planets/planet2.jpg")
        self.Planet2.setTexture(Planet2Texture, 1)

        #Setting Planet 3
        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(5000, 100, -500)
        self.Planet3.setScale(500)
        Planet3Texture = self.loader.loadTexture("Assets/Planets/planet3.jpg")
        self.Planet3.setTexture(Planet3Texture, 1)

        #Setting Planet 4
        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(3000, 10000, 1000)
        self.Planet4.setScale(1000)
        Planet4Texture = self.loader.loadTexture("Assets/Planets/planet4.jpg")
        self.Planet4.setTexture(Planet4Texture, 1)

        #Setting Planet 5
        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(-1000, 2000, 200)
        self.Planet5.setScale(200)
        Planet5Texture = self.loader.loadTexture("Assets/Planets/planet5.jpg")
        self.Planet5.setTexture(Planet5Texture, 1)

        #Setting Planet 6
        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(1000, 3000, -300)
        self.Planet6.setScale(500)
        Planet6Texture = self.loader.loadTexture("Assets/Planets/planet6.jpg")
        self.Planet6.setTexture(Planet6Texture, 1)

        #Setting Space Station
        self.SpaceStation = self.loader.loadModel("./Assets/Space Station/spaceStation.x")
        self.SpaceStation.reparentTo(self.render)
        self.SpaceStation.setPos(1000, 500, 0)
        self.SpaceStation.setHpr(0, 90, 0)
        self.SpaceStation.setScale(10)

        #Setting Space Ship (The Borg)
        self.SpaceShip = self.loader.loadModel("./Assets/SpaceShips/theBorg.x")
        self.SpaceShip.reparentTo(self.render)
        self.SpaceShip.setPos(100, 100, 0)
        self.SpaceShip.setHpr(0, 90, 0)
        self.SpaceShip.setScale(2)
        SpaceShipTexture = self.loader.loadTexture("./Assets/SpaceShips/theBorg.jpg")
        self.SpaceShip.setTexture(SpaceShipTexture, 1)

play = SpaceJam()
play.run()