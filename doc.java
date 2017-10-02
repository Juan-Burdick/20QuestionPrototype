package com.mkyong;

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
      JSONObject q4 = new JSONObject();
      JSONObject q5 = new JSONObject();
      JSONObject q6 = new JSONObject();
      JSONObject q7 = new JSONObject();
      JSONObject q8 = new JSONObject();
      JSONObject q9 = new JSONObject();
      JSONObject q10 = new JSONObject();
      JSONObject q11 = new JSONObject();
      JSONObject q12 = new JSONObject();
      JSONObject q13 = new JSONObject();
      JSONObject q14 = new JSONObject();
      JSONObject q15 = new JSONObject();
      JSONObject q16 = new JSONObject();
      JSONObject q17 = new JSONObject();
      JSONObject q18 = new JSONObject();
      JSONObject q19 = new JSONObject();
      JSONObject q20 = new JSONObject();

      q1.put("ID" , "1");
      q1.put("question" , "does it have fur?");
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
      
      q4.put("ID" , "4");
      q4.put("question" , "is it found in the US?");
      q4.put("Ysub" , "1,2,3,4");
      q4.put("Nsub" , "5,6,7,8");
      q4.put("answers" , "12,23,34");
      
      q5.put("ID" , "5");
      q5.put("question" , "is it a mamal?");
      q5.put("Ysub" , "1,2,3,4");
      q5.put("Nsub" , "5,6,7,8");
      q5.put("answers" , "12,23,34");
      
      q6.put("ID" , "6");
      q6.put("question" , "is it a reptile?");
      q6.put("Ysub" , "1,2,3,4");
      q6.put("Nsub" , "5,6,7,8");
      q6.put("answers" , "12,23,34");
     
      q7.put("ID" , "7");
      q7.put("question" , "is it domesticated?");
      q7.put("Ysub" , "1,2,3,4");
      q7.put("Nsub" , "5,6,7,8");
      q7.put("answers" , "12,23,34");
      
      q8.put("ID" , "8");
      q8.put("question" , "can it fly?");
      q8.put("Ysub" , "1,2,3,4");
      q8.put("Nsub" , "5,6,7,8");
      q8.put("answers" , "12,23,34");
      
      q9.put("ID" , "9");
      q9.put("question" , "does it live underground?");
      q9.put("Ysub" , "1,2,3,4");
      q9.put("Nsub" , "5,6,7,8");
      q9.put("answers" , "12,23,34");
      
      q10.put("ID" , "10");
      q10.put("question" , "is it big?");
      q10.put("Ysub" , "1,2,3,4");
      q10.put("Nsub" , "5,6,7,8");
      q10.put("answers" , "12,23,34");
      
      q11.put("ID" , "11");
      q11.put("question" , "is it small?");
      q11.put("Ysub" , "1,2,3,4");
      q11.put("Nsub" , "5,6,7,8");
      q11.put("answers" , "12,23,34");
      
      q12.put("ID" , "12");
      q12.put("question" , "is it dog sized?");
      q12.put("Ysub" , "1,2,3,4");
      q12.put("Nsub" , "5,6,7,8");
      q12.put("answers" , "12,23,34");
      
      q13.put("ID" , "13");
      q13.put("question" , "can it climb trees?");
      q13.put("Ysub" , "1,2,3,4");
      q13.put("Nsub" , "5,6,7,8");
      q13.put("answers" , "12,23,34");
      
      q14.put("ID" , "14");
      q14.put("question" , "is it nocturnal?");
      q14.put("Ysub" , "1,2,3,4");
      q14.put("Nsub" , "5,6,7,8");
      q14.put("answers" , "12,23,34");
      
      q15.put("ID" , "15");
      q15.put("question" , "is it a carnivore?");
      q15.put("Ysub" , "1,2,3,4");
      q15.put("Nsub" , "5,6,7,8");
      q15.put("answers" , "12,23,34");
      
      q16.put("ID" , "16");
      q16.put("question" , "is it friendly?");
      q16.put("Ysub" , "1,2,3,4");
      q16.put("Nsub" , "5,6,7,8");
      q16.put("answers" , "12,23,34");
      
      q17.put("ID" , "17");
      q17.put("question" , "does it have stripes?");
      q17.put("Ysub" , "1,2,3,4");
      q17.put("Nsub" , "5,6,7,8");
      q17.put("answers" , "12,23,34");
      
      q18.put("ID" , "18");
      q18.put("question" , "is it fast?");
      q18.put("Ysub" , "1,2,3,4");
      q18.put("Nsub" , "5,6,7,8");
      q18.put("answers" , "12,23,34");
      
      q19.put("ID" , "19");
      q19.put("question" , "does it have a good sense of smell?");
      q19.put("Ysub" , "1,2,3,4");
      q19.put("Nsub" , "5,6,7,8");
      q19.put("answers" , "12,23,34");
      
      
      q20.put("ID" , "20");
      q20.put("question" , "can you ride it?");
      q20.put("Ysub" , "1,2,3,4");
      q20.put("Nsub" , "5,6,7,8");
      q20.put("answers" , "12,23,34");
      
      
      
      
      System.out.print(q1);
      System.out.print(q2);
      System.out.print(q3);
      System.out.print(q4);
      System.out.print(q5);
      System.out.print(q6);
      System.out.print(q7);
      System.out.print(q8);
      System.out.print(q9);
      System.out.print(q10);
      System.out.print(q11);
      System.out.print(q12);
      System.out.print(q13);
      System.out.print(q14);
      System.out.print(q15);
      System.out.print(q16);
      System.out.print(q17);
      System.out.print(q18);
      System.out.print(q19);
      System.out.print(q20);

      try (FileWriter File = new FileWriter("C:\Users\Josh\Desktop\school\Git destination\git stuff\20QuestionPrototype")) 
      File.write(q1);
      File.write(q2);
      File.write(q3);
      File.write(q4);
      File.write(q5);
      File.write(q6);
      File.write(q7);
      File.write(q8);
      File.write(q9);
      File.write(q10);
      File.write(q11);
      File.write(q12);
      File.write(q13);
      File.write(q14);
      File.write(q15);
      File.write(q16);
      File.write(q17);
      File.write(q18);
      File.write(q19);
      File.write(q20);


      


   }
}