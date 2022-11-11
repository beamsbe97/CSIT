// Objective: My Assignment 3
// Name: An Nguyen
// Student number: 
// File name: AnNguyen_237_A3.java
// Declaration: this is my own lab and I have not passed my lab to anyone in this class

class AnNguyen_273_A3_FX{

    public static void main(String[] args){
        System.out.println();
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
        return "";
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
        return "";
    }

}