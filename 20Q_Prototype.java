public class 20Q_Prototype{ 

    public static void main (String[] args) {
        int count = 0;
        String input;
        boolean check;
        String[] TagArray = new String[20];
        UUID questionID;
    }
    
    public static runTime() {
        while (count >= 0 || count <= 20) {
            /* read question from file */
            receiveInput -> input;
            while (input =/= some form of yes/no) { 
                display(error msg); receiveInput -> input; 
            }
            if (input == yes) {
                questionID = selectFunction(questionID.YesSubQuestions);
                TagArray[questionCount] = questionID.Tag[0];
            }
            else if (input == no) {
                questionID = selectFunction(questionID.NoSubQuestions);
                TagArray[questionCount] = questionID.Tag[1];
            }
            else { 
                exit with error code; 
            }
            if (questionCount == 20) { 
                populate answerArray/select answers; 
            }
            count++;
        }
    }
}