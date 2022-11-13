// Objective: My Assignment 3
// Name: An Nguyen
// Student number: 
// File name: AnNguyen_237_A3.java
// Declaration: this is my own lab and I have not passed my lab to anyone in this class

import javax.swing.JFrame;
import javax.swing.JTextField;

import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextArea;

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

class AnNguyen_273_A3_FX extends JFrame{
  
    public static void main(String[] args){
        DemoSys ds = new DemoSys();
        ds.setSize(500, 800);
        ds.setVisible(true);
        ds.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);



    }
}

class DemoSys extends JFrame{
    private static Random rand = new Random();
    private static String[] comments = {"Statements too long", "Use meaningful identifiers", "Overall design OK", "Some improvements needed", "Well done"};
    private static String[] nameArray = {"Jessica", "Mike", "John", "Boris"};
    private static String[] titles = {"Part time student", "Full time student"};
    private static String[] imageFiles = {"1.jpg", "2.jpg", "3.jpg"};
    private static String[] groups = {"T01", "T02", "T03", "T04", "T05"};
    private static String[] demoWhat = {"Lab 1", "Lab 2", "Lab3", "Lab 4", "Assignment 1", "Assignment 2", "Assignment 3"};

    private static void generateMessage(ArrayList<String> alist){
        alist.add(comments[rand.nextInt(comments.length)]);
        for (int i = 0; i < rand.nextInt(comments.length); i++) {
            String message = comments[rand.nextInt(comments.length)];
            if(!alist.contains(message) && !alist.contains("Well done") && message !="Well done"){
                alist.add(message);
            }   
        }
    }

    public String generateName(){
        return nameArray[rand.nextInt(nameArray.length)];
    }

    public String generateTitle(){
        return titles[rand.nextInt(titles.length)];
    }

    public String generateImageFile(){
        return imageFiles[rand.nextInt(imageFiles.length)];
    }

    public String generateGroup(){
        return groups[rand.nextInt(groups.length)];
    }

    public String generateDemoWhat(){
        return demoWhat[rand.nextInt(demoWhat.length)];
    }



    private final JButton okButton;
    private JButton refreshButton;


    public DemoSys(){
        super("Let us start");
        setLayout (new FlowLayout ());
        
        JLabel welcomejl = new JLabel();
        Icon welcomeic = new ImageIcon("C:/Users/nguye/OneDrive/Desktop/homework.PNG");
        welcomejl.setIcon(welcomeic);
        add(welcomejl);

        okButton = new JButton("OK");
        add(okButton);

        okButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                //JOptionPane.showMessageDialog(null,"asdfasdf");
                JFrame aFrame = new JFrame ("Welcome to 121 Demo System");
                aFrame.setLayout (new FlowLayout ());
		        aFrame.setSize (500, 800);
		        aFrame.setVisible (true);

                JLabel label = new JLabel();
                Icon ic = new ImageIcon("C:/Users/nguye/OneDrive/Desktop/homework.PNG");
                label.setIcon(ic);
                aFrame.add(label);
                refreshButton = new JButton("Refresh button to get the next student");
                //aFrame.add(label);
                aFrame.add(refreshButton);

                refreshButton.addActionListener(new ActionListener() {
                    public void actionPerformed(ActionEvent e) {
                        Student student = new Student(generateName(),generateTitle(), "1.jpg", generateGroup(), generateDemoWhat());
                        JFrame studentFrame = new JFrame("Let us welcome " + student.getName());
                        studentFrame.setLayout (new FlowLayout ());

                        JLabel studentLabel = new JLabel(student.toString());
                        studentFrame.add(studentLabel);
    
                        studentFrame.setSize (200, 300);
                        studentFrame.setVisible (true);
                        JButton buttonOK1 = new JButton("OK");
                        studentFrame.add(buttonOK1);
                        

                        buttonOK1.addActionListener(new ActionListener() {
                            public void actionPerformed(ActionEvent e) {
                                ArrayList<String> message = new ArrayList<String>();
                                generateMessage(message);
                                Lecturer lecturer = new Lecturer(student.getName(), student.getTitle(), "heng.jpg", message);
                                JFrame lecturerFrame = new JFrame("Hi "+ student.getName() +", my comment to your " + student.getTitle());
                                lecturerFrame.setLayout (new FlowLayout ());

                                JLabel lecturerLabel = new JLabel(lecturer.toString());
                                lecturerFrame.add(lecturerLabel);
            
                                lecturerFrame.setSize (200, 300);
                                lecturerFrame.setVisible (true);
                                JButton buttonOK2 = new JButton("OK");
                                lecturerFrame.add(buttonOK2);

                                
                            }
                        });
                    
                    }
                });
                


            }
        });


    }

}

class PersonInfo{
    protected String name;
    protected String title;
    protected String imageFile;

    public PersonInfo(){}

    public PersonInfo(String name, String title, String imageFile){
        setInfo(name, title, imageFile);
    }

    public PersonInfo(PersonInfo pi){
        this(pi.name, pi.title, pi.imageFile);
    }

    public String getName(){
        return name;
    }

    public String getTitle(){
        return title;
    }

    public String getImageFile(){
        return imageFile;
    }

    public void setInfo(String name, String title, String imageFile){
        this.name = name;
        this.title = title;
        this.imageFile = imageFile;
    }

    @Override
    public String toString(){
        return "";
    }
}

class Student extends PersonInfo{
    private String group;
    private String demoWhat;

    public Student(){}

    public Student(String name, String title, String imageFile, String group, String demoWhat){
        this.setInfo(name, title, imageFile, group, demoWhat);
    }

    public String getGroup(){
        return group;
    }

    public String getDemoWhat(){
        return demoWhat;
    }

    public void setInfo(String name, String title, String imageFile, String group, String demoWhat){
        super.setInfo(name, title, imageFile);
        this.group = group;
        this.demoWhat = demoWhat;
    }

    @Override
    public String toString(){
        return String.format("<html>I am %s<br>%s<br>I am from group %s<br>I wish to demo %s%n<html>", name, title, group, demoWhat);
    }

}

class Lecturer extends PersonInfo{
    private ArrayList<String> message;

    public Lecturer(){}
    
    public Lecturer(String name, String title, String imageFile, ArrayList<String> message){
        this.setInfo(name, title, imageFile, message);
    }

    public Lecturer(Lecturer lect){
        
    }

    public ArrayList<String> getMessage(){
        return message;
    }

    public void setInfo(String name, String title, String imageFile, ArrayList<String> message){
        super.setInfo(name, title, imageFile);
        this.message = message;
    }

    public String toString(){
        return String.format("<html>My suggestions, if any:<br>%s<html>", message);
    }

}