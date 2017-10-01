import java.util.concurrent.ThreadLocalRandom;

public class 20Q_Prototype
{}

    public static void main (String[] args) 
    {
        private int count = 0;
        private String input;
        private int subsetSize = 0;
        private String[] TagArray = new String[20];
        private int questionID;
        private ArrayList() answerArray;
        private ArrayList() questionSubset;
    }
    
    public void runTime() 
    {
        while (count >= 0 || count <= 20) 
        {
            // read question from file
            // receiveInput -> input
            input.toUpperCase();
            while !(input == "Y" || input == "YES" || input == "N" || input == "NO") 
            { 
                //display(error msg);
                // receiveInput -> input 
            }
            if (input == "Y" || input == "YES") 
            {
                // get size of subset somehow
                questionID = selectNextQuestion(questionID.YesSubQuestions[], subsetSize);
                TagArray[count] = questionID.Tag[0];
            }
            else if (input == "N" || input == "NO") 
            {
                //get size of subset somehow
                questionID = selectNextQuestion(questionID.NoSubQuestions[], subsetSize);
                TagArray[count] = questionID.Tag[1];
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
        
    }

    private void addAnswer(String[] tags)
    {
        answers.put("ID", new Integer(/* some function for next ID in line */));
        answers.put("text", /* text from user */);
        answers.put("tags", /* tag array, prob have to for:each this */);
    }
}