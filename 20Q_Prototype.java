import java.util.concurrent.ThreadLocalRandom;
import java.util.Scanner;
import java.io.*;

public class 20Q_Prototype
{}

    public static void main (String[] args) 
    {
        private int count = 0;
        File file = null;
        private String input;
        private int subsetSize = 0;
        private String[] TagArray = new String[20];
        private int questionID;
        private ArrayList() answerArray;
        private ArrayList() questionSubset;
        Scanner scan = new Scanner(System.in);
        // input variable for yes or no answer @param scan
        // scan = input.next(); 
        
    }
    
    public void runTime() 
    {
        while (count >= 0 || count <= 20) 
        {
            system.out.println(file.count)
            // read question from file
            // receiveInput -> input
            scan = input.next();
            input.toUpperCase();
            while !(input == "Y" || input == "YES" || input == "N" || input == "NO") 
            { 
                system.out.println("ERROR: input yes or no");
            }
            if (input == "Y" || input == "YES") 
            {
                // get size of subset somehow
                //questionID = selectNextQuestion(questionID.YesSubQuestions[], subsetSize);
                //TagArray[count] = questionID.Tag[0];
                TagArray[count] = "Q" + count + " = yes";
            }
            else if (input == "N" || input == "NO") 
            {
                //get size of subset somehow
                //questionID = selectNextQuestion(questionID.NoSubQuestions[], subsetSize);
                //TagArray[count] = questionID.Tag[1];
                TagArray[count] = "Q" + count + " = no";
            }
            else 
            { 
                break; 
            }
            if (count == 20) 
            { 
                populateAnswers(TagArray[]);
            }
            else if (count > 20)
            {
                break;
            }
            count++;
        }
    }

    private void selectNextQuestion(int[] qIDs, int max) 
    {
        int randomNum = ThreadLocalRandom.current().nextInt(1, max + 1);
        // randomnumber constrained to size of array
    }

    private void populateAnswers(String[] tags)
    {
        int match = 0;
        for(int i = 0; i < FileAnswer.size(); i++)
        {
            for(int j = 0; j < 20; j++)
            {
                while(FileAnswer.tags[j] != null)
                {
                    if(tags[j] == File)
                    {
                        match += 1;
                    }
                    else
                    {
                    }
                }
            }
        }

    }

    private void addAnswer(String[] tags)
    {
        answers.put("ID", new Integer(/* some function for next ID in line */));
        answers.put("text", /* text from user */);
        answers.put("tags", /* tag array, prob have to for:each this */);
    }
}

// https://github.com/Juan-Burdick/20QuestionPrototype.git