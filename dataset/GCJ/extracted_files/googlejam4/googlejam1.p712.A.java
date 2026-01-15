

public class A {
	public static void main(String[] args) throws Exception {
		String output = "";
		
		String pathname = "D:\\Documents\\Downloads\\A-l.in"; 
		File filename = new File(pathname); 
		InputStreamReader reader = new InputStreamReader(new FileInputStream(
				filename));
		BufferedReader sc = new BufferedReader(reader);

		int total = Integer.parseInt(sc.readLine());
		//total=2;
		int starting = 1;
		//Syste                                                                                                                                                                                                                                                                                               m.out.println(total);
		int[] arr = new int[total];
		for (int i = 0; i < total; i++) {
			int n = Integer.parseInt(sc.readLine());
			String r1 = sc.readLine();
			String[] a1 = r1.split(" ");
			//pl(n);
			int totalSum=0;
			int before=Integer.parseInt(a1[0]);
			for( int k=1;k<n;k++){
				int mm = Integer.parseInt(a1[k]);
				//pl("before: "+before+", mm:"+mm);
				if(mm<=before){
					totalSum+=(before-mm);
				}else{
					//totalSum+=before;
				}
				before = mm;
			}
			
			//second method 
			int totalSum2=0;
			int before2=Integer.parseInt(a1[0]);
			int findMax2=0;
			
			for( int k=1;k<n;k++){
				int mm = Integer.parseInt(a1[k]);
				int difference=  before2-mm;
				//pl("before: "+before2+", mm:"+mm);
				if(difference>findMax2){
					findMax2=difference;
				}else{
				
				}
				before2 = mm;

			}
			before2=Integer.parseInt(a1[0]);
			for( int k=1;k<n;k++){
				int mm = Integer.parseInt(a1[k]);
				//pl("before: "+before+", mm:"+mm);
				int difference=  before2-mm;
				//p("[ difference  "+difference+"]");
				
				if(before2<findMax2){
					totalSum2+=before2;
					//p("+"+findMax2);
				}else{
					totalSum2+=findMax2;
					//p("+"+findMax2);

				}
				
				before2 = mm;

			}
			//pl("findMax is "+findMax2);

			//pl("totalSum:"+totalSum);
			//pl("totalSum2:"+totalSum2);

			//pl("");
			
			
			//pl(r1);
			output+="Case #"+(i+1)+": "+totalSum+" "+totalSum2+"\n";
			//arr[i]=needTobeAdded;
			//System.out.println();
		}

		
		Writer writer = null;

		try {
			writer = new BufferedWriter(new OutputStreamWriter(
					new FileOutputStream("generatedNumber.txt"), "utf-8"));
			writer.write(output);

		} catch (IOException ex) {
			// report
		} finally {
			try {
				writer.close();
			} catch (Exception ex) {
			}
		}

	}
}
