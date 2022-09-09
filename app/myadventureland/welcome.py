from csv import writer

class AliceInWonderLand:
    
    def __init__(self,name):
        self.name = name
    #Setter method to set the name
    def setName(self,new_name):
        self.__name = new_name
    #display a welcome message with the name
    def displayWelcome(self):
        yes_no = ["yes", "no"]
        yesorno = ""
        print("Welcome {} ".format(self.name))
        while yesorno not in yes_no:
            yesorno = input("Do you want to enter the Wonder Land? Yes/No")
            if (yesorno).lower() == "yes":
                log_data = ["Do you want to enter the Wonder Land?",yesorno]
                self.log_info(log_data)
                self.displayIntro()
            elif yesorno.lower() == "no":
                log_data = ["Do you want to enter the Wonder Land?",yesorno]
                self.log_info(log_data)
                print("You missed meeting Alice the wonder girl")
                quit()
            else:
                print("Enter yes or no")

                
    def displayIntro(self):
        print("*********************** Alice in Wonder land***********************")
        print("********                 It is a lazy summer day, and you are sitting                   ********")
        print("by the bank of a peaceful river,enyoyin the sunshine.")
        print("A swan gracefully glides by and you watch until")
        print("it is out of sight.")

        print("You sigh and lean back against a tree. You are")
        print("feeling happy and drowsy. You close your eyes...")
        print("You are just dozing of when you hear someone")
        print("shout,Wait!")

        print("You open your eyes and see a girl running by.")
        print("She looks as if she's chasing someone.")
        print("You jump up and run alongside her.")
        print("\"Where are you going ?\"you ask.")
        print("The girl looks at you in surprise.")
        print("\"T haven\'t got time to talk,\" she says. \"I might lose him!”")
        print("“Lose who?” you ask. “Who are you chasing?”")
        print("“The White Rabbit!” answers the girl.")
        print("You are about to ask her why she is chasing a")
        print("white rabbit when she cries, “Look! He’s going in that hole!”")
        print("And without another word, the girl crawls into a")
        print("hole nearby. You don’t know what’s going on, but")
        print("you want to find out.")

        print("“Wait for me!” you shout.")
        print("You crawl into the hole, too—and find yourself 3")
        print("falling through space! But you are falling in slow motion.")
        print(" Presently you notice that you are floating past")
        print("cupboards and shelves, clocks and mirrors. Maybe")
        print("you could grab for something and break your fall. Or")
        print("you could let yourself continue to float downward.")
        #Give option to fall or grab
        grab_fall=["grab","fall"]
        graborfall = ''
        while graborfall not in grab_fall:
            graborfall = input("Would you like to grab something or let yourself fall? Grab/Fall")
            if graborfall.lower() == "grab":
                log_data = ["Would you like to grab something or let yourself fall?",graborfall]
                self.log_info(log_data)
                self.grab()
            elif graborfall.lower() == "fall":
                log_data = ["Would you like to grab something or let yourself fall?",graborfall]
                self.log_info(log_data)
                self.fall()
            else:
                print("Enter grab/fall")

    def grab(self):
        print("You grab for a cupboard and scramble inside. But")
        print("you are surprised to find that the inside of the")
        print("cupboard is a long tunnel spiraling downward.")

        print("You try to crawl back out, but the sides are too")
        print("steep. You slide down at breakneck speed!")

        print("Suddenly you shoot out the end—and land right")
        print("on top of someone!")


        print("You don’t know who is underneath you, but you")
        print("look up and recognize the girl you followed down the")
        print("rabbit hole. And suddenly you realize that you and")
        print("the girl are surrounded by giant playing cards!")

        print("You must have gotten smaller! What’s going on?")
        print("Is it magic, you wonder?")

        print("The girl looks at you. “Oh, dear!” she says. “I’m")
        print("afraid you just fell on the Queen of Hearts! Let’s")
        print("run before she gets mad and has our heads!”")

        print("You dash after the girl. “What’s your name?” you")
        print("ask. “Alice,” she replies.")
        print("“T’m very glad to meet you,” you say.")
        print("“I’m glad to meet you, too!”")

        print("You and Alice run through a dark forest until you")
        print("come to a fork in the road.")
        print("“Which way should we go?” says Alice. 9")
        print("Suddenly you notice two signs on a tree. One says")
        print("THIS WAY, and the other says THAT WAY.")
        print("“Well?” asks Alice.")
        print("You shrug and say, “We can either go THIS")
        print("WAY or THAT WAY, I think we should go...")
        
        #Give option to this or that
        this_that=["this","that"]
        thisorthat = ''
        while thisorthat not in this_that:
            thisorthat = input("Would you like to go this way or that way? This/That")
            print(thisorthat)
            if(thisorthat.lower() == "this"):
                log_data = ["Would you like to go this way or that way?",thisorthat]
                self.log_info(log_data)
                self.this()
                return
            elif(thisorthat.lower() == "that"):
                log_data = ["Would you like to go this way or that way?",thisorthat]
                self.log_info(log_data)
                self.that()
            else:
                print("Enter this/that")

    #When you choose to fall
    def fall(self):
        print("You float down and down until you land with a")
        print("thump at the bottom of the hole. You look around")
        print("for the girl, but she’s nowhere in sight. In front of")
        print("you is a passage with doors all along it. You run to")
        print("the end and reach another passageway. This one is")
        print("flooded.")
        print("“Now, where did she go?” you say aloud.")
        print("“Through my keyhole, into my garden!” says a")
        print("doorknob.")
        print("You jump with surprise. A talking doorknob!")
        print("But you recover quickly and say, “How can I get")    
        print("into your garden?”")
        print("“Just wish you were there!” says the doorknob. “I")
        print("find it’s much simpler that way.”")
        print("You can’t believe it will be that easy, but you")
        print("close your eyes and wish, anyway.")
        print("When you open them again, you find yourself in a")
        print("beautiful garden.")
        print("“It worked!” you cry.")

        print("Just then you see the girl again. You have both II shrunk to the size of the flowers in the garden.")
        print("“Hello,” you say. “What’s your name?”")

        print("“Alice,” answers the girl. At that very moment the White Rabbit runs by—and he’s all dressed up! You ask Alice what she wants to do—follow the rabbit or forget him and go exploring.")

        print("“What do you think we should do?” she asks.")
        #Give option for follow or explore
        follow_explore=["follow","explore"]
        followorexplore = ''
        while followorexplore not in follow_explore:
            followorexplore = input("Would you like to follow or explore? follow/explore")
            if(followorexplore.lower() == "follow"):
                log_data = ["Would you like to follow or explore?",followorexplore]
                self.log_info(log_data)
                self.follow()
            elif(followorexplore.lower() == "explore"):
                log_data = ["Would you like to follow or explore?",followorexplore]
                self.log_info(log_data)
                self.explore()
            else:
                print("Enter follow/explore")
    #When you choose to follow
    def follow(self):
        print("You and Alice chase after the White Rabbit. He runs down a path and into a small house, all the while saying, “Oh, my fur and whiskers, I’m late! I’m late!”")
        print("You are just about to follow the White Rabbit into the house when he dashes out again.")
        print("“Don’t just stand there,” he calls to Alice. “Go inside and fetch my gloves!”")
        print("Alice is so surprised that she runs into the house to do as the White Rabbit asks.")
        print("“Wait for me!” you yell.")
        print("You and Alice look everywhere, but you can’t find the White Rabbit’s gloves.")
        print("“T don’t think we’re going to find them at all,” says Alice.")
        print("- You can’t find the gloves, but you do find a cookie jar labeled TAKE ONE.")
        print("The cover is on tightly, however, and you will have to work to get it off. From outside you hear the White Rabbit call, “Hurry, please. Seconds count. The Queen will be very angry if I’m late!”")
        print("You don’t want the White Rabbit to get into trouble, but as Alice said, you probably won't ever find his gloves. And you are hungry. Should you stop to eat some cookies, or should you keep looking for the gloves?")

        #Give option for gloves or cookies
        gloves_cookies=["gloves","cookies"]
        glovesorcookies = ''
        while glovesorcookies not in gloves_cookies:
            glovesorcookies = input("Would you like to gloves or cookies? gloves/cookies")
            if(glovesorcookies.lower() == "gloves"):
                log_data = ["Would you like to gloves or cookies?",glovesorcookies]
                self.log_info(log_data)
                self.gloves()
            elif(glovesorcookies.lower() == "cookies"):
                log_data = ["Would you like to gloves or cookies?",glovesorcookies]
                self.log_info(log_data)
                self.cookies()
            else:
                print("Enter gloves/cookies")
    def cookies(self):
        print("After some twisting and turning, you get the cover off the cookie jar. You are so hungry that you gobble up two big cookies before you offer one to Alice.")
        print("Alice is nibbling on hers when you notice that the house has gotten smaller. No! You are getting bigger! It must be the cookies!")
        print("“Alice, help!” you yell, as your head pushes the roof off the house. You’re so big that there’s no more room for Alice in the house. She runs outside and looks at you helplessly as you grow up and up")
        print("Oh, why did you eat those cookies? Why didn’t you just TAKE ONE, as the label said.")
        print("Will you ever shrink to your proper size?")
        print("You hope you won't be quite this big when you wake up from your dream!")
        print("******************** The End ********************")
        quit()

    def gloves(self):
        print("You look high and low for the White Rabbit’s gloves. In one room you find a closet with a heavy door. You go inside—and the door slams shut behind you. You try to open it but you can’t. You’re locked in!")
        print("“Help!” you ery, but you know that Alice can’t hear you through the thick door. You will have to open it yourself.")
        print("You push and pull and tug, but the door won’t budge. Then, in the light that shines in under the door, you see a can of oil labeled USE ME.")
        print("You squirt the oil around the door and it swings open.")
        print("You rush out of the closet and out of the house, calling for Alice, but she is nowhere to be found.")
        print("“Well, if you must know,” says the Cheshire Cat, “THAT WAY leads to THE END.”")
        print("“That sounds crazy,” you say.")
        print("“Of course it does,” answers the cat. “That’s because it is crazy. Everything here is crazy.”")
        print("“T think we should go somewhere else,” says Alice.")
        print("You would like to talk to the Cheshire Cat some more, but Alice looks frightened.")
        
        #Give option to stay somewhere or stay
        somewhere_stay=["somewhere","stay"]
        somewhereorstay = ''
        while somewhereorstay not in somewhere_stay:
            somewhereorstay = input("Do you want to go somewhere or stay and talk with the cat? somewhere/talk")
            if(somewhereorstay.lower() == "somewhere"):
                log_data = ["Do you want to go somewhere or stay and talk with the cat?",somewhereorstay]
                self.log_info(log_data)
                self.somewhere()
            elif(somewhereorstay.lower() == "stay"):
                log_data = ["Do you want to go somewhere or stay and talk with the cat?",somewhereorstay]
                self.log_info(log_data)
                self.stay()
            else:
                print("Enter somewhere/stay")
    
    def somewhere(self):
        print("You and Alice continue along the path. Soon you come upon a big sign that says KEEP OUT BY ORDER OF TWEEDLEDUM. Beyond it lies a garden.")
        print("“Who’s Tweedledum?” asks Alice.")
        print("“Tt’s such a silly name,” you answer. “I’m sure it’s no one important.”")
        print("You want to follow a path that goes through the garden, but Alice isn’t sure that’s a good idea. The only other path, though, leads through some thick bushes.")

        
        #Give option to go to garden or bushes
        garden_bushes=["garden","bushes"]
        gardenorbushes = ''
        while gardenorbushes not in garden_bushes:
            gardenorbushes = input("Do you want to go through the garden or bushes? garden/bushes")
            if(gardenorbushes.lower() == "garden"):
                log_data = ["Do you want to go through the garden or bushes?",gardenorbushes]
                self.log_info(log_data)
                self.garden()
            elif(gardenorbushes.lower() == "bushes"):
                log_data = ["Do you want to go through the garden or bushes?",gardenorbushes]
                self.log_info(log_data)
                self.bushes()
            else:
                print("Enter garden/bushes")
    def garden(self):
        print("You step boldly into the garden, but Alice stands back.")
        print("As soon as you enter, you feel a tug on your arm.")
        print("“I’m Tweedledum,” says a roly-poly little man as he pulls you out of the garden. “Keep out!”")
        print("Then you feel a tug on your other arm.")
        print("“T’m Tweedledee, his brother,” says a look-alike man, as he pulls you into the garden. “Keep in!”")
        print("You are wondering what’s going on when you see  the other side of the sign, the side that’s facing the garden. It says KEEP IN BY ORDER OF TWEEDLEDEE. Just then, Tweedledum and Tweedledee pull at the same time. You feel as if youre stretching.")
        print("You look at your arms—you are!")
        print("“Help!” you cry to Alice, but there’s nothing she can do.")
        print("Oh, no! Now youre caught in a tug of war between two quarrelsome brothers, and you’re the rope!")
        print("**************The End***************************")
        quit()

    def bushes(self):
        print("When you come out on the other side of the thick bushes, you find yourselves in the middle of a tea party!")
        print("A funny little man in a big hat shouts, “This is the March Hare’s un-birthday party. Did you bring a present?”")
        print(" “Why, no,” you both say. “Good!” says the little man. “Then you’re un-invited!”")
        print("“The Mad Hatter is right,” says the March Hare. “You're un-invited, so sit down!” You and Alice sit down. In a few minutes you are caught up in the craziest party you’ve ever been to.")
        print("Everyone keeps switching places and switching cups, and the Hatter and Hare stuff a dormouse into the teapot! You’ve never had more fun at an un-birthday party in your life!")
        print("**********The End**************")
        quit()

    def explore(self):
        print("The White Rabbit scampers away, and you and Alice turn and run in the opposite direction. Soon you come to another garden.")
        print("“What kind of flowers are you?” asks a flower.")
        print("We're not flowers,” says Alice as a bread-and-butterfly glides by. She doesn’t seem at all surprised to hear the flower speak.")
        print("“Then you must be weeds!” says a daisy. “Be off with you!”")
        print("Talking flowers! Bread-and-butterflies! You’ve never seen anything like this in your life!")
        print("The path leads to a small beach, where a strange race is going on. It has no beginning and no end— everyone just runs around and around a rock.")
        print("“Would you hold this?” asks Alice, as she hands you a little golden key. “I want to join the race.”")
        print("You hold the key in your hand and watch the runners. But the race is making you dizzy. You close your eyes for a moment...")
        print(". . and when you open them, you’re back on the riverbank. Was it all a dream?")
        print("You feel something in your hand. You are still holding the key that Alice gave you!")
        print("You wonder if you can find your way back to the long hall at the bottom of the rabbit hole. You’re sure this is the key that opens the door to that wonderful place!")
        print("On the other hand, maybe if you just wish you were back...")
        print("******************** The End ********************")
        quit()

    def this(self):
        print("You and Alice follow the overgrown path to THIS")
        print("WAY. After walking a bit, you hear, “Stop!”")
        print("You look up in surprise and see a funny-looking")
        print("caterpillar sitting on a mushroom.")
        print("“Why must we stop?” you ask politely. “We want")
        print("to go THIS WAY.”")
        print("“Well, if you want to go THIS WAY,” says the")
        print("Caterpillar, “you will have to go THAT WAY to get")
        print("there.”")

        print("“But we don’t want to go THAT WAY,” cries")
        print("Alice. “And if we can’t go THIS WAY, we can’t go anywhere!”")
        print("“Well, that’s not true at all,” says the Caterpillar.")
        print("“There is always a where to go to when you can’t go")
        print("where you want to.”")
        print("“Really?” you say. “Then tell us where.”")
        print("“Why you can go nowhere!” says the Caterpillar.")
        print("You and Alice sigh and give up.")
        print("“There! That’s settled,” says the Caterpillar.")
        print("“But don’t worry,” he continues. “I will entertain 2 you. I know all my multiplication tables and [’ll recite them for you, one after the other.” You groan and sit down. Why did you choose to go THIS WAY? Now yov’e stuck with a boring caterpillar who loves arithmetic. What a way to spend the day. . . . What a way to end a dream!")
        print("****************************  The End ****************************")
        quit()

    def that(self):
        print("You and Alice follow the path to THAT WAY.")
        print("You have gone only a little way when you see a")
        print("Cheshire Cat on the branch of a tree.")
        print("“Excuse me, Cheshire Puss,” you say, “are we")
        print("going the right way for THAT WAY?”")
        print("Instead of answering, the Cheshire Cat just grins.")
        print("“Excuse me,” you say again, “but we would like 15 to know where THAT WAY leads to.”")
        print("The cat just keeps grinning from ear to ear. “Excuse me, too,” says Alice timidly, “but why are you grinning?”")
        print("“Why are you asking so many questions?” asks the cat, pointing to Alice.")
        print("“Because we want to know where THAT WAY leads to!” you say a bit angrily.")
        print("“Well, if you must know,” says the Cheshire Cat,“THAT WAY leads to THE END.”")
        print("“That sounds crazy,” you say.")
        print("“Of course it does,” answers the cat. “That’s because it is crazy. Everything here is crazy.”") 
        print("“T think we should go somewhere else,” says Alice.") 
        print("You would like to talk to the Cheshire Cat some more, but Alice looks frightened.") 
        print("Do you want to go some where or talk? Somewhere / talk")
        #Give option to somewhere or talk
        somewhere_talk=['somewhere','talk']
        somewhereortalk = ''
        while somewhereortalk not in somewhere_talk:
            somewhereortalk = input("Would you like to go somwhere or talk? somewhere/talk")
            if(somewhereortalk == "somewhere"):
                log_data = ["Would you like to go somwhere or talk?",somewhereortalk]
                self.log_info(log_data)
                self.somewhere()
            elif(somewhereortalk == "talk"):
                log_data = ["Would you like to go somwhere or talk?",somewhereortalk]
                self.log_info(log_data)
                self.talk()
            else:
                print("Enter somewhere/talk")
    
    def somewhere(self):
        print("You and Alice continue along the path.")
        print("Soon you come upon a big sign that says KEEP")
        print("OUT BY ORDER OF TWEEDLEDUM. Beyond it lies a garden.")
        print("“Who’s Tweedledum?” asks Alice.")
        print("“Tt’s such a silly name,” you answer. “I’m sure it’s no one important.”")
        print("You want to follow a path that goes through")
        print("the garden, but Alice isn’t sure that’s a good idea.")
        print("The only other path, though, leads through some thick bushes.")
        print("Do you want to go through the garden or through the bushes? garden/bushes")
        #Give option to somewhere or talk
        garden_bushes=['garden','bushes']
        gardenorbushes = ''
        while gardenorbushes not in garden_bushes:
            gardenorbushes= input("Would you like to go through garden or bushes? garden/bushes")
            if(gardenorbushes == "garden"):
                log_data = ["Would you like to go through garden or bushes?",gardenorbushes]
                self.log_info(log_data)
                self.garden()
            elif(gardenorbushes == "bushes"):
                log_data = ["Would you like to go through garden or bushes?",gardenorbushes]
                self.log_info(log_data)
                self.bushes()
            else:
                print("Enter garden/bushes")
    def talk(self):
        print("“What do you mean THAT WAY leads to THE END?” you ask the Cheshire Cat.")
        print("But instead of answering, the cat starts to disappear!")
        print("Soon all that is left is his grin. “Well,” says Alice, “I’ve often seen a cat without a grin, but a grin without a cat! It’s the most curious thing I ever saw in all my life!”")
        print("“Me, too,” you answer. “And by the way, I’m more curious than ever to find out where THAT WAY leads!” So you and Alice continue down the path. In a little while you come to a grove of Weeping Willow trees.Suddenly Alice stubs her toe on a rock and starts to cry.")
        print("You are trying to make her feel better, when a big drop of water falls on your head. Then another .. . and another and another. Is it raining? No! It’s the Weeping Willows. They    are crying with Alice! They cry so hard they start a small flood!")
        print("“Stop crying, Alice,” you say. “You’re making the Weeping Willows cry, too!”")
        print("“T can’t,” sobs Alice. “It hurts too much!”")
        print("You try to help her up, but now the flood of tears ot has turned into a small river. You and Alice are swept along like two leaves.")
        print("Suddenly you hear a roar. Oh, no! There’s a big waterfall ahead and you are heading right for it! “I hope this is all a dream,” you say. “Otherwise going THAT WAY really is going to lead to... ")
        print("****************************  The End ****************************")
        quit()

    def log_info(self,data):
        with open('log_info.csv', 'a', newline='') as f:
            writer_object = writer(f)
            # write the data
            writer_object.writerow(data)
            f.close()
def main():
    name = input("Enter your name")
    aliceland = AliceInWonderLand(name)
    aliceland.displayWelcome()
    aliceland.displayIntro()

main()
