

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Ismael
 */
public class ProblemA {
    public static void main(String[] args) throws FileNotFoundException {
        FileReader f= new FileReader("C:\\Users\\Ismael\\Desktop\\inputA.txt");
        PrintWriter out =new PrintWriter("C:\\Users\\Ismael\\Desktop\\outputA.txt");
        Scanner in = new Scanner(f);
        int cant= in.nextInt();

        for (int i = 0; i < cant; i++) {
            double R= in.nextInt();
            double C= in.nextInt();
            double W= in.nextInt();
            
            double res=W+Math.ceil((C-W)/W);

            
            
            
            
            out.println("Case #"+(i+1)+": "+(int)res);
        }
            
            
        
        in.close();
        out.close();
    }

}