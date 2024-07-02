// the ourAnimals array will store the following: 
using System;
using System.Diagnostics;
using System.Linq;
using System.Text.Json.Serialization.Metadata;

string animalSpecies = "";
string animalID = "";
string animalAge = "";
string animalPhysicalDescription = "";
string animalPersonalityDescription = "";
string animalNickname = "";

// variables that support data entry
int maxPets = 8;
string? readResult;
string menuSelection = "";

// array used to store runtime data, there is no persisted data
string[,] ourAnimals = new string[maxPets, 6];

// TODO: Convert the if-elseif-else construct to a switch statement

// create some initial ourAnimals array entries
for (int i = 0; i < maxPets; i++)
{
    switch (i)
    {
        case 0:

            animalSpecies = "dog";
            animalID = "d1";
            animalAge = "2";
            animalPhysicalDescription = "medium sized cream colored female golden retriever weighing about 65 pounds. housebroken.";
            animalPersonalityDescription = "loves to have her belly rubbed and likes to chase her tail. gives lots of kisses.";
            animalNickname = "lola";
            break;

        case 1:

            animalSpecies = "dog";
            animalID = "d2";
            animalAge = "9";
            animalPhysicalDescription = "large reddish-brown male golden retriever weighing about 85 pounds. housebroken.";
            animalPersonalityDescription = "loves to have his ears rubbed when he greets you at the door, or at any time! loves to lean-in and give doggy hugs.";
            animalNickname = "loki";
            break;

        case 2:

            animalSpecies = "cat";
            animalID = "c3";
            animalAge = "1";
            animalPhysicalDescription = "small white female weighing about 8 pounds. litter box trained.";
            animalPersonalityDescription = "friendly";
            animalNickname = "Puss";
            break;

        case 3:

            animalSpecies = "cat";
            animalID = "c4";
            animalAge = "?";
            animalPhysicalDescription = "";
            animalPersonalityDescription = "";
            animalNickname = "";
            break;

        default:
            animalSpecies = "";
            animalID = "";
            animalAge = "";
            animalPhysicalDescription = "";
            animalPersonalityDescription = "";
            animalNickname = "";
            break;
    }

    ourAnimals[i, 0] = "ID #: " + animalID;
    ourAnimals[i, 1] = "Species: " + animalSpecies;
    ourAnimals[i, 2] = "Age: " + animalAge;
    ourAnimals[i, 3] = "Nickname: " + animalNickname;
    ourAnimals[i, 4] = "Physical description: " + animalPhysicalDescription;
    ourAnimals[i, 5] = "Personality: " + animalPersonalityDescription;
}

// display the top-level menu options
do
{
    Console.Clear();

    Console.WriteLine("Welcome to the Contoso PetFriends app. Your main menu options are:");
    Console.WriteLine(" 1. List all of our current pet information");
    Console.WriteLine(" 2. Add a new animal friend to the ourAnimals array");
    Console.WriteLine(" 3. Ensure animal ages and physical descriptions are complete");
    Console.WriteLine(" 4. Ensure animal nicknames and personality descriptions are complete");
    Console.WriteLine(" 5. Edit an animal’s age");
    Console.WriteLine(" 6. Edit an animal’s personality description");
    Console.WriteLine(" 7. Display all cats with a specified characteristic");
    Console.WriteLine(" 8. Display all dogs with a specified characteristic");
    Console.WriteLine();
    Console.WriteLine("Enter your selection number (or type Exit to exit the program)");

    readResult = Console.ReadLine();
    if (readResult != null)
    {
        menuSelection = readResult.ToLower();
    }

    Console.WriteLine($"You selected menu option {menuSelection}.");

    switch (menuSelection)
    {
        case "1":
            for (int i = 0; i < maxPets; i++)
            {
                for (int j = 0; j < 6; j++)
                {
                    if (ourAnimals[i, 0] != "ID #: ")
                    {
                        Console.WriteLine(ourAnimals[i, j]);
                    }
                }
            }
            Console.WriteLine("Press the Enter key to continue.");
            readResult = Console.ReadLine();
            break;
        case "2":
            Console.WriteLine("this app feature is coming soon - please check back to see progress.");
            Console.WriteLine("Press the Enter key to continue.");
            readResult = Console.ReadLine();
            break;
        case "3":

            for (int i = 0; i < maxPets; i++)
            {

                if (ourAnimals[i, 0] != "ID #: ")
                {
                    Console.WriteLine(ourAnimals[i, 0]);
                    string age_verify = ourAnimals[i, 2].Substring(5);
                    int results;
                    int.TryParse(age_verify, out results);

                    if (ourAnimals[i, 2] == "Age: " || results == 0)
                    {
                        string? age;
                        int result = 0;
                        do
                        {
                            Console.WriteLine($"Enter an age for {ourAnimals[i, 0]}");
                            age = Console.ReadLine();
                            if (age != null)
                            {
                                int.TryParse(age, out result);
                                if (result > 0)
                                {
                                    ourAnimals[i, 2] = "Age: " + result;
                                }
                            }
                        }
                        while (result == 0);
                    }
                    if (ourAnimals[i, 4] == "Physical description: ")
                    {
                        do
                        {
                            string? desc;
                            Console.WriteLine($"Enter a physical description for {ourAnimals[i, 0]} (size, color, breed, gender, weight, housebroken)");
                            desc = Console.ReadLine();
                            if (desc != null)
                            {
                                ourAnimals[i, 4] = "Physical description: " + desc;
                            }
                        } while (ourAnimals[i, 4] == "Physical description: ");
                    }
                }

            }
            Console.WriteLine("\nAge and physical description fields are complete for all of our friends. ");
            Console.WriteLine("Press Enter key to continue");
            readResult = Console.ReadLine();
            break;
        case "4":
            for (int i = 0; i < maxPets; i++)
            {
                if (ourAnimals[i, 0] != "ID #: ")
                {
                    Console.WriteLine(ourAnimals[i, 0]);
                    if (ourAnimals[i, 3] == "Nickname: ")
                    {
                        do
                        {
                            string? name;
                            Console.WriteLine($"Enter a nickname for {ourAnimals[i, 0]}");
                            name = Console.ReadLine();
                            if (name != null)
                            {
                                ourAnimals[i, 3] = "Nickname: " + name;
                            }
                        } while (ourAnimals[i, 3] == "Nickname: ");
                    }
                    if (ourAnimals[i, 5] == "Personality: ")
                    {
                        do
                        {
                            string? caracter;
                            Console.WriteLine($"Enter a personality description for {ourAnimals[i,0]} (likes or dislikes, tricks, energy level)");
                            caracter = Console.ReadLine();
                            if (caracter != null)
                            {
                                ourAnimals[i, 5] = "Personality: " + caracter;
                            }
                        } while (ourAnimals[i, 5] == "Personality: ");
                    }
                }
            }
            Console.WriteLine("\nNickname and personality fields are complete for all of our friends. ");
            Console.WriteLine("Press the Enter key to continue.");
                readResult = Console.ReadLine();
                break;
        case "5":
                    Console.WriteLine("this app feature is coming soon - please check back to see progress.");
                    Console.WriteLine("Press the Enter key to continue.");
                    readResult = Console.ReadLine();
                    break;
                case "6":
                    Console.WriteLine("this app feature is coming soon - please check back to see progress.");
                    Console.WriteLine("Press the Enter key to continue.");
                    readResult = Console.ReadLine();
                    break;
                case "7":
                    Console.WriteLine("this app feature is coming soon - please check back to see progress.");
                    Console.WriteLine("Press the Enter key to continue.");
                    readResult = Console.ReadLine();
                    break;
                case "8":
                    Console.WriteLine("this app feature is coming soon - please check back to see progress.");
                    Console.WriteLine("Press the Enter key to continue.");
                    readResult = Console.ReadLine();
                    break;
                default:
                    break;
                }
                Console.WriteLine("Press the Enter key to continue.");
                // pause code execution
                readResult = Console.ReadLine();

}while (menuSelection != "exit");
