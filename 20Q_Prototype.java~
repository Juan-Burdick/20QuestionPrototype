import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import java.io.FileWriter;
import java.io.IOException;

import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Iterator;

import java.util.concurrent.ThreadLocalRandom;
import java.util.Scanner;
import java.io.*;

class QuestionsPrototype
{

    public static void main (String[] args) throws IOException
    {
        int count = 0;
        FileReader fileReader = null;
        FileInputStream aDocIn = null;
        FileOutputStream aDocOut = null;
        File file = null;
        String input;
        int subsetSize = 0;
        String[] TagArray = new String[20];
        int questionID;
        
        
        Scanner scan = new Scanner(System.in);
        JSONParser parser = new JSONParser();
        // input variable for yes or no answer
        // scan = input.next(); 
        
        try 
        {
            // fileReader = new FileReader("questions.txt");
            // BufferedReader qDoc = new BufferedReader(fileReader);
            Object obj = parser.parse(new FileReader("C:/Users/Josh/Desktop/project/20QuestionPrototype/info.json"));
            JSONObject jsonObject = (JSONObject) obj;
            String name = (String) jsonObject.get("ID");
            System.out.println(name);

           
        }catch (Exception e) 
          {
              e.printStackTrace();
          }


        finally
        {
            
        }
    }

    
}
