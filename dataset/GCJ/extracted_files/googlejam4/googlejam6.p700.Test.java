/* package whatever; // don't place package name! */


/* Name of the class has to be "Main" only if the class is public. */
class Test
{
	
	public static void main (String[] args) throws java.lang.Exception
	{
int a=4,b=0;
try{
	int c=a/b;
}
catch (Exception e)
{
	System.out.println("A");
}
finally
{
	System.out.println("B");
}
}

}
