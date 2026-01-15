



public class Problem1A {

	private static BufferedReader in;
	private static PrintWriter out;
	public static boolean SUBMIT = true;
	public static final String NAME = "A-small-attempt1";
	static String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	
	public static void main(String[] args) throws IOException{
		if (SUBMIT) {
		      in = new BufferedReader(new FileReader(NAME + ".in"));
		      out = new PrintWriter(NAME + ".out");
		    } else {
		      in = new BufferedReader(new FileReader("testA.in"));
		      out = new PrintWriter("testA.out");
		    }

		 	String line = in.readLine();
		    int totalCases = Integer.parseInt(line);
		    for(int caseNum=1;caseNum<=totalCases;caseNum++){
		    	out.print("Case #" + caseNum + ": ");
		    	in.readLine();
		    	LinkedHashMap<String, Integer> map = new LinkedHashMap<String, Integer>();
				String test = in.readLine();
				String[] number = test.split(" ");
				for(int k=0;k<number.length;k++){
					 map.put(""+alpha.charAt(k), Integer.parseInt(number[k]));
				}
				
				String result = "";
				
				while(true){
				
				int current = -1;
				String equalKey = "";
				String bigKey = "";
				String currentKey = "";
				boolean zeroFOund = false;
				
				Iterator it = map.entrySet().iterator();
				while (it.hasNext()) {
				    Map.Entry pair = (Map.Entry)it.next();
				    int val = (int) pair.getValue();
				    if(val == 0){
				    	zeroFOund = true;
				    	continue;
				    }else{
				    	zeroFOund = false;
				    }
				    if(current < val){
				    	current = val;
				    	currentKey = (String) pair.getKey();
				    	equalKey = "";
				    	bigKey = (String) pair.getKey();
				    }else if(current == val){
				    	equalKey = currentKey + (String) pair.getKey();
				    }
				    System.out.println(pair.getKey() + " = " + pair.getValue());
				   // it.remove(); // avoids a ConcurrentModificationException
				}
				
				if(equalKey.length() > 0){
					for(int i=0;i<2;i++){
						String key = ""+equalKey.charAt(i);
						int value = map.get(key);
						value = value - 1;
						map.put(key, value);
						result = result + key;
					}
					result = result + " ";
				}else if(bigKey.length() > 0){
					int value = map.get(bigKey);
					if(value >= 2){
						value = value - 2;	
						result = result + bigKey + bigKey + " ";
					}else{
						value = value - 1;
						result = bigKey + " " + result;
					}
					map.put(bigKey, value);
				}
				
				if(zeroFOund){
					break;
				}
				}
				System.out.println(result);
				out.print(result);
				out.println();
		    }

		    out.close();
		    System.exit(0);
	}
	
	
}
