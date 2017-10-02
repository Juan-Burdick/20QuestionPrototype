

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import java.io.FileWriter;
import java.io.IOException;

import org.json.simple.JSONObject;

class QuestionEncoder {

   public static void main(String[] args){
      JSONObject q1 = new JSONObject();
      JSONObject q2 = new JSONObject();
      JSONObject q3 = new JSONObject();

      q1.put("ID" , "1").put("question" , "does it have fur?");
      //q1.put("question" , "does it have fur?");
      q1.put("Ysub" , "1,2,3,4");
      q1.put("Nsub" , "5,6,7,8");
      q1.put("answers" , "12,23,34");
      
      q2.put("ID" , "2");
      q2.put("question" , "is it a land dweller?");
      q2.put("Ysub" , "1,2,3,4");
      q2.put("Nsub" , "5,6,7,8");
      q2.put("answers" , "12,23,34");
      
      q3.put("ID" , "3");
      q3.put("question" , "does it have more than four legs?");
      q3.put("Ysub" , "1,2,3,4");
      q3.put("Nsub" , "5,6,7,8");
      q3.put("answers" , "12,23,34");
     
      System.out.print(q1);
      System.out.print(q2);
      System.out.print(q3);

      try 
      {
        FileWriter fileWriter = new FileWriter("info.json");
        fileWriter.write(q1.toJSONString());
        fileWriter.write("\n");
        fileWriter.write(q2.toJSONString());
        fileWriter.write("\n");
        fileWriter.write(q3.toJSONString());
        fileWriter.write("\n");
        
        fileWriter.flush();
      } 
      catch (Exception e) 
      {
        e.printStackTrace();
      }
      System.out.println(q1);
      



   }
}

