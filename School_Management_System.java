import java.util.Scanner;


class Student
{


  private String name;

  private int iuNo;


  private int semester;

  private int sec;

  private int age;




  // Method for taking user input
  public void takeInput ()
  {

    Scanner scanner = new Scanner (System.in);


      System.out.print ("Enter name: ");

      name = scanner.nextLine ();



      System.out.print ("Enter IU Number: ");

      iuNo = scanner.nextInt ();


      System.out.print ("Enter Semester: ");

      semester = scanner.nextInt ();



      System.out.print ("Enter Section: ");

      sec = scanner.nextInt ();





      System.out.print ("Enter Age : ");

      age = scanner.nextInt ();








  }

  // Method for displaying student information
  public void displayInfo ()
  {

    System.out.println ("Name: " + name);

    System.out.println ("IU Number:  " + "IU" + iuNo);


    System.out.println ("Semester: " + semester);

    System.out.println ("Section: " + sec);

    System.out.println ("Age: " + age);


  }
}




class Teacher
{

  private String name;
  private int age;
  private String subject;

  // Method for taking user input
  public void takeInput ()
  {
    Scanner scanner = new Scanner (System.in);

      System.out.print ("Enter Teacher name: ");
      name = scanner.nextLine ();

      System.out.print ("Enter age: ");
      age = scanner.nextInt ();
      scanner.nextLine ();

      System.out.print ("Enter subject: ");
      subject = scanner.nextLine ();
  }

  // Method for displaying teacher information
  public void displayInfo ()
  {
    System.out.println ("Name: " + name);
    System.out.println ("Age: " + age);
    System.out.println ("Subject: " + subject);
  }
}



class Courses
{

  private String courseCode;
  private String courseName;
  private int courseCredit;

  // Method for taking user input
  public void takeInput ()
  {
    Scanner scanner = new Scanner (System.in);

      System.out.print ("Enter course code: ");
      courseCode = scanner.nextLine ();

      System.out.print ("Enter course name: ");
      courseName = scanner.nextLine ();

      System.out.print ("Enter course credit: ");
      courseCredit = scanner.nextInt ();
      scanner.nextLine ();
  }

  // Method for displaying course information
  public void displayInfo ()
  {
    System.out.println ("Course Code: " + courseCode);
    System.out.println ("Course Name: " + courseName);
    System.out.println ("Course Credit: " + courseCredit);
  }
}



class FeePayment
{

  private String studentName;
  private int totalFee;
  private int paidFee;
  private int remainingFee;

  // Method for taking user input
  public void takeInput ()
  {
    Scanner scanner = new Scanner (System.in);

      System.out.print ("Enter student name: ");
      studentName = scanner.nextLine ();

      System.out.print ("Enter total fee: ");
      totalFee = scanner.nextInt ();

      System.out.print ("Enter paid fee: ");
      paidFee = scanner.nextInt ();

      remainingFee = totalFee - paidFee;
  }

  // Method for displaying payment information
  public void displayInfo ()
  {
    System.out.println ("Student Name: " + studentName);
    System.out.println ("Total Fee: " + totalFee);
    System.out.println ("Paid Fee: " + paidFee);
    System.out.println ("Remaining Fee: " + remainingFee);
  }
  
  
   public void displayInfo1 ()
  {
   
    System.out.println ("Total Fee: " + totalFee);
    System.out.println ("Paid Fee: " + paidFee);
    System.out.println ("Remaining Fee: " + remainingFee);
  }

  // Method for calculating payment
  public void calculatePayment (int paymentAmount)
  {
    if (paymentAmount <= remainingFee)
      {
	paidFee += paymentAmount;
	remainingFee -= paymentAmount;
	System.out.println ("Payment successful. Remaining Fee: " +
			    remainingFee);
      }
    else
      {
	System.out.
	  println ("Payment failed. Payment amount exceeds remaining fee.");
      }
  }
}



 class Result {
    
    private int[] marks;
    private int average;
    private boolean isPass;
    
    public void takeInput() {
        Scanner scanner = new Scanner(System.in);
        marks = new int[5];
        
        System.out.println("Enter marks for 5 subjects:");
        for (int i = 0; i < 5; i++) {
            System.out.print("Subject " + (i+1) + ": ");
            marks[i] = scanner.nextInt();
        }
        
        calculateAverage();
    }
    
    private void calculateAverage() {
        int sum = 0;
        for (int mark : marks) {
            sum += mark;
        }
        average = sum / 5;
    }
    
    public void checkPass() {
        if (average >= 40) {
            isPass = true;
            System.out.println("Congratulations! You have passed.");
        } else {
            isPass = false;
            System.out.println("Sorry, you have failed. Please try again.");
        }
    }
    
    public void displayInfo() {
        System.out.println("Average: " + average);
        System.out.println("Pass Status: " + (isPass ? "Pass" : "Fail"));
    }
}





public class Main
{

  public static void main (String[]args)
  {

    int i, j;

    Student student = new Student ();
    Teacher teacher = new Teacher ();
    Courses course = new Courses ();
    FeePayment payment = new FeePayment ();
    Result result = new Result();

    for (j = 0; j <= 90; j++)
      {

	System.out.println ("------------------------------------------------------------University Management System---------------------------------------------------------------------");

	System.out.
	  println
	  ("Enter choice\n 1. Add Student \n 2. Display Student Info\n 3. Add Teacher  \n 4. Display Teacher Info\n 5. Add Course \n 6. Display Course\n 7. FeePayment\n 8. Display Fee \n 9. Calculate Fee Payment \n 10. Report \n 11.Result \n 12. EXIT");

	Scanner scanner = new Scanner (System.in);


	  i = scanner.nextInt ();
	int choice = i;

	switch (choice)
	  {
	  case 1:
	    student.takeInput ();
	    break;
	    case 2:
	        student.displayInfo ();
	    break;
	    case 3:
	        teacher.takeInput ();
	    break;
	    case 4:
	        teacher.displayInfo ();
	    break;
	    case 5:
	        course.takeInput ();
	    break;
	    case 6:
	        course.displayInfo ();
	    break;
	    case 7:
	        payment.takeInput ();
	    break;
	    case 8:
	        payment.displayInfo ();
	    break;
	    case 9:System.out.print ("Enter payment amount: ");
	    int paymentAmount = scanner.nextInt ();
	      payment.calculatePayment (paymentAmount);
	      break;
	    case 10:
	       System.out.println("Report is Generated");
	       student.displayInfo ();
	       payment.displayInfo1 ();
	       
	    break;
	     case 11:
	       System.out.println("Result is Generated");
	       result.takeInput();
           result.checkPass();
           result.displayInfo();
	       
	    break;

	  }
	if (choice == 12)
	  {
	    break;
	  }
      }
  }
}


